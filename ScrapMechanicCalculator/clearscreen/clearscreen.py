import os, platform


clearcmd = 0
opsys = platform.system()
if opsys == "Windows":
	clearcmd = "cls"
if opsys == "Linux":
	clearcmd = "clear"
	
def clearscreen():  #clears the screen. 
    os.system(clearcmd)


