#!/usr/bin/env python3
""" Alta3 Research | BCopeland 
   Creating json data."""

def main():
    #Runtime
    import json
    import os
    import time

    dict_movie = {}
    os.system('clear')
    print("What are your top 10 favorite movies? Starting at #1 your most favorite.\n")
    rank = 1
    while rank <= 10:
        input_movie = input(f'Enter Title for Movie#{rank}... \ or "q" to quit.\n')
        if input_movie.lower() == 'q':
            break
        data = search(input_movie)
        if bool(data):
            while True:
                input_results = input('Enter the "Result" number to add to list...\n')
                if input_results.isdigit():
                    num = int(input_results) - 1
                    res = data[num]
                    input_id = res.get('id')
                    dict_movie[f"{rank}"] = { 'title':input_movie, 'id':input_id }
                    rank += 1
                    break
                else:
                    print('Invalid: Enter a "Result" number.')
        else:
            print("No Match Found, try something else...")
            time.sleep(1)
        os.system('clear')
        if rank == 10:
            filename = input("What is the name of the *.json file? ")
            with open(f"./data/{filename}.json", "w") as outfile:
                json.dump(dict_movie, outfile)
                print("The file " + filename + ".json should be in your data directory")
                break

def search(input):
    import requests
    import json

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
            print(f"Result: {i + 1}   Title: {json_data[i].get('l')}   Year: {json_data[i].get('y', 'Not Found')}   Stars: {json_data[i].get('s', 'Not Found')}\n")
        return json_data
    except:
        pass

main()
