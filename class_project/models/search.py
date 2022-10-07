"""Alta3 Research | BCopeland
    Handles User Search Functionality"""
import os
import json
import requests

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
        os.system('clear')
        break

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

def get_top10_data(selected, data):
    """Displays data from one of the top10 movies the user selects"""
    os.system('clear')
    movie_id = data.get(selected).get('id')
    json_data = search(movie_id)
    get_details(json_data)

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

def prompt_narrow_search(data):
    """Promts user too select from narrowed search """
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
    """Displays Search Results in a clear and readable format"""
    os.system('clear')
    print(f"{res.get('l')}  ({res.get('y', 'Not Found')})")
    print(f"Category: {res.get('qid', 'Not Found').capitalize()}")
    print(f"IMDB Rank: {res.get('rank', 'Not Found')}")
    print(f"Stars: {res.get('s', 'Not Found')}\n")
