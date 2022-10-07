#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Class Project """
import os
import sys
import json
import time
import requests
from models.home import display_home

def main():
    """on runtime """
    #top10_movies = "./data/default_top10.json"
    top10_data = display_home()
    menu_opt = ("Home", "Search", "Exit")
    while True:
        menu_input = input("MENU:\n|  Home  |  Search  |  Exit  |\n")
        if bool(menu_input):
            if menu_input.capitalize() in menu_opt or menu_input.isdigit():
                if menu_input.capitalize() == menu_opt[0]:
                    display_home()
                elif menu_input.capitalize() == menu_opt[1]:
                    prompt_search()
                elif menu_input.capitalize() == menu_opt[2]:
                    close_app()
                elif bool(int(menu_input)) and int(menu_input.lstrip("0")) in range(1, 11):
                    get_top10_data(menu_input.lstrip("0"), top10_data)
                else:
                    display_404()
            else:
                display_404()
        else:
            display_404()

def display_404():
    """Displays 404 if user inputs invalid menu path"""
    os.system('clear')
    print("404: Page Not Found")


def get_top10_data(selected, data):
    """Displays data from one of the top10 movies the user selects""" 
    os.system('clear')
    movie_id = data.get(selected).get('id')
    data = search(movie_id)
    get_details(data)

def prompt_search():
    """Prompts user to input keyword to search for movies"""
    os.system('clear')
    while True:
        search_input = input('Input keyword, and hit ENTER to search...\
                        or "q" to quit.\n ')
        if bool(search_input) and search_input != 'q':
            data = search(search_input)
            get_details(data)
            break
        else:
            os.system('clear')
            break

def search(search_key):
    """Handles API search from online movie database"""
    try:
        url = "https://online-movie-database.p.rapidapi.com/auto-complete"
        querystring = {"q":f"{search_key}"}
        headers = {
                "X-RapidAPI-Key": "b4345c9a47msh60f2da8131089fdp1e5897jsn77eb22836ae8",
                "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
                }
        print("Searching...")
        response = requests.request("GET", url, headers=headers, params=querystring, timeout=5)
        json_data = json.loads(response.text).get('d', 'No Match Found')
        if bool(json_data):
            if len(json_data) > 1:
                display_res(json_data)
                return json_data
            return json_data
    except ValueError:
        print("No Match Found")
        return None

def display_res(data):
    """Displays List of Result Findings in a clear format"""
    os.system('clear')
    length = len(data)
    for i in range(length):
        print(f"Result: {i + 1}   Title: {data[i].get('l', 'Not Found')}\
                   Year: {data[i].get('y', 'Not Found')}\n")

def get_details(data):
    """Prompts user to select result number, then makes call to print details"""
    if bool(data):
        if len(data) > 1:
            prompt_narrow_search(data)
        else:
            movie = data[0]
            print_details(movie)
    else:
        os.system('clear')
        print("No Match Found")

def prompt_narrow_search(data):
    while True:
        input_results = input('Enter the "Result" number to get more details... \
                or "q" to quit.\n')
        if input_results.isdigit(): 
            if int(input_results) in range(1, (len(data)+1)):
                os.system('clear')
                num = int(input_results) - 1
                res = data[num]
                print_details(res)
                break
        if input_results.lower() == 'q':
            os.system('clear')
            break
        print('Invalid: Enter a "Result" number.')

def print_details(res):
    os.system('clear')
    """Displays Search Results in a clear and readable format"""
    print(f"{res.get('l')}  ({res.get('y', 'Not Found')})\n")
    print(f"Category: {res.get('qid', 'Not Found').capitalize()}")
    print(f"IMDB Rank: {res.get('rank', 'Not Found')}")
    print(f"Stars: {res.get('s', 'Not Found')}\n")

def close_app():
    """Closes the application when called"""
    os.system('clear')
    print("Good Bye! Closing application...")
    time.sleep(2)
    sys.exit()

if __name__ == "__main__":
    main()
