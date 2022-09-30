#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Archive zipfiles """

import os
import zipfile

def zipdir(dirpath, zipfileobj):
    """does the work of writing data into our zipfile"""
    # os.walk() returns a 3-tuple
    # thats a fancy wany of saying it returns 3 things
    # always in the order... root, dirs, files
    # so ... the following line says given that you will return to us roots, dirs and files...
    for root, dirs, files in os.walk(dirpath):
        for file in files:  # we only want to loop across the file component
            print(os.path.join(root,file))   # create an aboslute path of where file lives
            zipfileobj.write(os.path.join(root, file)) ## adds files to our zipfileobject that was passed in
    return None

def main():
    """called at runtime"""

    dirpath = input("What directory are we archiving today? --> ")

    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? --? ")
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            zipdir(dirpath, zipfileobj)
    else:
        print("Run the script again when you have a valid directory to zip.")

main()
