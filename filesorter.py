import os 
from pathlib import Path

#creating a dictionary to tell the program what the suffixes are for each of the file types
#i just looked up a list of file types for each and plopped those in there, idk what a .pptx is lmao
DIRECTORIES = { 
	"images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
			".heif", ".psd"], 
	"videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
				"pptx"], 
	"audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"plaintexts": [".txt", ".in", ".out"],
	"pdfs": [".pdf"], 
	#"python": [".py"], #took this out because it was interfering with this program since i had it stored on the desktop
	"runnables": [".exe"], 
	"jsons": [".json"],
	"zipped": [".zip"],
} 

#creating another dict for the directories, and making sure that it reads all the files that it can
FILETYPES = {fileType: directory 
				for directory, fileTypes in DIRECTORIES.items() 
				for fileType in fileTypes} 

def junk(): 
	for entry in os.scandir(): 
		if entry.is_dir(): 
			continue
		filePath = Path(entry) 
		fileType = filePath.suffix.lower() 
        #if the file type is in the list that we made, then put the file into those corresponding folders
		if fileType in FILETYPES: 
			pathOfTheFile = Path(FILETYPES[fileType]) 
			pathOfTheFile.mkdir(exist_ok=True) 
            #making sure that the folder is there, if not then it will make one
			filePath.rename(pathOfTheFile.joinpath(filePath)) 

junk() 

