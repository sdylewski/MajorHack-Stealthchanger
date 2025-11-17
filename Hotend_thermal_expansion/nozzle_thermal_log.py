#!/usr/bin/env python3
import sys
import os
import csv
from datetime import datetime

BASE_DIR = os.path.expanduser("~/printer_data/config/plots")
RUN_INFO_FILE = os.path.join(BASE_DIR, "nozzle_thermal_current_run.txt")


def ensure_base_dir():
    os.makedirs(BASE_DIR, exist_ok=True)


def make_run_id(tool_name: str) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{tool_name}_{ts}"


def write_current_run(run_id: str):
    with open(RUN_INFO_FILE, "w") as f:
        f.write(run_id.strip() + "\n")


def read_current_run():
    if not os.path.exists(RUN_INFO_FILE):
        return None
    with open(RUN_INFO_FILE, "r") as f:
        return f.read().strip() or None


def get_paths_for_run(run_id: str):
    raw_file = os.path.join(BASE_DIR, f"nozzle_thermal_{run_id}_raw.csv")
    summary_file = os.path.join(BASE_DIR, f"nozzle_thermal_{run_id}.csv")
    plot_file = os.path.join(BASE_DIR, f"nozzle_thermal_{run_id}.png")
    comp_file = os.path.join(BASE_DIR, f"nozzle_thermal_{run_id}_comp.png")
    return raw_file, summary_file, plot_file, comp_file


def cmd_init(tool_name: str):
    ensure_base_dir()

    tool_name = tool_name.strip().upper()
    if not tool_name.startswith("T"):
        tool_name = "T" + tool_name

    run_id = make_run_id(tool_name)
    write_current_run(run_id)

    raw_file, summary_file, _, _ = get_paths_for_run(run_id)

    # Raw taps
    with open(raw_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "tool", "temperature_C", "tap_index", "z_raw"])

    # Summary (will be overwritten in plot step)
    with open(summary_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["temperature_C", "z_height"])

    print(f"[nozzle_thermal] Init run_id={run_id}")
    print(f"[nozzle_thermal] Raw file: {raw_file}")


def cmd_add_raw(tool_name: str, temp_str: str, tap_str: str, z_str: str):
    ensure_base_dir()
    run_id = read_current_run()
    if run_id is None:
        print("[nozzle_thermal] No active run – call 'init <tool>' first.")
        return

    raw_file, _, _, _ = get_paths_for_run(run_id)

    try:
        temp = float(temp_str)
        tap = int(tap_str)
        z = float(z_str)
    except ValueError:
        print(f"[nozzle_thermal] Invalid numeric values: temp={temp_str}, tap={tap_str}, z={z_str}")
        return

    ts = datetime.now().isoformat(timespec="seconds")
    tool_name = tool_name.strip().upper()

    with open(raw_file, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([ts, tool_name, temp, tap, z])

    print(f"[nozzle_thermal] Logged raw: tool={tool_name} T={temp}C tap={tap} z={z} run_id={run_id}")


def linear_regression(xs, ys):
    n = len(xs)
    if n < 2:
        return None, None

    Sx = sum(xs)
    Sy = sum(ys)
    Sxx = sum(x * x for x in xs)
    Sxy = sum(x * y for x, y in zip(xs, ys))
    denom = n * Sxx - Sx * Sx
    if denom == 0:
        return None, None

    a = (n * Sxy - Sx * Sy) / denom
    b = (Sy - a * Sx) / n
    return a, b


def cmd_plot(ref_temp=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ensure_base_dir()

    if ref_temp is None:
        ref_temp = 150.0

    run_id = read_current_run()
    if run_id is None:
        print("[nozzle_thermal] No active run – call 'init <tool>' first.")
        return

    raw_file, summary_file, plot_file, comp_file = get_paths_for_run(run_id)

    if not os.path.exists(raw_file):
        print(f"[nozzle_thermal] Missing raw file: {raw_file}")
        return

    # Load raw taps: group by temperature
    temp_to_zs = {}
    with open(raw_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                T = float(row["temperature_C"])
                tap = int(row["tap_index"])
                z = float(row["z_raw"])
            except Exception:
                continue

            # We only log non-ignored taps from the macro,
            # so just group them all here
            temp_to_zs.setdefault(T, []).append(z)

    if not temp_to_zs:
        print("[nozzle_thermal] No raw data to process.")
        return

    # Build per-temperature averages
    temps = sorted(temp_to_zs.keys())
    avg_zs = []
    for T in temps:
        zs = temp_to_zs[T]
        if not zs:
            continue
        avg_z = sum(zs) / len(zs)
        avg_zs.append(avg_z)

    if not avg_zs:
        print("[nozzle_thermal] No valid average data.")
        return

    # Write summary CSV
    with open(summary_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["temperature_C", "z_height"])
        for T, z in zip(temps, avg_zs):
            w.writerow([T, z])

    print(f"[nozzle_thermal] Wrote summary: {summary_file}")

    # Regression on summary data
    a, b = linear_regression(temps, avg_zs)
    if a is not None:
        slope_mm = a
        slope_um = a * 1000.0
        print("[nozzle_thermal] Linear fit: Z = a*T + b")
        print(f"    a = {slope_mm:.6f} mm/°C = {slope_um:.3f} µm/°C")
        print(f"    b = {b:.6f} mm")
    else:
        print("[nozzle_thermal] WARNING: could not compute linear regression.")
        slope_mm = None

    # --- Main Z vs T plot ---
    plt.figure()
    plt.plot(temps, avg_zs, "o", label="Average Z per temp")

    if a is not None:
        xs_line = [min(temps), max(temps)]
        ys_line = [a * x + b for x in xs_line]
        plt.plot(xs_line, ys_line, "-", label="Linear fit")

    plt.xlabel("Temperature (°C)")
    plt.ylabel("Z height (mm)")
    plt.title(f"Nozzle Thermal Expansion: {run_id}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot_file)

    print(f"[nozzle_thermal] Saved plot: {plot_file}")

    # --- Compensation plot ---
    if slope_mm is None:
        print("[nozzle_thermal] Skipping compensation plot (no fit).")
        return

    a = slope_mm
    Z_ref = a * ref_temp + b

    temps_comp = [T for T in temps if T >= ref_temp]
    if not temps_comp:
        print(f"[nozzle_thermal] No temps >= reference {ref_temp}°C for compensation.")
        return

    comp_vals = []
    for T in temps_comp:
        Z_T = a * T + b
        comp = Z_ref - Z_T
        comp_vals.append(comp)

    print(f"[nozzle_thermal] Using reference temperature T_ref = {ref_temp:.1f}°C")
    print("[nozzle_thermal] Compensation (mm):")
    print("    comp(T) = a * (T_ref - T)")
    print(f"    where a = {a:.6f} mm/°C, T_ref = {ref_temp:.1f}°C")

    plt.figure()
    plt.plot(temps_comp, comp_vals, "o-", label="Z compensation")
    plt.axhline(0.0, linestyle="--", linewidth=1, label="Zero compensation")

    plt.xlabel("Temperature (°C)")
    plt.ylabel(f"Z compensation (mm) relative to {ref_temp:.1f}°C")
    plt.title(f"Nozzle Z Compensation vs T (ref {ref_temp:.1f}°C) - {run_id}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(comp_file)

    print(f"[nozzle_thermal] Saved compensation plot: {comp_file}")


def main():
    argv = sys.argv

    if len(argv) < 2:
        print("Usage: nozzle_thermal_log.py <init|add_raw|plot> ...")
        return

    cmd = argv[1].lower()

    if cmd == "init":
        if len(argv) != 3:
            print("Usage: nozzle_thermal_log.py init <tool>")
            return
        cmd_init(argv[2])

    elif cmd == "add_raw":
        if len(argv) != 6:
            print("Usage: nozzle_thermal_log.py add_raw <tool> <temp> <tap> <z>")
            return
        cmd_add_raw(argv[2], argv[3], argv[4], argv[5])

    elif cmd == "plot":
        ref_temp = None
        if len(argv) >= 3:
            try:
                ref_temp = float(argv[2])
            except ValueError:
                print(f"[nozzle_thermal] Invalid reference temp '{argv[2]}', using default 150°C.")
                ref_temp = None
        cmd_plot(ref_temp)

    else:
        print(f"Unknown command: {cmd}")
        print("Valid commands: init, add_raw, plot")


if __name__ == "__main__":
    main()

