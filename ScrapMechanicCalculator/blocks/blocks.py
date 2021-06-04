import time, clearscreen
category = 'Blocks'

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
def blocks():
	print ("Here is the list of Craftable Blocks: \n")
	print ("Concrete1 \nWood1 \nMetal1 \nBarrierBlock \nTileBlock \nBrickBlock \nGlassBlock \nGlassTile \nPathLight \nCardBoard \nWood2 \nWood3 \nMetal2 \nMetal3 \nConcrete2 \nConcrete3 \nExtrudedMetal \nBubblePlastic \nCarpet \nNet \nSolidNet \nPunchedSteel \nRestroomBlock \nDiamondPlate \nSand \nArmoredGlass")
	time.sleep(2)
	input_str = "\n \nPlease choose a block to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
	choice = input(input_str)
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
	
	if bulk == True:
			time.sleep(5)
			more=input('Do you want to craft in bulk? (True or False)(Same Capitalization): \n')
			if more == 'False':
				exit
			
			elif more == 'True':
				clearscreen.clearscreen()
				bulkcraft = int(input("How Much " + choice + " Do You Need: \n"))
				clearscreen.clearscreen()
				
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
				
				
