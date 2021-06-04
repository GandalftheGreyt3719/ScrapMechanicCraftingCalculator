import time, clearscreen
category = 'Interactive Parts'

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
def interactive():
		print ("Here is the list of Craftable Interactive Parts: \n")
		print ("Beacon \nSportSuspension \nOffRoadSuspension \nDriverSeat \nSeat \nDriverSaddle \nSaddle \nGasEngine \nElectricEngine \nThruster \nController \nSensor \nPiston \nGasContainer \nWaterContainer \nBatteryContainer \nSawBlade \nDrill \nVacuumPump \nVacuumPipe \nVacuumPipeCorner \nLargeChest \nRefineBot \nResourceCollector \nCraftBot \nScrapGasEngine \nScrapDriverSeat \nScrapSeat \nRespawnBed \nChest \nFridge \nChemicalContainer \nBearing \nToilet \nSwitch \nButton \nRadio \nHorn \nLogicGate \nTimer \nSmallExplosive \nLargeExplosive \nWaterCannon \nHeadlight")
		time.sleep(2)
		input_str = "\n \nPlease choose a block to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
		choice = input(input_str)

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
				
				clearscreen.clearscreen
				bulkcraft = int(input("How Much " + choice + " Do You Need: \n"))
				clearscreen.clearscreen()
				
				
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
				
				
				

