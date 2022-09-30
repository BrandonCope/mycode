#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    check if zip is valid """

import zipfile

def main():

    zip_file = input("What file would you like to validate? (provide full or relative path)")

    if zipfile.is_zipfile(zip_file):
        print(f"{zip_file} is a 'zip' file.")
    else:
        print(f"The provided file is not a 'zip' file.")
main()
