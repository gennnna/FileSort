import os 
from pathlib import Path 

#here, creating a list of possible file types and the corresponding names of the files that they will be assigned to
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
	#"pythoon": [".py"], #took this out because it was interfering with this program since i had it stored on the desktop
	"runnables": [".exe"], 
	"jsons": [".json"],
	"zipped": [".zip"],
} 

#setting a dict to make it easier to call the list that i just made
FILETYPES = {fileType: directory 
				for directory, fileTypes in DIRECTORIES.items() 
				for fileType in fileTypes} 

#defining a function/method
def junk(): 
    #for every file it sees
	for entry in os.scandir(): 
		if entry.is_dir(): 
			continue
        #setting variables
		filePath = Path(entry) 
		fileType = filePath.suffix.lower() 
        #if the file type is in the list that we made, then put the file into those corresponding folders
		if fileType in FILETYPES: 
			pathOfTheFile = Path(FILETYPES[fileType]) 
			pathOfTheFile.mkdir(exist_ok=True) 
            #making sure that the folder is real, if not then it will make one
			filePath.rename(pathOfTheFile.joinpath(filePath)) 

junk() 

