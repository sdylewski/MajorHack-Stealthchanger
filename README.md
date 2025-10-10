# Stealthchanger
## Introduction
It was difficult to figure out my stealthchanger build, so this is my attempt to define a standard build that works and correct a lot of the errors in the documentation.

I started with an initial LDO Voron 2.4 300 with Stealthburner toolhead running on CAN (SB2209 CAN RP2040 board), with a Rapido Ace hotend and Galileo2 Extruder. 

Plan is to move slowly to 4 toolheads, mostly dragonburner since it seems well supported by Stealthchadnger already. I may also make one Dragonburner, one A4T, one Anthead, etc. to try them out and see how I like each one. 

What worked well for me was to do the following in this order:

1. Decide on what you want to do! Then be prepared to change your mind halfway through, and re-print stuff, take everything apart, and do it again.
2. Upgrade to CAN or USB toolhead board for primary toolhead. 
2. Install CAN or USB distribution board and "backpack"
3. Install umbilical cable to primary toolhead (T0)
4. Install CNC shuttle and backplate for your toolhead
5. Get printer working again to print other parts.
6. Print door buffer (done anytime)
7. Install top hat (done anytime)
8. Install Docks for your toolhead (getting harder)
9. Build 2nd + toolheads, install with umbilicals.
10. Install Klipper-toolchanger-easy (KTE)
11. Configure KTE
12. Calibrate offsets
13. Calibrate dock locations
14. Add Additional toolheads and docks

## Main References
* DraftShift Design Stealthchanger Wiki
* DraftShift Design Repositories
* Good [instructions from Cergs](https://github.com/EasterWorks/Cergs-Stealthchanger/blob/main/Hardware-And-Calibration.md) and background found here
	
## Main Components & Options
<table>
<tr><th>Components</th><th>Details</th><th>Options</th></tr>

<tr>
	<td valign=top><strong>Shuttle</strong><br>
      <img src="Images/Fystec_CNC_Shuttle.jpg" alt="Fystec shuttle" width="220">
	</td>
	<td valign=top>
	</td>
	<td valign=top>
	<ul><li>LDO kit</li>
	</td>
</tr>
<tr>
	<td valign=top> 
	</td>
	<td valign=top>
	</td>
	<td valign=top>
	</td>
</tr>
<tr>
	<td valign=top> 
	</td>
	<td valign=top>
	</td>
	<td valign=top>
	</td>
</tr>
<tr>
	<td valign=top> 
	</td>
	<td valign=top>
	</td>
	<td valign=top>
	</td>
</tr>
</table>


## Docking / Door Buffer / etc
* Door buffer & crossbar, default from Draftshift
* [Dragonburner magnetic docks](https://discord.com/channels/1226846451028725821/1320029517376655462/1347878802751230005) (not in github, only Discord)
* option:  replace front xy idlers: [Beefy Front Idlers](https://github.com/clee/VoronBFI)
* Looks like I should try to change my idlers to [MiniBFI](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/BT123/MiniBFI%20%2B%20MicroBFI)

## Cable management
* CAN 
## Toolheads
* [Fystec CNC Shuttle](https://www.fysetc.com/products/fysetc-stealthchanger-cnc-shuttle-kit-sb-combo-v2-board-tool-distribution-board-h36-board?variant=44927105040559) (includes all dowel pins, magnets, and hardware for 6 toolheads!)
### Stealthburner
* [SB2209 CAN 2040](https://github.com/bigtreetech/EBB/blob/master/EBB%20SB2209%20CAN%20(RP2040)/Hardware/EBB%20SB2209%20CAN%20V1.0（RP2040）-Pin.png)
* Regular dock
* Magnetic dock?
* [Happy Crab dock](https://www.printables.com/model/994635-stealthchanger-stealthburner-minimal-docks-aka-hap)
* TBD: [Filament runout](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/RNGIllSkillz/IllFilamentRunout)
* [Screwed pins backplate](https://www.printables.com/model/1358108-stealtchanger-stealthburner-backplate-with-screwed/comments)
* 
### Dragonburners
* [EBB36 CANn toolhead board](https://github.com/bigtreetech/EBB/blob/master/EBB%20CAN%20V1.1%20and%20V1.2%20(STM32G0B1)/EBB36%20CAN%20V1.1%20and%20V1.2/Hardware/EBB36%20CAN%20V1.1%26V1.2-PIN.png), using UserMod [TheSin PCB36 Mount](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/TheSin-/PCB36_Mount)
* [22mm standoffs](https://www.printables.com/model/1440113-m3-heatset-standoffs-10mm-30mm) to mount the toolhead board to Orbiter 2 extruder
* Needs the toolhead attachment to shuttle from TheSin also: 
* [Magnetic dock](https://discord.com/channels/1226846451028725821/1320029517376655462/1347878802751230005) for Dragonburner, Discord only
* [Dragonburner numbered cowls](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/traxman25) (not compatible with magnetic bases?)

## Software & Calibration
Sounds like I should use "Klipper-toolchanger-easy" instead of the default repo.  
* https://github.com/jwellman80/klipper-toolchanger-easy?tab=readme-ov-file
* Even when using klipper-toolchanger-easy, use the examples in the [Draftshift Klipper-toolchanger folder](https://github.com/DraftShift/klipper-toolchanger)
* Klipper-toolchanger-easy is just for installation.  After installing that, still follow the [stealthchanger wiki](https://github.com/DraftShift/StealthChanger/wiki/Calibration) for configuration and setup!
* Nudge XY calibration
* [Dock Tuner macro]((https://github.com/Contomo/klipper-toolchanger-hard/blob/main/examples/dock%20location/fixed/dock_tuner.cfg)  how to install?
* LEDs: [Example from Draftshift](https://github.com/DraftShift/klipper-toolchanger?tab=readme-ov-file) designs page
* [LED Effects](https://github.com/julianschill/klipper-led_effect) TBD

SW Setup issues:
* if using "fan0 or fan2" from slicer, need to change those back to named fans.

## Calibration !!
I found that the default instructions on the Draftshift wiki were wrong. I started with 1 Stealthburner as T0, and 1 Dragonburner as T1.  Assumed all the calibration would allow for this, but after three days of frustration, here's my learnings:
1. If you home with T1, Anytime the gcode_offsets change for T>0, the dock positions need to be updated.
2. When you get your T1 dock positions,M114 reports the gcode positions. That is, the raw machine position with any gcode_offsets and probe_offsets.  I found that I needed to use the raw machine position in my dock locations set in params_park_x,y,z.  This means using my Fluidd-reported location without offsets, NOT M114 locations, which include all the offsets.
3. When people use the same toolhead for all their tools, they don't notice this difference because each tool's gcode_offset_x,y is near zero.
4. Another way to get around this difficulty would be to home with T0 (no gcode or probe offsets!), and then, when putting T1 on, DON'T initialize_toolchanger.  This should (to be verified) keep the machine coordinates.
5. FYI, because initialize_toolchanger applies the probe and gcode_offsets, this is a feature, not a bug. This allows you to home with any tool, and the dock locations will be the same.


## Setup & Slicing
How to handle the build area loss from the docks? 
<img width="895" height="757" alt="image" src="https://github.com/user-attachments/assets/1b72cddc-5580-4371-aec5-24bdd37dfcf3" />

* [Stealthchanger plate image generator](https://jsfiddle.net/ng3Lawyb/).  This shows where to print short objects so you don't loose too much area in the front!
* 
