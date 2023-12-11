## File Organizer
This simple Python script helps you organize your files on the desktop by categorizing them into specific folders based on their file extensions. Currently, it supports organizing files with extensions like .png, .jpg, .gif, .pdf, and .mp3.

# Usage
Clone or download the script to your local machine.
Open the script in a text editor and adjust the DESKTOP variable to the path of your desktop or the directory where you want to organize files.
Run the script.

```python file_organizer.py```

# Folder Structure
The script organizes files into the following folders:

Photos_folder: For files with .png, .jpg, and .gif extensions.
PDF_folder: For files with .pdf extension.
MP3_folder: For files with .mp3 extension.

# Notes
The script checks for the existence of destination folders and creates them if not present.
Files with extensions not specified in SUFFIX are categorized into a MISC_folder.
Feel free to customize the script to fit your specific needs or extend it to support additional file types.
