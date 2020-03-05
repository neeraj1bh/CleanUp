Extensions = {
"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", "svg", 
           ".psd"], 
"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".qt", 
           ".mpg", ".mpeg", ".3gp"], 
"Documents": [".oxps", ".epub", ".docx", ".doc", ".ods", ".odt",
              ".rtf", ".rtfd", ".xls", ".xlsx", ".ppt", "pptx"], 
"Archives": [".iso", ".tar", ".gz", ".7z", ".rar",".zip"], 
"Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"], 
"Text": [".txt", ".in", ".out"], 
}

# {'.jpeg': 'Images', '.jpg': 'Images',...., '.mp4': 'Videos'}
data = {file_ext: folder
            for folder, file_formats in Extensions.items()
                for file_ext in file_formats}