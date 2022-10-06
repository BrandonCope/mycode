#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Class Project """

def main():
    """ on runtime """
    import os
    import json
    
    os.system('clear')
    render_home(json)
    while True:
        menu_input = input("|  Home  |  Search  |  Exit  |\n")
        if menu_input.capitalize() == "Home":
            os.system('clear')
            render_home(json)
            
        if menu_input.capitalize() == "Search":
            os.system('clear')
            search_input = input('Input keyword, and hit ENTER to search...\
                    or "q" to quit.\n ')
            if search_input.lower() != 'q':
                data = search(search_input)
                if data:
                    get_details(data, os)
                else:
                    print("No Match Found")
            else:
                os.system('clear')

        if menu_input.capitalize() == "Exit":
            os.system('clear')
            quit()

def render_home(json):
    print("Welcome To The Python Movie Library!\
            \n***Enter a MENU key to navigate***\
            \n***Or Select one of our Top 10 by Rank Number[1-10], for details***")
    print("\nOur Top 10 Favorites")
    movies = "./data/default_top10.json"
    with open(movies, 'r') as openfile:
        json_object = json.load(openfile)
        for rank, movie in json_object.items():
            print(rank, ": ", movie)
        print("")

def search(input):
    import requests
    import json
    import os
    try:
        url = "https://online-movie-database.p.rapidapi.com/auto-complete"
        querystring = {"q":f"{input}"}
        headers = {
                "X-RapidAPI-Key": "b4345c9a47msh60f2da8131089fdp1e5897jsn77eb22836ae8",
                "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
                }
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(response.text)['d']
        for i in range(len(json_data)):
            print(f"Result: {i + 1}   Title: {json_data[i].get('l')}   Year: {json_data[i].get('y', 'Not Found')}\n")
        return json_data
    except:
        pass

def get_details(data , os):
    while True:
        input_results = input('Enter the "Result" number to get more details... \
                or "q" to quit.\n')
        if input_results.isdigit():
            os.system('clear')
            num = int(input_results) - 1
            res = data[num]
            print(f"{res.get('l')}  ({res.get('y', 'Not Found')})\n")
            print(f"Category: {res.get('qid').capitalize()}")
            print(f"IMDB Rank: {res.get('rank')}")
            print(f"Stars: {res.get('s')}\n")
            break
        if input_results.lower() == 'q':
            os.system('clear')
            break
        else:
            print('Invalid: Enter a "Result" number.')

def quit():
    import time

    print("Good Bye! Closing application...")
    time.sleep(2)
    exit()

main()    
