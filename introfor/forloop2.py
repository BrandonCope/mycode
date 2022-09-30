#!/usr/bin/python3
""" Alta3 Research | BCopeland
   Printing dictionary data stored as lists to the screen"""

def main():
    farms = [
            {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
            {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
            {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
            ]
    for farm in farms:
        print(farm.get("name", "Unkown Farm"), end=":\n ")
        for stock in farm.get("agriculture"):
            print(" -", stock)

main()
