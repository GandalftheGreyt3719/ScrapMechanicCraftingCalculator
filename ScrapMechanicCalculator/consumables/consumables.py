import time, clearscreen
category = 'Consumables'

Gasoline = ("5 Crude Oil for 5 Gasoline [10 Sec. Craft Time]")
Battery = ("10 Scrap Metal, 5 Glow, and 5 Chemical for 5 Battery")
Water = ("1 Bucket of Water for 1 Water and 1 Empty Bucket [5 Sec. Craft Time]")
PaintAmmo = ("5 Pigment Flower for 5 Paint Ammo [15 Sec. Craft Time]")
Chemical = ("1 Bucket of Chemical for 1 Chemicals and 1 Empty Bucket [5 Sec. Craft Time]")
Fertilizer = ("10 Tomato Seeds, 10 Carrot Seeds, and 10 Redbeetfor 5 Fertilizer [10 Sec. Craft Time]")
Glowstick = ("4 Chemical and 4 Glow for 4 Glow Stick [20 Sec. Craft Time]")
def consumables():
		print ("Here is the list of Craftable Consumables: \n")
		print ("Gasoline \nBattery \nWater \nPaintAmmo \nChemical \nFertilizer \nGlowstick")

		time.sleep(2)
		input_str = "\n \nPlease choose a block to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
		choice = input(input_str)
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
