import os
import json

def display_home():
    """Displays greeting to user, and top 10 movies from library"""
    os.system('clear')
    print("Welcome To The Python Movie Library!\
            \n***Enter a MENU key to navigate***\
            \n***Or Select one of our Top 10 by Rank Number[1-10], for details***")
    print("\nOur Top 10 Favorites")
    data = open_json()
    return data


def open_json():
    top10_file = "./data/default_top10.json"
    with open(top10_file, 'r', encoding='UTF-8') as openfile:
        json_object = json.load(openfile)
        for rank, movie in json_object.items():
            print(rank, ": ", movie.get('title'))
        print("")
        return json_object
