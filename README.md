# Stealthchanger
My notes and files for Stealthchanger

It was difficult to figure out my stealthchanger build, and many things are confusing still.  Here's my setup:

Initial Voron 2.4 300 with Stealthburner

Plan to move to 4 toolheads, mostly dragonburner since it seems well supported by Stealthchanger already.

## References
* DraftShift Design
* Good [instructions from Cergs](https://github.com/EasterWorks/Cergs-Stealthchanger/blob/main/Hardware-And-Calibration.md) and background found here

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
* Needs the toolhead attachment to shuttle from TheSin also: 
* [Magnetic dock](https://discord.com/channels/1226846451028725821/1320029517376655462/1347878802751230005) for Dragonburner, Discord only
* [Dragonburner numbered cowls](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/traxman25) (not compatible with magnetic bases?)

## Software & Calibration
Sounds like I should use "Klipper-toolchanger-easy" instead of the default repo.  
* https://github.com/jwellman80/klipper-toolchanger-easy?tab=readme-ov-file
* Klipper-toolchanger-easy is just for installation.  After installing that, still follow the [stealthchanger wiki](https://github.com/DraftShift/StealthChanger/wiki/Calibration) for configuration and setup!
* Nudge XY calibration
* [Dock Tuner macro]((https://github.com/Contomo/klipper-toolchanger-hard/blob/main/examples/dock%20location/fixed/dock_tuner.cfg)  how to install?
* LEDs: [Example from Draftshift](https://github.com/DraftShift/klipper-toolchanger?tab=readme-ov-file) designs page
* [LED Effects](https://github.com/julianschill/klipper-led_effect)

SW Setup issues:
* if using "fan0 or fan2" from slicer, need to change those back to named fans.


## Setup & Slicing
How to handle the build area loss from the docks? 
<img width="895" height="757" alt="image" src="https://github.com/user-attachments/assets/1b72cddc-5580-4371-aec5-24bdd37dfcf3" />

* [Stealthchanger plate image generator](https://jsfiddle.net/ng3Lawyb/).  This shows where to print short objects so you don't loose too much area in the front!
* 
