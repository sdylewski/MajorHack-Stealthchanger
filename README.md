# Stealthchanger
My notes and files for Stealthchanger

It was difficult to figure out my stealthchanger build, and many things are confusing still.  Here's my setup:

Initial Voron 2.4 300 with Stealthburner

Plan to move to 4 toolheads, mostly dragonburner since it seems well supported by Stealthchanger already.

## Docking / Door Buffer / etc
* Door buffer & crossbar, default from Draftshift
* [Dragonburner magnetic docks](https://discord.com/channels/1226846451028725821/1320029517376655462/1347878802751230005) (not in github, only Discord)

## Cable management
* CAN 
## Toolheads
### Stealthburner
* Regular dock
* Magnetic dock?
* TBD: [Filament runout](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/RNGIllSkillz/IllFilamentRunout)
* 

### Dragonburners
* EBB36 CANn toolhead board, using UserMod [TheSin PCB36 Mount](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/TheSin-/PCB36_Mount)
* Needs the toolhead attachment to shuttle from TheSin also: 
* [Magnetic dock](https://discord.com/channels/1226846451028725821/1320029517376655462/1347878802751230005) for Dragonburner, Discord only
* [Dragonburner numbered cowls](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/traxman25) (not compatible with magnetic bases?)

## Software
Sounds like I should use "Klipper-toolchanger-easy" instead of the default repo.  
* https://github.com/jwellman80/klipper-toolchanger-easy?tab=readme-ov-file
* 

## Setup & Slicing
How to handle the build area loss from the docks? 
<img width="895" height="757" alt="image" src="https://github.com/user-attachments/assets/1b72cddc-5580-4371-aec5-24bdd37dfcf3" />

* [Stealthchanger plate image generator](https://jsfiddle.net/ng3Lawyb/).  This shows where to print short objects so you don't loose too much area in the front!
* 
