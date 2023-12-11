import os
import shutil

DESKTOP = "/Users/24RyanM/Desktop/"
SUFFIX = ['.png', '.jpg', '.gif', '.pdf', '.mp3']

print(DESKTOP + "PNG_folder")
files = os.listdir(DESKTOP)
for file in files:
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
        if (os.path.exists(DESKTOP + "Photos_folder")):
            shutil.move(DESKTOP + file, DESKTOP + "Photos_folder")
        else:
            os.mkdir(DESKTOP + "Photos_folder")
            shutil.move(DESKTOP + file, DESKTOP + "Photos_folder")
    elif file.endswith('.pdf'):
        if (os.path.exists(DESKTOP + "PDF_folder")):
            shutil.move(DESKTOP + file, DESKTOP + "PDF_folder")
        else:
            os.mkdir(DESKTOP + "PDF_folder")
            shutil.move(DESKTOP + file, DESKTOP + "PDF_folder")
    elif file.endswith('.mp3'):
        if (os.path.exists(DESKTOP + "MP3_folder")):
            shutil.move(DESKTOP + file, DESKTOP + "MP3_folder")
        else:
            os.mkdir(DESKTOP + "MP3_folder")
            shutil.move(DESKTOP + file, DESKTOP + "MP3_folder")