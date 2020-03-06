import os
from pathlib import Path

Extensions = {
"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", "svg", 
           ".psd"], 
"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".qt", 
           ".mpg", ".mpeg", ".3gp"], 
"Documents": [".oxps", ".epub", ".docx", ".doc", ".ods", ".odt",
              ".rtf", ".rtfd", ".xls", ".xlsx", ".ppt", "pptx"], 
"Archives": [".iso", ".tar", ".gz", ".7z", ".rar",".zip"], 
"Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"], 
"Text": [".txt", ".in", ".out"]
}

# {'.jpeg': 'Images', '.jpg': 'Images',...., '.mp4': 'Videos'}
data = {file_ext: folder
        for folder, file_formats in Extensions.items()
        for file_ext in file_formats}


def organize_files():
    # print(data)
    # Scans the current directory
    for entry in os.scandir():
        # if the entry is a directory skips it 
        if entry.is_dir():
            continue
        # Saves the path and type of each scanned file
        file_path = Path(entry)
        file_ext = file_path.suffix.lower()
        # print(file_path, file_ext)
        if file_ext in data:
            # Saves the Values as desired path from data dictionary for each Key in it. 
            folder_path = Path(data[file_ext])
            # print(folder_path)
            # make a new directory from the above path we got
            folder_path.mkdir(exist_ok=True)
            # Change the file path and move into the new directory
            file_path.rename(folder_path.joinpath(file_path))


if __name__ == "__main__":
    organize_files()
    print()
    print("How to Find What We Organised:")
    print("Audio Folder        - Contains Audio files.")
    print("Videos Folder       - Contains Video files.")
    print("Images Folder       - Contains Image files.")
    print("Archives Folder     - Contains Compressed files and Other Archives.")
    print("Documents Folder    - Contains Documents files from Libre Office / MS Office.")
    print("Text Folder         - Contains Plain Text files.")
    input('Hit enter to exit')
