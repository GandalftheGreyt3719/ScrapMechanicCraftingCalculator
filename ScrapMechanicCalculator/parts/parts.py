import time, clearscreen
category = 'Parts'

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
MannequinHand = (" 2 Wood 1, 1 Paint Ammo, 3 Bees Wax for 1 Mannequin Hand ")
DuckStatue = ("1 Wood 1, 1 Paint Ammo, 3 Bees Wax, and 1 Glue for 1 Duck Statue")
TrafficCone = ("10 Metal 1 and 1 Paint Ammo for 1 Traffic Cone [15 Sec. Craft Time]")
ScrapWheel = ("20 Scrap Wood and 5 Scrap Metal for 1 Scrap Wheel [15 Sec. Craft Time]")
Bucket = ("5 Scrap Metal for 1 Bucket [20 Sec. Craft Time]")
SoilBag = ("10 Scrap Wood, 10 Sand, and 2 Carrots for 1 Soil Bag [20 Sec. Craft Time]")
def parts():
	print ("Here is the list of Craftable Parts: \n")
	print ("Wheel \nBigWheel \nI-BeamShort \nI-BeamLong \nI-BeamCorner \nI-BeamHolder \nI-BeamEnd \nSmallRectangleWindow \nSquareWindow \nLargeRectangleWindow \nLargeWindshield \nSmallWindShield \nAirConditioner \nPipeShort \nPipeLong \nPipeCorner \nPipeJoin \nValve \nSmallPipeShort \nSmallPipeLong \nSmallPipeBend \nSmallPipeTee \nSmallPipeCorner \nSmallPipe4Way \nSmallPipe4WayTee \nSmallPipe5Way \nSmallPipe6Way \nToiletPaper \nSink \nMug \nMannequinBoot \nMannequinHand  \nDuckStatue \nTrafficCone \nScrapWheel \nBucket \nSoilBag")
	time.sleep(2)
	input_str = "\n \nPlease choose a part to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
	choice = input(input_str)
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
		crafttime = 0
	elif choice == "IBeamLong":
		print (IBeamLong)
		Metal1Empty = 3
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "IBeamCorner":
		print (IBeamCorner)
		Metal1Empty = 1
		craft = True
		bulk = True	
		singlecraft = 1
		crafttime = 0
	elif choice == "IBeamHolder":
		print (IBeamHolder)
		Metal1Empty = 1
		craft = True
		bulk = True	
		singlecraft = 1
		crafttime = 0
	elif choice == "IBeamEnd":
		print (IBeamEnd)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallRectangleWindow":
		print (SmallRectangleWindow)
		GlassEmpty = 5
		Metal1Empty = 5
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SquareWindow":
		print (SquareWindow)
		GlassEmpty = 10
		Metal1Empty = 10
		craft = True
		bulk = True
		crafttime = 0
	elif choice == "LargeRectangleWindow":
		print (LargeRectangleWindow)
		GlassEmpty = 15
		Metal1Empty = 10
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "LargeWindshield":
		print (LargeWindshield)
		GlassEmpty = 20
		Metal1Empty = 10
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallWindshield":
		print (SmallWindShield)
		GlassEmpty = 10
		Metal1Empty = 5
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "AirConditioner":
		print (AirConditioner)
		Metal1Empty = 10
		CircutBoard = 3
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "PipeShort":
		print (PipeShort)
		Metal1Empty = 1    
		singlecraft = 1
		craft = True
		bulk = True
		crafttime = 0
	elif choice == "PipeLong":
		print (PipeLong)
		Metal1Empty = 3
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "PipeCorner":
		print (PipeCorner)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "PipeJoin":
		print (PipeJoin)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "Valve":
		print (Valve)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipeShort":
		print (SmallPipeShort)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipeLong":
		print (SmallPipeLong)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipeBend":
		print (SmallPipeBend)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipeTee":
		print (SmallPipeTee)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipeCorner":
		print (SmallPipeCorner)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipe4Way":
		print (SmallPipe4Way)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipe4WayTee":
		print (SmallPipe4WayTee)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "SmallPipe5Way":
		print (SmallPipe5Way)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 00
	elif choice == "SmallPipe6Way":
		print (SmallPipe6Way)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 00
	elif choice == "ToiletPaper":
		print (ToiletPaper)
		ScrapWood = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "Sink":
		print (Sink)
		Metal1Empty = 5
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "Mug":
		print (Mug)
		Metal1Empty = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "MannequinBoot":
		print (MannequinBoot)
		WocSteak = 1
		Wood1Empty = 2
		PaintAmmoEmpty = 1
		BeesWax = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "MannequinHand":
		print (MannequinHand)
		Wood1Empty = 2
		PaintAmmoEmpty = 1
		BeesWax = 3
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "DuckStatue":
		print (DuckStatue)
		Wood1Empty = 1
		PaintAmmoEmpty = 1
		BeesWax = 3
		Glue = 1
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 0
	elif choice == "TrafficCone":
		print (TrafficCone)
		Metal1Empty = 10
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 15
	elif choice == "ScrapWheel":
		print (ScrapWheel)
		ScrapWood = 20
		ScrapMetal = 5
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 15
	elif choice == "Bucket":
		print (Bucket)
		ScrapMetal = 5
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 20
	elif choice == "SoilBag":
		print (SoilBag)
		ScrapWood = 10
		SandEmpty = 10
		Carrot = 2
		craft = True
		bulk = True
		singlecraft = 1
		crafttime = 20

	if bulk == True:
			time.sleep(5)
			more=input('Do you want to craft in bulk? (True or False)(Same Capitalization): \n')
			if more == 'False':
				exit
			elif more == 'True':
				
				clearscreen.clearscreen()
				bulkcraft = int(input("How Much " + choice + " Do You Need: \n"))
				clearscreen.clearscreen()
				
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
