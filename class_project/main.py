#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Class Project """

def main():
    """ on runtime """
    import json
    import os

    print("Welcome To The Python Movie Library!\
            \n Enter a MENU key to navigate...")
    
    while True:
        menu_input = input("|  Home  |  Search  |  Exit  |\n")
        if menu_input.capitalize() == "Home":
            os.system('clear')
            print("Our Top 10 Favorites")
            movies = "./data/default_top10.json"
            with open(movies, 'r') as openfile:
                json_object = json.load(openfile)
                for rank, movie in json_object.items():
                    print(rank, ": ", movie)
            
        if menu_input.capitalize() == "Search":
            os.system('clear')
            search_input = input("Input keyword, and hit ENTER to search...")
            search(search_input)

        if menu_input.capitalize() == "Exit":
            os.system('clear')
            quit()

def search(input):
    import requests
    try:

        url = "https://online-movie-database.p.rapidapi.com/auto-complete"

        querystring = {"q":f"{input}"}

        headers = {
                "X-RapidAPI-Key": "b4345c9a47msh60f2da8131089fdp1e5897jsn77eb22836ae8",
                "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
    except:
        print("No Match Found")

def quit():
    import time

    print("Good Bye! Closing application...")
    time.sleep(2)
    exit()

main()    
