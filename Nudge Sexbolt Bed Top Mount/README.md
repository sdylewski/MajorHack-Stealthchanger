# Nudge or Sexbolt Bed Top Mount



## Overview & Design
I tried the design from ___ and ___ and found my bracket was moving around a bit, and wanted something a bit more sturdy and perhaps simpler if possible.  I also wanted something that would work with the [Nudge](https://github.com/zruncho3d/nudge/blob/main/README.md) or [Sexbolt](https://mods.vorondesign.com/details/t1DBVlcUBbdEK6habEsVzg) alignment hardware because my Nudge was not working well until I got the copper M3x6 SHCS. I'm getting an X,Y accuracy of < 0.001 mm.

Chages from original design:

* This design is stronger, with longer brackets to reduce bending and allow 2 screws/hammerheads to attach to 2020 railing.
* 2 options to have bushings or no bushings.  I find that the one without bushings works well for me!
* Sexbolt or Nudge mountable

## Bill of Materials
### Bracket
* (2) M3x4x5 voron heatset inserts
* (2-6) 6x3 magnets, depending on strength

### Bracket block
* (2) M4 x 12 dowel pins. one end rounded, other end M3 tapped.  Same as the ones from Stealthchanger shuttle.
* (2) M3 x 16 SHCS for screwing in dowel pins.
* (2) 6x3 magnets
* (2) M3 x 20 SHCS for attaching bracket to 2020 T-nuts
* (2) M3 T-nuts

### Bracket dock option (A) No bushings
* (1) M3x4x5 voron heatset insert
* (2) 6x3 magnets
* (2) m2x10 SHCS for attaching optional switch (optional)
* (1) M3x16 BHCS or SHCS for attaching bracket block to bracket

### Bracket dock option (B) With bushings
* (2) 4x6x6mm brass bushing (4mm id x 6mm od x 6mm tall) same as stealthchanger shuttle
* (2) M4x (1) M3x4x5 heatset insert
* (2) 6x3 magnets
* (2) m2x10 SHCS for attaching optional switch (optional)
* (1) M3x16 BHCS or SHCS for attaching bracket block to bracket

### Rear dock
* (1) M3x20?
* (2) 6x3mm magnets
  
### Nudge attachment
* (2) M3x

### Sexbolt attachment
* (2) M3x
  
## Assembly


## Usage

* Use T0
* Home all
* QGL
* Manually move the nozzle a mm or two dirctly above the probe
* run `TOOL_LOCATE_SENSOR`
to find the exact location. This returns your T0 probe location. 
* Then, follow the commands for your sensor:

### Nudge
* In the file "calibrate_offsets.cfg", enter the sensor location in gcode macro section `NUDGE_MOVE_OVER_PROBE` 
* Save config and restart 
* Run `Nudge_find_tool_offset` or `nudge_find_tool_offsets` to do all tools.

### SexBolt
* Enter the sensor location in `Nudge_move_over_probe` gcode macro section
* Save config and restart 
* Run `TOOL_CALIBRATE_TOOL_OFFSET`
* `TOOL_CALIBRATE_SAVE_TOOL_OFFSET` (not sure if this is correct)


## Accuracy
Nudge: For my setup, using the Nudge-recommended [printer-experiments](https://github.com/zruncho3d/printer-experiments) repo, for 10 iterations:
```
Printing stats for x:
  Range: 0.0328
  Min: 71.1219
  Max: 71.1547
  Median: 71.1297
  Standard Deviation: 0.0089
Printing stats for y:
  Range: 0.0312
  Min: 305.3906
  Max: 305.4219
  Median: 305.4086
  Standard Deviation: 0.0096
Printing stats for z:
  Range: 0.0137
  Min: 30.5755
  Max: 30.5892
  Median: 30.5799
  Standard Deviation: 0.0039
```




