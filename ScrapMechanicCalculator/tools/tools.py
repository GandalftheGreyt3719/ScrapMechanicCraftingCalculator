import time, clearscreen
category = 'Tools'

ConnectTool = ("10 Scrap Metal and 2 Circut Board for 1 Connect Tool [35 Sec. Craft Time]")
WeldTool = ("20 Metal 2, 5 Circut Board, and 5 Component Kit for 1 Weld Tool [35 Sec. Craft Time]")
PaintTool = ("10 Metal 1, 5 Glass, and 3 Component Kits for 1 Paint Tool [35 Sec. Craft Time]")
def tools():
	print ("Here is the list of Craftable Tools: \n")
	print ("Connect Tool \nWeld Tool \nPaint Tool")
	time.sleep(2)
	input_str = "\n \nPlease choose a block to craft \n\x1B[3m Please use same Capitalization and spaces\x1B[23m \n "
	choice = input(input_str)
	clearscreen.clearscreen()
	if choice == "Connect Tool":
			print (ConnectTool)
			craft = True
			bulk = False
	elif choice == "Weld Tool":
			print (WeldTool)
			craft = True
			bulk = False
	elif choice == "Paint Tool":
			print (PaintTool)
			craft = True
			bulk = False
