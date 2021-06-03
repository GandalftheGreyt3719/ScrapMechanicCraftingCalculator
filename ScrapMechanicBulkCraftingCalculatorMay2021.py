#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  s.py
#  
#  Copyright 2021 GandalfThrGreytGamer <Jaxer6563@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


"""
This is a Calculator that will help in crafting Blocks, Interactive Parts, Consumables, and Parts in bulk.
When prompted, choose from a list of parts, and then input the amount needed.
As a simple example, We will use the Glowstick crafting. 
1st, the program will ask for how much you want.
2nd, then it will multiply the value by the already known values. In the case of glowsticks, at 32 glowsticks, it will be 32 glow, 32 chemical, and 3-ish minutes.

"""
import time, os, platform

#for crossplatform support
clearcmd = 0
opsys = platform.system()
if opsys == "Windows":
	clearcmd = "cls"
if opsys == "Linux":
	clearcmd = "clear"
	
def clearscreen():  #clears the screen. 
    os.system(clearcmd)
def loading():    #loading() acts as a loading screen. 1st is clears the screen, then displays a grey bar, that every 1/8 of a second clears and adds a new bar with a white rectangle.
	clearscreen()
	time.sleep(.125)
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						▒▒▒▒▒▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						█▒▒▒▒▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						██▒▒▒▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						███▒▒▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						████▒▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						█████▒▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						██████▒▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						███████▒▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						████████▒▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						█████████▒▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						██████████▒▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						███████████▒ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n						████████████ \n						 (LOADING)")
	time.sleep(.125)
	clearscreen()
	time.sleep(.125)
	

	 
    
#Blocks
Concrete1 = ("5 Scrap Stone, 5 Water, and 5 Chemical for 10 Concrete 1 [10 Sec. Craft Time]")
Wood1 = ("15 Scrap Wood for 10 Wood 1 [10 Sec. Craft Time]")
Metal1 = ("15 Scrap Metal for 10 Metal 1 [10 Sec. Craft Time]")
BarrierBlock = ("10 Wood 1 and 1 Paint Ammo for 10 Barrier Blocks [10 Sec. Craft Time]")
TileBlock = ("10 Scrap Stone and 1 Paint Ammo for 10 Tile Blocks [10 Sec. Craft Time]")
BrickBlock = ("10 Scrap Stone for 10 Brick Blocks [10 Sec. Craft Time]")
GlassBlock = ("10 Sand and 1 Ember for 10 Glass Blocks [10 Sec. Craft Time]")
GlassTile = ("10 Sand and 1 Ember for 10 Glass Tiles [10 Sec. Craft Time]")
PathLight = ("10 Metal 1 and 1 Circut Board for 10 Path Light Blocks [10 Sec. Craft Time]")
CardBoard = ("5 Scrap Wood for 20 Cardboard Blocks [5 Sec. Craft Time]")
Wood2 = ("15 Wood 1 and 1 Metal 1 for 10 Wood 2 [10 Sec. Craft Time]")
Wood3 = ("15 Wood 2 and 1 Metal 2 for 10 Wood 3 [10 Sec. Craft Time]")
Metal2 = ("15 Metal 1, 1 Ember, and 2 Water [10 Sec. Craft Time]")
Metal3 = ("20 Metal 2, 2 Ember, and 4 Water [10 Sec. Craft Time]")
Concrete2 = ("15 Concrete 1 and 2 Metal 2 for 10 Concrete 2 [10 Sec. Craft Time]")
Concrete3 = ("15 Concrete 2 and 2 Metal 3 for 10 Concrete 3 [10 Sec. Craft Time]")
ExtrudedMetal = ("5 Metal 1 for 10 Extruded Metal [10 Sec. Craft Time]")
BubblePlastic = ("5 Crude Oil for 10 Bubble Plastic [10 Sec. Craft Time]")
Carpet = ("5 Cotton and 1 Paint Ammo for 10 Carpet Blocks [10 Sec. Craft Time]") 
Net = ("2 Metal 1 for 10 Net Blocks [10 Sec. Craft Time]")
SolidNet = ("5 Metal 2 for 10 Solid Net Blocks [10 Sec. Craft Time]")
PunchedSteel = ("5 Metal 1 for 10 Punched Steel Blocks [10 Sec. Craft Time]")
RestroomBlock = ("10 Scrap Stone and 1 Bees Wax for 10 Restroom Blocks [10 Sec. Craft Time]")
DiamondPlate = ("10 Metal 1 for 10 Diamond Plate Block [10 Sec. Craft Time]")
Sand = ("5 Scrap Stone for 10 Sand [10 Sec. Craft Time]")
ArmoredGlass = ("10 Glass, 2 Net Block, and 1 Ember for 10 Armored Glass [10 Sec. Craft Time]")
#Parts
Wheel = ("15 Wood 1, 5 Metal 1, and 6 Bees Wax for 1 Wheel [20 Sec. Craft Time]")
BigWheel = ("40 Wood 1, 10 Metal, and 8 Bees Wax for 1 Big Wheel for [30 Sec. Craft Time]")
IBeamShort = ("1 Metal 1 for 1 Short I-Beam ")
IBeamLong = ("3 Metal 1 for 1 Long I-Beam ")
IBeamCorner = ("1 Metal 1 for 1 I-Beam Corner ")
IBeamHolder = ("1 Metal 1 for 1 I-Beam Holder ")
IBeamEnd = ("1 Metal 1 for 1 I-Beam End ")
SmallRectangleWindow = ("5 Glass and 5 Metal 1 for Small Rectangle Window ")
SquareWindow = ("10 Glass and 10 Metal 1 for 1 Square Window ")
LargeRectangleWindow = ("15 Glass and 10 Metal 1 for 1 Large Rectangle Window ")
LargeWindshield = ("20 Glass and 10 Metal 1 for 1 Large Windshield ")
SmallWindShield = ("10 Glass and 5 Metal 1 for 1 Small Windshield ")
AirConditioner = ("10 Metal 1 and 3 Circut Boards for 1 Air Conditioner ")
PipeShort = ("1 Metal 1 for 1 Pipe Short ")
PipeLong = ("3 Metal 1 for 1 Pipe Long ")
PipeCorner = ("1 Metal 1 for 1 Pipe Corner ")
PipeJoin = ("1 Metal 1 for 1 Pipe Join ")
Valve  = ("1 Metal 1 for 1 Valve ")
SmallPipeShort = ("1 Metal 1 for 1 Small Pipe Short ")
SmallPipeLong = ("3 Metal 1 for 1 Small Pipe Long ")
SmallPipeBend = ("1 Metal 1 for 1 Small Pipe Bend ")
SmallPipeTee = ("1 Metal 1 for 1 Small Pipe Tee ")
SmallPipeCorner = ("1 Metal 1 for 1 Small Pipe Corner ")
SmallPipe4Way = ("1 Metal 1 for 1 Small Pipe 4 Way ")
SmallPipe4WayTee = ("1 Metal 1 for 1 Small Pipe 4 Way Tee ")
SmallPipe5Way = ("1 Metal 1 for 1 Small Pipe 5 Way ")
SmallPipe6Way = ("1 Metal 1 for 1 Small Pipe 6 Way ")
ToiletPaper = ("1 Scrap Wood for 1 Toilet Paper ")
Sink = ("5 Metal 1 for 1 Sink ")
Mug = ("1 Metal 1 for 1 Mug ")
MannequinBoot = ("1 Woc Steak, 2 Wood 1, 1 Paint Ammo, 1 Bees Wax for 1 Mannequin Boot ")
MannequinHand = (" 2 Wood 1, 1 Paint Ammo, 3 Bees Wax for 1 Mannequin Boot ")
DuckStatue = ("1 Wood 1, 1 Paint Ammo, 3 Bees Wax, and 1 Glue for 1 Duck Statue")
TrafficCone = ("10 Metal 1 and 1 Paint Ammo for 1 Traffic Cone [15 Sec. Craft Time]")
ScrapWheel = ("20 Scrap Wood and 5 Scrap Metal for 1 Scrap Wheel [15 Sec. Craft Time]")
Bucket = ("5 Scrap Metal for 1 Bucket [20 Sec. Craft Time]")
SoilBag = ("10 Scrap Wood, 10 Sand, and 2 Carrots for 1 Soil Bag [20 Sec. Craft Time]")
#Interactive
Beacon = ("10 Metal 2, 1 Radio, and 10 Circut Boards for 1 Beacon [45 Sec. Craft Time]")
SportSuspension = ("5 Metal 2 and 2 Crude Oil for 1 Sport Suspension [45 Sec. Craft Time]")
OffRoadSuspension = ("10 Metal 2 and 2 Crude Oil for 1 Off-Road Suspension [45 Sec. Craft Time]")
DriverSeat = ("10 Cotton, 5 Metal 1, 3 Circut Board, and 1 Component Kit for 1 Lvl 1 Driver's Seat[1 Minute Craft Time]")
Seat = ("10  Cotton, 5 Metal 1, and 2 Circut Board for 1 Seat [40 Sec. Craft Time]")
DriverSaddle = ("5 Cotton, 5 Metal 1, 3 Circut Board, and 1 Component Kit for 1 Lvl 1 Driver's Saddle[1 Minute Craft Time]")
Saddle = ("5  Cotton, 5 Metal 1, and 2 Circut Board for 1 Saddle [40 Sec. Craft Time]")
GasEngine = ("20 Metal 2, 5 Crude Oil, 5 Circut Board, and 3 Component for 1 Lvl 1 Gas Engine [1:30 Craft Time]")
ElectricEngine = ("20 Metal 2, 5 Battery, 10 Circut Board, and 5 Component for 1 Lvl 1 Electric Engine [1:30 Craft Time]")
Thruster = ("40 Metal 3 and 10 Component Kit for 1 Lvl 1 Thruster [2 Minute Craft Time]")
Controller = ("5 Metal 1, 5 Circut Board, 1 Component Kit, and 3 Glue for 1 Lvl 1 Controller [40 Sec. Craft Time]")
Sensor = ("1 Metal 1, 1 Glass, 2 Circut Board, and 2 and 2 Glue for 1 Lvl 1 Sensor [30 Sec. Craft Time]")
Piston = ("10 Metal 2, 2 Crude Oil, 2 Circut Board, 1 Component Kit for 1 Lvl 1 Piston [40 Sec. Craft Time]")
GasContainer = ("20 Metal 1, 5 Circut Board, 15 Paint Ammo, and 2 Glue for 1 Gas Container [40 Sec. Craft Time]")
WaterContainer = ("10 Metal 1, 10 Bees Wax, 5 Circut Board, and 2 Glue for 1 Water Container [1 Minute Craft Time]")
BatteryContainer = ("20 Metal 1, 5 Circut Board, 15 Paint Ammo, and 2 Glue for 1 Battery Container [40 Sec. Craft Time]")
SawBlade = ("10 Metal 2 and 20 Metal 1 for 1 Saw Blade [1:30 Craft Time]")
Drill = ("20 Metal 2 and 30 Metal 1 for 1 Drill [1:30 Craft Time]")
VacuumPump = ("10 Metal 2, 5 Bees Wax, 5 Circut Board for 1 Vacuum Pump [1:30 Craft Time]")
VacuumPipe = ("10 Glass, 5 Metal 2, 2 Circut Board for 1 Vacuum Pump [15 Sec. Craft Time]")
VacuumPipeCorner = ("10 Glass, 5 Metal 2, and 2 Circut Board for 1 Vacuum Pipe Corner [15 Sec. Craft Time]")
LargeChest = ("60 Metal 1, 5 Circut Board, 3 Component Kit, and 5 Glue for 1 Large Chest [1:30 Craft Time]")
RefineBot = ("60 Metal 1, 5 Circut Board, and 5 Component Kit for 1 RefineBot")
ResourceCollector = ("30 Metal 1 for 1 Resource Collector")
CraftBot = ("90 Scrap Metal, 10 Circut Board, and 10 Component Kit for 1 CraftBot")
ScrapGasEngine = ("30 Scrap Metal, 20 Scrao Wood, and 3 Circut Board for 1 Scrap Gas Engine [35 Sec. Craft Time]")
ScrapDriverSeat = ("10 Scrap Metal, 100 Scrap Wood, and 2 Circut Board for 1 Scrap Driver Engine [35 Sec. Craft Time]")
ScrapSeat = ("50 Scrap Wood and 1 Circut Board for 1 Scrap Seat [25 Sec Craft Time]")
RespawnBed = ("50 Wood 1, 20 Cotton, and 10 Paint Ammo for 1 Respawn Bed [1:00 Craft Time]")
Chest = ("40 Metal 1 and 2 Glue for 1 Chest [1:00 Craft Time]")
Fridge = ("10 Metal 1, 2 Chemical, 1 Circut Board, and 2 Glue for 1 Fridge [1:00 Craft Time]")
ChemicalContainer = ("10 Metal 2, 20 Glass, 5 Circut Board, and 2 Glue for 1 Chemical Container [1:00 Craft Time]")
Bearing = ("5 Scrap Metal for 1 Bearing [15 Sec. Craft Time]")
Toilet = ("5 Metal 1 and 5 Wood 1 for 1 Toilet [5 Sec. Craft Time]")
Switch = ("1 Scrap Metal and 1 Circut Board for 1 Switch [25 Sec. Craft Time (Mini-CraftBot)][15 Sec. Craft Time]")
Button = ("1 Scrap Metal and 1 Circut Board for 1 Button [25 Sec. Craft Time (Mini-CraftBot)][15 Sec. Craft Time]")
Radio = ("5 Metal 1, 2 Battery, 4 Circut Board, and 1 Glue for 1 Radio [45 Sec. Craft Time]")
Horn = ("1 Metal, 1 Circut Board, 1 Glue for 1 Horn [45 Sec. Craft Time]")
LogicGate = ("1 Metal, 1 Circut Board, 1 Glue for 1 Logic Gate [20 Sec. Craft Time]")
Timer = ("2 Metal, 2 Circut Board, 1 Glue for 1 Timer [45 Sec. Craft Time]")
SmallExplosive = ("10 Gas, 6 Glow, and 5 Paint Ammo for 1 Small Explosive Canister [20 Sec. Craft Time]")
LargeExplosive = ("20 Gas, 8 Glow, and 10 Paint Ammo for 1 Large Explosive Canister [20 Sec. Craft]")
WaterCannon = ("10 Metal 2, 10 Bees Wax, and 2 Component Kit for 1 Water Cannon [1:30 Craft Time]")
Headlight = ("1 Metal 1, 1 Glass, 2 Circut Board, and 1 Glue for 1 Headlight [25 Sec. Craft Time]")
#Consumable
Gasoline = ("5 Crude Oil for 5 Gasoline [10 Sec. Craft Time]")
Battery = ("10 Scrap Metal, 5 Glow, and 5 Chemical for 5 Battery")
Water = ("1 Bucket of Water for 1 Water and 1 Empty Bucket [5 Sec. Craft Time]")
PaintAmmo = ("5 Pigment Flower for 5 Paint Ammo [15 Sec. Craft Time]")
Chemical = ("1 Bucket of Chemical for 1 Chemicals and 1 Empty Bucket [5 Sec. Craft Time]")
Fertilizer = ("10 Tomato Seeds, 10 Carrot Seeds, and 10 Redbeetfor 5 Fertilizer [10 Sec. Craft Time]")
Glowstick = ("4 Chemical and 4 Glow for 4 Glow Stick [20 Sec. Craft Time]")
#Tools
ConnectTool = ("10 Scrap Metal and 2 Circut Board for 1 Connect Tool [35 Sec. Craft Time]")
WeldTool = ("20 Metal 2, 5 Circut Board, and 5 Component Kit for 1 Weld Tool [35 Sec. Craft Time]")
PaintTool = ("10 Metal 1, 5 Glass, and 3 Component Kits for 1 Paint Tool [35 Sec. Craft Time]")
#Selection Variables
choice = 0
category = 0 #differs between Blocks, Tools, Interactive Parts, Parts, and Consumables
craft = 0 #Shows that the program is ready to end the loop for crafting
bulk = 0 #shows that the item is bulk craftable.
#Empty Resource Variables #for Use with Bulk Crafting
singlecraft = 0 # how much the recipe will grant after 1 craft
bulkcraft = 0 # how many the user wants to craft
crafttime = 0 # how long it takes to craft

#Everything Below is used to show the number of resources to craft the items.
Ember = 0
WaterEmpty = 0
Metal1Empty = 0
Metal2Empty = 0
Metal3Empty = 0
Wood1Empty = 0
Wood2Empty = 0
Wood3Empty = 0
Concrete1Empty = 0
Concrete2Empty = 0
Concrete3Empty = 0
ComponentKit = 0
CircutBoard = 0
ChemicalEmpty = 0
ScrapMetal = 0
ScrapWood = 0
ScrapStone = 0
Glow = 0
GlassEmpty = 0
SeedsT = 0
SeedsC = 0
SeedsR = 0
Glue = 0
Cotton = 0
SandEmpty = 0
WocSteak = 0
PaintAmmoEmpty = 0
BeesWax = 0
PigmentFlower = 0
Gas = 0
CrudeOil = 0
BucketofChemical = 0
BucketofWater = 0
RadioEmpty = 0
NetBlockEmpty = 0
Carrot = 0


while category == 0:
	choice = input("Are you crafting Parts, Blocks, Tools, Consumables, or Interactive Parts?\n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n ")
	if choice == "Parts":
		category = choice
		loading()
		print ("Here is the list of Craftable Parts: \n")
		print ("Wheel \nBigWheel \nI-BeamShort \nI-BeamLong \nI-BeamCorner \nI-BeamHolder \nI-BeamEnd \nSmallRectangleWindow \nSquareWindow \nLargeRectangleWindow \nLargeWindshield \nSmallWindShield \nAirConditioner \nPipeShort \nPipeLong \nPipeCorner \nPipeJoin \nValve \nSmallPipeShort \nSmallPipeLong \nSmallPipeBend \nSmallPipeTee \nSmallPipeCorner \nSmallPipe4Way \nSmallPipe4WayTee \nSmallPipe5Way \nSmallPipe6Way \nToiletPaper \nSink \nMug \nMannequinBoot \nMannequinHand  \nDuckStatue \nTrafficCone \nScrapWheel \nBucket \nSoilBag")
	elif choice == "Blocks":
		category = choice
		loading()
		print ("Here is the list of Craftable Blocks: \n")
		print ("Concrete1 \nWood1 \nMetal1 \nBarrierBlock \nTileBlock \nBrickBlock \nGlassBlock \nGlassTile \nPathLight \nCardBoard \nWood2 \nWood3 \nMetal2 \nMetal3 \nConcrete2 \nConcrete3 \nExtrudedMetal \nBubblePlastic \nCarpet \nNet \nSolidNet \nPunchedSteel \nRestroomBlock \nDiamondPlate \nSand \nArmoredGlass")
	elif choice == "Tools":
		category = choice
		loading()
		print ("Here is the list of Craftable Tools: \n")
		print ("Connect Tool \nWeld Tool \nPaint Tool")
	elif choice == "Consumables":
		category = choice
		loading()
		print ("Here is the list of Craftable Consumables: \n")
		print ("Gasoline \nBattery \nWater \nPaintAmmo \nChemical \nFertilizer \nGlowstick")
	elif choice == "Interactive Parts":
		category = choice
		loading()
		print ("Here is the list of Craftable Interactive Parts: \n")
		print ("Beacon \nSportSuspension \nOffRoadSuspension \nDriverSeat \nSeat \nDriverSaddle \nSaddle \nGasEngine \nElectricEngine \nThruster \nController \nSensor \nPiston \nGasContainer \nWaterContainer \nBatteryContainer \nSawBlade \nDrill \nVacuumPump \nVacuumPipe \nVacuumPipeCorner \nLargeChest \nRefineBot \nResourceCollector \nCraftBot \nScrapGasEngine \nScrapDriverSeat \nScrapSeat \nRespawnBed \nChest \nFridge \nChemicalContainer \nBearing \nToilet \nSwitch \nButton \nRadio \nHorn \nLogicGate \nTimer \nSmallExplosive \nLargeExplosive \nWaterCannon \nHeadlight")
choice = 0



while craft == 0:
#	input_str = "Please choose a ",category," to craft"
	input_str = "\n \nPlease choose a " + category + " to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
	choice = input(input_str)
	if category == "Parts":
		if choice == "Wheel":
			print (Wheel)
			Wood1Empty = 15
			Metal1Empty = 5
			BeesWax = 6
			crafttime = 20
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "BigWheel":
			print (BigWheel)
			Wood1Empty = 40
			Metal1Empty = 10
			BeesWax = 8
			craft = True
			bulk = True
			crafttime = 30
			singlecraft = 1
		elif choice == "IBeamShort":
			print (IBeamShort)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "IBeamLong":
			print (IBeamLong)
			Metal1Empty = 3
			craft = True
			bulk = True
			singlecraft = 1
			
			singlecraft = 1
		elif choice == "IBeamCorner":
			print (IBeamCorner)
			Metal1Empty = 1
			craft = True
			bulk = True
			
			singlecraft = 1
		elif choice == "IBeamHolder":
			print (IBeamHolder)
			Metal1Empty = 1
			
			craft = True
			bulk = True
			
			singlecraft = 1
		elif choice == "IBeamEnd":
			print (IBeamEnd)
			Metal1Empty = 1
			
			craft = True
			bulk = True
			
			singlecraft = 1
		elif choice == "SmallRectangleWindow":
			print (SmallRectangleWindow)
			GlassEmpty = 5
			Metal1Empty = 5
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SquareWindow":
			print (SquareWindow)
			GlassEmpty = 10
			Metal1Empty = 10
			craft = True
			bulk = True
		elif choice == "LargeRectangleWindow":
			print (LargeRectangleWindow)
			GlassEmpty = 15
			Metal1Empty = 10
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "LargeWindshield":
			print (LargeWindshield)
			GlassEmpty = 20
			Metal1Empty = 10
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallWindshield":
			print (SmallWindShield)
			GlassEmpty = 10
			Metal1Empty = 5
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "AirConditioner":
			print (AirConditioner)
			Metal1Empty = 10
			CircutBoard = 3
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "PipeShort":
			print (PipeShort)
			Metal1Empty = 1
			
			singlecraft = 1
		elif choice == "PipeLong":
			print (PipeLong)
			Metal1Empty = 3
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "PipeCorner":
			print (PipeCorner)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "PipeJoin":
			print (PipeJoin)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Valve":
			print (Valve)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipeShort":
			print (SmallPipeShort)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipeLong":
			print (SmallPipeLong)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipeBend":
			print (SmallPipeBend)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipeTee":
			print (SmallPipeTee)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipeCorner":
			print (SmallPipeCorner)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipe4Way":
			print (SmallPipe4Way)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipe4WayTee":
			print (SmallPipe4WayTee)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipe5Way":
			print (SmallPipe5Way)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SmallPipe6Way":
			print (SmallPipe6Way)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
			
		elif choice == "ToiletPaper":
			print (ToiletPaper)
			ScrapWood = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Sink":
			print (Sink)
			Metal1Empty = 5
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Mug":
			print (Mug)
			Metal1Empty = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "MannequinBoot":
			print (MannequinBoot)
			WocSteak = 1
			Wood1Empty = 2
			PaintAmmoEmpty = 1
			BeesWax = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "MannequinHand":
			print (MannequinHand)
			Wood1Empty = 2
			PaintAmmoEmpty = 1
			BeesWax = 3
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "DuckStatue":
			print (DuckStatue)
			Wood1Empty = 1
			PaintAmmoEmpty = 1
			BeesWax = 3
			Glue = 1
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "TrafficCone":
			print (TrafficCone)
			Metal1Empty = 10
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ScrapWheel":
			print (ScrapWheel)
			ScrapWood = 20
			ScrapMetal = 5
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Bucket":
			print (Bucket)
			ScrapMetal = 5
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SoilBag":
			print (SoilBag)
			ScrapWood = 10
			SandEmpty = 10
			Carrot = 2
			craft = True
			bulk = True
			singlecraft = 1
		
	elif category == "Blocks":
		if choice == "Concrete1":
			print (Concrete1)
			ScrapStone = 5
			WaterEmpty = 5
			ChemicalEmpty = 5
			crafttime = 10
			
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "Wood1":
			print (Wood1)
			ScrapWood = 15
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "Metal1":
			print (Metal1)
			ScrapMetal = 15
			crafttime = 10
			singlecraft = 10
			
			
			craft = True
			bulk = True
		elif choice == "BarrierBlock":
			print (BarrierBlock)
			Wood1Empty = 10
			PaintAmmoEmpty = 1
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "GlassBlock":
			print (GlassBlock)
			SandEmpty = 10
			Ember = 1
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "GlassTile":
			print (GlassTile)
			SandEmpty = 10
			Ember = 1
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "BrickBlock":
			print (BrickBlock)
			ScrapStone = 10
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = False
		elif choice == "PathLight":
			print (PathLight)
			Metal1Empty = 10
			CircutBoard = 1
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "CardBoard":
			print (CardBoard)
			ScrapWood = 5
			
			singlecraft = 10
			crafttime = 5
			
			craft = True
			bulk = True
		elif choice == "Wood2":
			print (Wood2)
			Wood1Empty = 15
			Metal1Empty = 1
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Wood3":
			print (Wood3)
			Wood2Empty = 15
			Metal2Empty = 1
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Metal2":
			print (Metal2)
			Metal1Empty = 15
			Ember = 1
			WaterEmpty = 2
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "Metal3":
			print (Metal3)
			Metal2Empty = 20
			Ember = 2
			WaterEmpty = 4
			
			crafttime = 10
			singlecraft = 10
			craft = True
			bulk = True
		elif choice == "Concrete2":
			print (Concrete2)
			Concrete1Empty = 15
			Metal1Empty = 2
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "Concrete3":
			print (Concrete3)
			Concrete2Empty = 15
			Metal2Empty = 2
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "ExtrudedMetal":
			print (ExtrudedMetal)
			Metal1Empty = 5
			
			crafttime = 10
			singlecraft = 10
			
			craft = True
			bulk = True
		elif choice == "BubblePlastic":
			print (BubblePlastic)
			CrudeOil = 5
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Carpet":
			print (Carpet)
			Cotton = 5
			PaintAmmoEmpty = 1
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Net":
			print (Net)
			Metal1Empty = 2
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "SolidNet":
			print (SolidNet)
			Metal2Empty = 5
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "PunchedSteel":
			print (PunchedSteel)
			craft = True
			Metal1Empty = 5
			
			singlecraft = 10
			crafttime = 10
			
			bulk = True
		elif choice == "RestroomBlock":
			print (RestroomBlock)
			craft = True
			ScrapStone = 10
			BeesWax = 1
			
			singlecraft = 10
			crafttime = 10
			
			bulk = True
		elif choice == "DiamondPlate":
			print (DiamondPlate)
			craft = True
			Metal1Empty = 10
			
			singlecraft = 10
			crafttime = 10
			
			bulk = True
		elif choice == "Sand":
			print (Sand)
			ScrapStone = 5
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "ArmoredGlass":
			print (ArmoredGlass)
			GlassEmpty = 10
			NetBlockEmpty = 2
			Ember = 1
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "TileBlock":
			print (TileBlock)
			ScrapStone = 10
			PaintAmmoEmpty = 1
			
			singlecraft = 10
			crafttime = 10
			
			craft = True
			bulk = True

	elif category == "Tools":
		if choice == "Connect Tool":
			print (ConnectTool)
			ScrapMetal = 10
			CircutBoard = 1
			
			singlecraft = 1
			crafttime = 35
			
			craft = True
			bulk = False
			
		elif choice == "Weld Tool":
			print (WeldTool)
			Metal2Empty = 20
			CircutBoard  = 5
			ComponentKit = 5
			crafttime = 35
			
			singlecraft = 1
			
			craft = True
			bulk = False
		elif choice == "Paint Tool":
			print (PaintTool)
			Metal1Empty = 10
			GlassEmpty = 5
			ComponentKit = 3
			crafttime = 35
			
			singlecraft = 1
			
			craft = True
			bulk = False
	elif category == "Consumables":
		if choice == "Gasoline":
			print (Gasoline)
			CrudeOil = 5
			crafttime = 10
			
			singlecraft = 5
			craft = True
			bulk = True
			
		elif choice == "Battery":
			print (Battery)
			ScrapMetal = 10
			Glow = 5
			ChemicalEmpty = 5
			
			singlecraft = 5
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Water":
			print (Water)
			BucketofWater = 1
			
			singlecraft = 1
			crafttime = 5
			craft = True
			
			bulk = True
		elif choice == "Paint Ammo":
			print (PaintAmmo)
			PigmentFlower = 5
			
			singlecraft = 5
			crafttime = 15
			
			craft = True
			bulk = True
		elif choice == "Chemical":
			print (Chemical)
			BucketofChemical = 1
			
			singlecraft = 1
			crafttime = 5
			
			craft = True
			bulk = True
		elif choice == "Fertilizer":
			print (Fertilizer)
			SeedsT = 10
			SeedsR = 10
			SeedsC = 10
			
			singlecraft = 5
			crafttime = 10
			
			craft = True
			bulk = True
		elif choice == "Glowstick":
			print (Glowstick)
			Glow = 4
			ChemicalEmpty = 4
			
			singlecraft = 4
			crafttime = 20
			
			craft = True
			bulk = True
	elif category == "Interactive Parts":
		if choice == "Beacon":
			print (Beacon)
			Metal2Empty = 10
			RadioEmpty = 1
			CircutBoard = 10
			crafttime = 45
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "SportSuspension":
			print (SportSuspension)
			Metal2Empty = 5
			CrudeOil = 2
			crafttime = 45
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "OffRoadSuspension":
			print (OffRoadSuspension)
			Metal2Empty = 10
			CrudeOil = 2
			crafttime = 45
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "DriverSeat":
			print (DriverSeat)
			Cotton = 10
			Metal1Empty = 5
			CircutBoard = 3
			ComponentKit = 1
			crafttime = 60
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Seat":
			print (Seat)
			Cotton = 10
			Metal1Empty = 5
			CircutBoard = 2
			crafttime = 40
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "DriverSaddle":
			print (DriverSaddle)
			Cotton = 5
			Metal1Empty = 5
			CircutBoard = 3
			ComponentKit = 1
			crafttime = 60
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Saddle":
			print (Saddle)
			Cotton = 5
			Metal1Empty = 5
			CircutBoard = 2
			crafttime = 40
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "GasEngine":
			print (GasEngine)
			Metal2Empty = 20
			CrudeOil = 5
			CircutBoard = 5
			ComponentKit = 3
			crafttime = 90
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ElectricEngine":
			print (ElectricEngine)
			Metal2Empty = 20
			BatteryEmpty = 5
			CircutBoard = 10
			ComponentKit = 5
			crafttime = 90
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Thruster":
			print (Thruster)
			Metal2Empty = 40
			ComponentKit = 10
			crafttime = 120
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Controller":
			print (Controller)
			Metal1Empty = 5
			CircutBoard = 5
			ComponentKit = 1
			Glue = 3
			crafttime = 120
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Sensor":
			print (Sensor)
			GlassEmpty = 1
			Metal1Empty = 1
			CircutBoard = 2
			Glue = 2
			crafttime = 30
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Piston":
			print (Piston)
			Metal2Empty = 10
			CrudeOil = 2
			CircutBoard = 2
			ComponentKit = 1 
			crafttime = 40
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "GasContainer":
			print (GasContainer)
			Metal1Empty = 20
			CircutBoard = 5
			PaintAmmoEmpty = 15
			Glue = 2
			crafttime = 40
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "WaterContainer":
			print (WaterContainer)
			Metal1Empty = 10
			BeesWax = 10
			CircutBoard = 5
			Glue = 2
			craft = True
			bulk = True
			crafttime = 60
			singlecraft = 1
		elif choice == "BatteryContainer":
			print (BatteryContainer)
			Metal1Empty = 20
			CircutBoard = 5
			PaintAmmoEmpty = 15
			Glue = 2
			craft = True
			bulk = True
			crafttime = 40
			singlecraft = 1
		elif choice == "SawBlade":
			print (SawBlade)
			Metal2Empty = 10
			Metal1Empty = 20
			crafttime = 90
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "Drill":
			print (Drill)
			Metal2Empty = 20
			Metal1Empty = 30
			crafttime = 90
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "VacuumPump":
			print (VacuumPump)
			Metal2Empty = 10
			BeesWax = 5
			CircutBoard = 5
			crafttime = 90
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "VacuumPipe":
			print (VacuumPipe)
			GlassEmpty = 10
			Metal2Empty = 5
			CircutBoard = 2
			crafttime = 15
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "VacuumPipeCorner":
			print (VacuumPipeCorner)
			GlassEmpty = 10
			craft = True
			bulk = True
			Metal2Empty = 5
			CircutBoard = 2
			crafttime = 15
			singlecraft = 1
		elif choice == "LargeChest":
			print (LargeChest)
			Metal1Empty = 60
			CircutBoard = 5
			ComponentKit = 3
			Glue = 5
			craft = True
			bulk = True
			crafttime = 90
			singlecraft = 1
		elif choice == "RefineBot":
			print (RefineBot)
			Metal1Empty = 60
			CircutBoard = 5
			ComponentKit = 5
			crafttime = 0
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ResourceCollector":
			print (ResourceCollector)
			Metal1Empty = 30
			crafttime = 0
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "CraftBot":
			print (CraftBot)
			Metal1Empty = 90
			CircutBoard = 10
			ComponentKit = 10
			crafttime = 0
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ScrapGasEngine":
			print (ScrapGasEngine)
			ScrapMetal = 30
			ScrapWood = 20
			CircutBoard = 3
			crafttime = 35
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ScrapDriverSeat":
			print (ScrapDriverSeat)
			ScrapMetal = 10
			ScrapWood = 100
			CircutBoard = 1
			crafttime = 35
			craft = True
			bulk = True
			singlecraft = 1
		elif choice == "ScrapSeat":
			print (ScrapSeat)
			ScrapWood = 50
			CircutBoard = 1
			crafttime = 35
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "RespawnBed":
			print (RespawnBed)
			Wood1Empty = 50
			Cotton = 20
			craft = True
			bulk = True
			PaintAmmoEmpty = 15
			crafttime = 60
			singlecraft = 1
		elif choice == "Chest":
			print (Chest)
			Metal1Empty = 40
			Glue = 2
			craft = True
			bulk = True
			crafttime = 60
			singlecraft = 1
		elif choice == "Fridge":
			print (Fridge)
			Metal1Empty = 10
			ChemicalEmpty = 2
			CircutBoard = 1
			craft = True
			bulk = True
			Glue = 2
			crafttime = 60
			singlecraft = 1
		elif choice == "ChemicalContainer":
			print (ChemicalContainer)
			Metal2Empty = 10
			GlassEmpty = 20
			craft = True
			bulk = True
			CircutBoard = 1
			Glue = 2
			crafttime = 60
			singlecraft = 1
		elif choice == "Bearing":
			print (Bearing)
			ScrapMetal = 5
			crafttime = 15
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "Toilet":
			print (Toilet)
			Metal1Empty = 5
			Wood1Empty = 5
			crafttime = 5
			singlecraft = 1 
			craft = True
			bulk = True
		elif choice == "Switch":
			print (Switch)
			ScrapMetal = 1
			CircutBoard = 1
			craftbottime = 15
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "Button":
			print (Button)
			ScrapMetal = 1
			CircutBoard = 1
			craftbottime = 15
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "Radio":
			print (Radio)
			Metal1Empty = 5
			BatteryEmpty =2
			CircutBoard = 4
			Glue = 1
			craft = True
			bulk = True
			crafttime = 45
			singlecraft = 1
		elif choice == "Horn":
			print (Horn)
			Metal1Empty = 1
			CircutBoard = 1
			Glue = 1
			craft = True
			bulk = True
			crafttime = 45
			singlecraft = 1
		elif choice == "LogicGate":
			print (LogicGate)
			Metal1Empty = 1
			CircutBoard = 1
			Glue = 1
			craft = True
			bulk = True
			crafttime = 20
			singlecraft = 1
		elif choice == "Timer":
			print (Timer)
			Metal1Empty = 2
			CircutBoard = 2
			Glue = 1
			craft = True
			bulk = True
			crafttime = 45
			singlecraft = 1
		elif choice == "SmallExplosive":
			print (SmallExplosive)
			GasolineEmpty = 10
			Glow = 6
			craft = True
			bulk = True
			PaintAmmoEmpty = 5
			crafttime = 20
			singlecraft = 1
		elif choice == "LargeExplosive":
			print (LargeExplosive)
			GasolineEmpty = 20
			Glow = 8
			craft = True
			bulk = True
			PaintAmmoEmpty = 10
			crafttime = 20
			singlecraft = 1
		elif choice == "WaterCannon":
			print (WaterCannon)
			Metal2Empty = 10
			BeesWax = 10
			ComponentKit = 2
			crafttime = 90
			singlecraft = 1
			craft = True
			bulk = True
		elif choice == "Headlight":
			print (Headlight)
			Metal1Empty = 1
			GlassEmpty = 1
			CircutBoard = 1
			Glue = 1
			craft = True
			bulk = True
			crafttime = 25
			singlecraft = 1
	
	
	if bulk == True:
		time.sleep(5)
		more=input('Do you want to craft in bulk? (True or False)(Same Capitalization): \n')
		if more == 'False':
			exit
		elif more == 'True':
			
			loading()
			bulkcraft = int(input("How Much " + choice + " Do You Need: \n"))
			clearscreen()
			if category == "Blocks":
				if choice == 'Concrete1':
					ScrapStone = (bulkcraft * ScrapStone) / singlecraft
					WaterEmpty = (bulkcraft * WaterEmpty) / singlecraft
					ChemicalEmpty = (bulkcraft * ChemicalEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ("Concrete 1 from:")
					print (ChemicalEmpty)
					print ("Chemical,")
					print (WaterEmpty)
					print("Water, and")
					print (ScrapStone)
					print ("Scrap Stone")
					print (crafttime)
					print ("Seconds")
				elif choice == 'Wood1':
					ScrapWood = (bulkcraft * ScrapWood) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ("Wood 1 from:")
					print (ScrapWood)
					print ("Scrap Wood")
					print (crafttime)
					print ("Seconds") 
				elif choice == 'Metal1':
					ScrapMetal = (bulkcraft * ScrapMetal) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ("Metal 1 from:")
					print (ScrapMetal)
					print ("Scrap Metal")
					print (crafttime)
					print ("Seconds")
				elif choice == 'BarrierBlock':
					Wood1Empty = (bulkcraft * Wood1Empty) / singlecraft
					PaintAmmoEmpty = (bulkcraft * PaintAmmoEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ("Barrier Block from:")
					print (Wood1Empty)
					print ("Wood 1 and")
					print (PaintAmmoEmpty)
					print ("Paint Ammo")
					print (crafttime)
					print ("Seconds") 
				elif choice == 'GlassBlock':
					SandEmpty = (bulkcraft * SandEmpty) / singlecraft
					Ember = (bulkcraft * Ember) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					print (Totalcraft)
					print ("Glass Block from:")
					print (SandEmpty)
					print ("Sand and")
					print (Ember)
					print ("Ember")
					print (crafttime)
					print ("Seconds") 
				elif choice == 'GlassTile':
					SandEmpty = (bulkcraft * SandEmpty) / singlecraft
					Ember = (bulkcraft * Ember) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					print (Totalcraft)
					print ("Glass Tile from:")
					print (SandEmpty)
					print ("Sand and")
					print (Ember)
					print ("Ember")
					print (crafttime)
					print ("Seconds") 
				elif choice == 'TileBlock':
					ScrapStone = (bulkcraft * ScrapStone) / singlecraft
					PaintAmmoEmpty = (bulkcraft * PaintAmmoEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Tile Block from')
					print (ScrapStone)
					print ("Scrap Stone and")
					print (PaintAmmoEmpty)
					print ("Paint Ammo")
					print (crafttime)
					print ("seconds")
					
				elif choice == 'BrickBlock':
					ScrapStone = (bulkcraft * singlecraft) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Brick Block from')
					print (ScrapStone)
					print ('Scrap Stone')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'PathLight':
					Metal1Empty = (bulkcraft * Metal1Empty) / singlecraft
					CircutBoard = (bulkcraft * CircutBoard) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Path Light from')
					print (Metal1Empty)
					print ('Metal 1 and')
					print (CircutBoard)
					print ('Circut Boards')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Cardboard':
					ScrapWood = (bulkcraft * ScrapWood) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Cardboard from')
					print (ScrapWood)
					print ('Scrap Wood')
					print (crafttime)
					print ('seconds')
				
				elif choice == 'Wood2':
					Wood1Empty = (bulkcraft * Wood1Empty) / singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Wood 2 from')
					print (Wood1Empty)
					print ('Wood 1 and ')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Wood3':
					Wood2Empty = (bulkcraft * Wood2Empty) / singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Wood3 from')
					print (Wood2Empty)
					print ('Wood 2 and')
					print (Metal2Empty)
					print ('Metal 2')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Metal2':
					Metal1Empty = (bulkcraft * Metal1Empty) / singlecraft
					Ember = (bulkcraft * Ember) / singlecraft
					WaterEmpty = (bulkcraft * WaterEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Metal 2 from')
					print (Metal1Empty)
					print ('Metal 1,')
					print (Ember)
					print ('Ember, and')
					print (WaterEmpty)
					print ('Water')
					print (crafttime)
					print ('seconds')
				elif choice == 'Metal3':
					Metal2Empty  = (bulkcraft * Metal2Empty) / singlecraft
					Ember = (bulkcraft * Ember) / singlecraft
					WaterEmpty = (bulkcraft * WaterEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Metal 3 from')
					print (Metal1Empty)
					print ('Metal 2,')
					print (Ember)
					print ('Ember, and')
					print (WaterEmpty)
					print ('Water')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Concrete2':
					Concrete1Empty = (bulkcraft * Concrete1Empty) / singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Concrete 2 from')
					print (Concrete1Empty)
					print ('Concrete 1')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Concrete3':
					Concrete2Empty = (bulkcraft * Concrete2Empty) / singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Concrete 3 from')
					print (Concrete2Empty)
					print ('Concrete 2')
					print (Metal2Empty)
					print ('Metal 2')
					print (crafttime)
					print ('seconds')
				
				elif choice == 'ExtrudedMetal':
					Metal2Empty =  (bulkcraft * Metal2Empty ) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('ExtrudedMetal from')
					print (Metal2Empty)
					print ('Metal 2')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'BubblePlastic':
					CrudeOil =  (bulkcraft * CrudeOil ) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Bubble Plastic from')
					print (CrudeOil)
					print ('Crude Oil')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Carpet':
					Cotton =  (bulkcraft * Cotton) / singlecraft
					PaintAmmoEmpty =  (bulkcraft * PaintAmmoEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Carpet from')
					print (Cotton)
					print ('Cotton and')
					print (PaintAmmoEmpty)
					print ('Paint Ammo')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Net':
					Metal1Empty =  (bulkcraft * Metal1Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Net from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SolidNet':
					Metal2Empty =  (bulkcraft * Metal2Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Solid Net from')
					print (Metal2Empty)
					print ('Metal 2')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'PunchedSteel':
					Metal1Empty =  (bulkcraft * Metal1Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Punched Steel from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'RestroomBlock':
					ScrapStone =  (bulkcraft * ScrapStone) / singlecraft
					BeesWax = (bulkcraft * BeesWax) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Restroom Block from')
					print (ScrapStone)
					print ('Scrap Stone and')
					print (BeesWax)
					print ("Bee's Wax")
					print (crafttime)
					print ('seconds')
					
				elif choice == 'DiamondPlate':
					Metal1Empty =  (bulkcraft * Metal1Empty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Sand':
					ScrapStone =  (bulkcraft * ScrapStone) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Scrap from')
					print (ScrapStone)
					print ('Scrap Stone')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'ArmoredGlass':
					GlassEmpty =  (bulkcraft * GlassEmpty) / singlecraft
					NetBlockEmpty =  (bulkcraft * NetBlockEmpty) / singlecraft
					Ember  =  (bulkcraft * Ember) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Armored Glass from')
					print (GlassEmpty)
					print ('Glass,')
					print (NetBlockEmpty)
					print ('Net Block, and')
					print (Ember)
					print ('Ember')
					print (crafttime)
					print ('seconds')
					
			elif category == 'Consumables':
				if choice == 'Gasoline':
					CrudeOil =  (bulkcraft * CrudeOil) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Gasoline from')
					print (CrudeOil)
					print ('Crude Oil')
					print (crafttime)
					print ('seconds') 
				elif choice == 'Battery':
					ScrapMetal = (bulkcraft * ScrapMetal) / singlecraft
					Glow = (bulkcraft * Glow) / singlecraft
					ChemicalEmpty = (bulkcraft * ChemicalEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Battery from')
					print (ScrapMetal)
					print ('Scrap Metal,')
					print (Glow)
					print ('Glow, and')
					print (ChemicalEmpty)
					print ('Chemical')
					print (crafttime)
					print ('seconds')
				elif choice == 'Water':
					BucketofWater = (bulkcraft * BucketofWater) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Water from')
					print (BucketofWater)
					print ('Bucket Of Water')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Chemical':
					BucketofChemical = (bulkcraft * BucketofChemical) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Chemical from')
					print (BucketofChemical)
					print ('Bucket of Chemical')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Fertilizer':
					SeedsC = (bulkcraft * SeedsC) / singlecraft
					SeedsR = (bulkcraft * SeedsR) / singlecraft
					SeedsT = (bulkcraft * SeedsT) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Fertilizer from')
					print (SeedsC)
					print ('Carrot Seeds')
					print (SeedsR)
					print ('Redbeet Seeds')
					print (SeedsT)
					print ('Turnip Seeds')
					print (crafttime)
					print ('seconds')
				
				elif choice == 'Glowstick':
					Glow = (bulkcraft * Glow) / singlecraft
					ChemicalEmpty = (bulkcraft * ChemicalEmpty) / singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Glowstick from')
					print (Glow)
					print ('Glow and')
					print (ChemicalEmpty)
					print ('Chemical')
					print (crafttime)
					print ('seconds')
		
			elif category == 'Interactive Parts':
				if choice == 'Beacon':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					RadioEmpty = (bulkcraft * RadioEmpty)/singlecraft
					CircutBoard = (bulkcraft * CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (RadioEmpty)
					print ('Radio')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'SportSuspension':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CrudeOil = (bulkcraft *CrudeOil)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (CrudeOil)
					print ('Crude Oil')
					print (crafttime)
					print ('seconds')
				elif choice == 'OffRoadSuspension':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CrudeOil = (bulkcraft *CrudeOil)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (CrudeOil)
					print ('Crude Oil')
					print (crafttime)
					print ('seconds')
				elif choice == 'DriverSeat':
					Cotton = (bulkcraft *Cotton)/singlecraft
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Cotton)
					print ('Cotton')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'Seat':
					Cotton = (bulkcraft *Cotton)/singlecraft
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Cotton)
					print ('Cotton')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'DriverSaddle':
					Cotton = (bulkcraft *Cotton)/singlecraft
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Cotton)
					print ('Cotton')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'Saddle':
					Cotton = (bulkcraft *Cotton)/singlecraft
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print ('Cotton')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'GasEngine':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CrudeOil = (bulkcraft *CrudeOil)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (CrudeOil)
					print ('Crude Oil')
					print (crafttime)
					print ('seconds')
				elif choice == 'ElectricEngine':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					BatteryEmpty = (bulkcraft *BatteryEmpty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (BatteryEmpty)
					print ('Battery')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'Thruster':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'Controller':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'Sensor':
					GlassEmpty = (bulkcraft *GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (GlassEmpty)
					print ('Glass')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'Piston':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CrudeOil = (bulkcraft *CrudeOil)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (CrudeOil)
					print ('Crude Oil')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'GasContainer':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					PaintAmmoEmpty = (bulkcraft *PaintAmmoEmpty)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (PaintAmmoEmpty)
					print ('Paint Ammo')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'WaterContainer':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					BeesWax = (bulkcraft *BeesWax)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (BeesWax)
					print ('Bees Wax')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'BatteryContainer':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					PaintAmmoEmpty = (bulkcraft *PaintAmmoEmpty)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (PaintAmmoEmpty)
					print ('Paint ammo')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'SawBlade':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
				elif choice == 'Drill':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2)
					print ('Metal 2')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
				elif choice == 'VacuumPump':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					BeesWax = (bulkcraft *BeesWax)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (BeesWax)
					print ('Bees Wax')
					print (CircutBoard)
					print ('Circut Board')
					
					print (crafttime)
					print ('seconds')
				elif choice == 'VacuumPipe':
					GlassEmpty = (bulkcraft *GlassEmpty)/singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (GlassEmpty)
					print ('Glass')
					print (Metal2Empty)
					print ('Metal 2')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'VacuumPipeCorner':
					GlassEmpty = (bulkcraft *GlassEmpty)/singlecraft
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (GlassEmpty)
					print ('Glass')
					print (Metal2Empty)
					print ('Metal 2')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'LargeChest':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'RefineBot':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'ResourceCollector':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
				elif choice == 'CraftBot':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'ScrapGasEngine':
					ScrapMetal = (bulkcraft *ScrapMetal)/singlecraft
					ScrapWood = (bulkcraft *ScrapWood)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (ScrapWood)
					print ('Scrap Wood')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'ScrapDriverSeat':
					ScrapMetal = (bulkcraft *ScrapMetal)/singlecraft
					ScrapWood = (bulkcraft *ScrapWood)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (ScrapWood)
					print ('Scrap Wood')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'ScrapSeat':
					ScrapWood = (bulkcraft *ScrapWood)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (ScrapWood)
					print ('Scrap Wood')
					print (CircutBoard)
					print ('')
					print (crafttime)
					print ('seconds')
				elif choice == 'RespawnBed':
					Cotton = (bulkcraft *Cotton)/singlecraft
					Wood1Empty = (bulkcraft *Wood1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Wood1Empty)
					print ('Wood 1')
					print (Cotton)
					print ('Cotton')
					print (crafttime)
					print ('seconds')
				elif choice == 'Chest':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'Fridge':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					ChemicalEmpty = (bulkcraft *ChemicalEmpty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (ChemicalEmpty)
					print ('Chemical')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'ChemicalContainer':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					GlassEmpty = (bulkcraft *GlassEmpty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					#print ()
					#print ('')
					print (crafttime)
					print ('seconds')
				elif choice == 'Bearing':
					ScrapMetal = (bulkcraft *ScrapMetal)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (crafttime)
					print ('seconds')
				elif choice == 'Toilet':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					Wood1Empty = (bulkcraft *Wood1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (Wood1Empty)
					print ('Wood 1')
					print (crafttime)
					print ('seconds')
				elif choice == 'Switch':
					ScrapMetal = (bulkcraft *ScrapMetal)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'Button':
					ScrapMetal = (bulkcraft *ScrapMetal)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print ('Scrap Metal')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				elif choice == 'Radio':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					BatteryEmpty = (bulkcraft *BatteryEmpty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (BatteryEmpty)
					print ('Battery')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'Horn':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'LogicGate':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					#print ()
					#print ('')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'Timer':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					Glue = (bulkcraft *Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					#print ()
					#print ('')
					print (Metal1Empty)
					print ('Metal 1')
					print (CircutBoard)
					print ('Circut Board')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
				elif choice == 'SmallExplosive':
					GasolineEmpty = (bulkcraft *GasolineEmpty)/singlecraft
					Glow = (bulkcraft *Glow)/singlecraft
					PaintAmmoEmpty = (bulkcraft *PaintAmmoEmpty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (GasolineEmpty)
					print ('Gasoline')
					print (Glow)
					print ('Glow')
					print (PaintAmmoEmpty)
					print ('Paint Ammo')
					print (crafttime)
					print ('seconds')
				elif choice == 'LargeExplosive':
					GasolineEmpty = (bulkcraft *GasolineEmpty)/singlecraft
					Glow = (bulkcraft *Glow)/singlecraft
					PaintAmmoEmpty = (bulkcraft *PaintAmmoEmpty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					
					print (GasolineEmpty)
					print ('Gasoline')
					print (Glow)
					print ('Glow')
					print (PaintAmmoEmpty)
					print ('Paint Ammo')
					print (crafttime)
					print ('seconds')
				elif choice == 'WaterCannon':
					Metal2Empty = (bulkcraft * Metal2Empty)/singlecraft
					BeesWax = (bulkcraft *BeesWax)/singlecraft
					ComponentKit = (bulkcraft *ComponentKit)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal2Empty)
					print ('Metal 2')
					print (BeesWax)
					print ('Bees Wax')
					print (ComponentKit)
					print ('Component Kit')
					print (crafttime)
					print ('seconds')
				elif choice == 'Headlight':
					Metal1Empty = (bulkcraft *Metal1Empty)/singlecraft
					GlassEmpty = (bulkcraft *GlassEmpty)/singlecraft
					CircutBoard = (bulkcraft *CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (GlassEmpty)
					print ('Glass')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
			
			
			elif category == 'Parts':
				if choice == 'Wheel':
					Wood1Empty = (bulkcraft * Wood1Empty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					BeesWax = (bulkcraft * BeesWax)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Wheel from')
					print (Wood1Empty)
					print ('Wood 1')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Big Wheel':
					Wood1Empty = (bulkcraft * Wood1Empty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					BeesWax = (bulkcraft * BeesWax)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Big Wheel from')
					print (Wood1Empty)
					print ('Wood 1')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'IBeamShort':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('IBeamShort from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'IBeamLong':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('IBeamLong from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'IBeamCorner':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('IBeamCorner from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'IBeamHolder':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('IBeamHolder from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'IBeamEnd':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('IBeamEnd from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallRectangleWindow':
					GlassEmpty = (bulkcraft * GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Small Rectangle Window from')
					print (GlassEmpty)
					print ('Glass and')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SquareWindow':
					GlassEmpty = (bulkcraft * GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Square Window from')
					print (GlassEmpty)
					print ('Glass and')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'LargeRectangleWindow':
					GlassEmpty = (bulkcraft * GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Large Rectangle Window from')
					print (GlassEmpty)
					print ('Glass and')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Large Windshield':
					GlassEmpty = (bulkcraft * GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Large Windshield from')
					print (GlassEmpty)
					print ('Glass and')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Small Windshield':
					GlassEmpty = (bulkcraft * GlassEmpty)/singlecraft
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Small Windshield from')
					print (GlassEmpty)
					print ('Glass and')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'AirConditioner':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					CircutBoard = (bulkcraft * CircutBoard)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1 and')
					print (CircutBoard)
					print ('Circut Board')
					print (crafttime)
					print ('seconds')
				
				elif choice == 'PipeShort':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Pipe_ from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'PipeTall':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Pipe_ from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'PipeCorner':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Pipe_ from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'PipeJoin':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Pipe_ from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Valve':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Valve from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipeShort':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipeShort from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipeLong':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipeLomg from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipeBend':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipeBend from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipeTee':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipeTee from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipeCorner':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipeCorner from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipe4Way':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipe4Way from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipe4WayTee':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipe4WayTee from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipe5Way':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipe6Way from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SmallPipe6Way':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SmallPipe6Way from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'ToiletPaper':
					ScrapWood = (bulkcraft * ScrapWood)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('ToiletPaper from')
					print (ScrapWood)
					print ('Scrap Wood')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Sink':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Sink from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Mug':
					Metal1Empty= (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Mug from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'MannequinBoot':
					WocSteak = (bulkcraft * WocSteak)/singlecraft
					Wood1Empty = (bulkcraft * Wood1Empty)/singlecraft
					PaintAmmoEmpty = (bulkcraft * PaintAmmoEmpty)/singlecraft
					BeesWax = (bulkcraft * BeesWax)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Mannequin Boot from')
					print (WocSteak)
					print ('Woc Steak')
					print (Wood1Empty)
					print ('Wood 1')
					print (PaintAmmoEmpty)
					print ('Paint Ammo and')
					print (BeesWax)
					print ('Bees Wax')
					print (crafttime)
					print ('seconds')
				elif choice == 'MannequinHand':
					Wood1Empty = (bulkcraft * Wood1Empty)/singlecraft
					PaintAmmoEmpty = (bulkcraft * PaintAmmoEmpty)/singlecraft
					BeesWax = (bulkcraft * BeesWax)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Mannequin Hand from')
					print (Wood1Empty)
					print ('Wood 1')
					print (PaintAmmoEmpty)
					print ('Paint Ammo and')
					print (BeesWax)
					print ('Bees Wax')
					
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Duck Statue':
					Wood1Empty = (bulkcraft * Wood1Empty)/singlecraft
					PaintAmmoEmpty = (bulkcraft * PaintAmmoEmpty)/singlecraft
					BeesWax = (bulkcraft * BeesWax)/singlecraft
					Glue = (bulkcraft * Glue)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Duck Statue from')
					print (Wood1Empty)
					print ('Wood 1')
					print (PaintAmmoEmpty)
					print ('Paint Ammo')
					print (BeesWax)
					print ('Bees Wax and')
					print (Glue)
					print ('Glue')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'TrafficCone':
					Metal1Empty = (bulkcraft * Metal1Empty)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print (' from')
					print (Metal1Empty)
					print ('Metal 1')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'ScrapWheel':
					ScrapWood = (bulkcraft * ScrapWood)/singlecraft
					ScrapMetal = (bulkcraft * ScrapMetal)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('ScrapWheel from')
					print (ScrapWood)
					print ('Scrap Wood and')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'Bucket':
					ScrapMetal = (bulkcraft * ScrapMetal)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('Bucket from')
					print (ScrapMetal)
					print ('Scrap Metal')
					print (crafttime)
					print ('seconds')
					
				elif choice == 'SoilBag':
					ScrapWood = (bulkcraft * ScrapWood)/singlecraft
					SandEmpty = (bulkcraft * SandEmpty)/singlecraft
					Carrot = (bulkcraft * Carrot)/singlecraft
					crafttime = (bulkcraft * crafttime) / singlecraft
					Totalcraft = (bulkcraft * singlecraft) / singlecraft
					print (Totalcraft)
					print ('SoilBag from')
					print (ScrapWood)
					print ('Scrap Wood and')
					print (SandEmpty)
					print ('Sand and')
					print (Carrot)
					print ('Carrots')
					print (crafttime)
					print ('seconds')
				
			
				
				
				
				
				
				
				
				
				
				
				
				
			
