#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Creating json data."""
import os
import time
import json

from search import search

def main():
    """Builds json file for top10 movies"""
    #Runtime
    dict_movie = {}
    os.system('clear')
    print("What are your top 10 favorite movies? Starting at #1 your most favorite.\n")
    rank = 1
    while rank <= 10:
        input_movie = input(f'Enter Title for Movie#{rank}... \
                or "q" to quit.\n')
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
                print('Invalid: Enter a "Result" number.')
        else:
            print("No Match Found, try something else...")
            time.sleep(1)
        os.system('clear')
        if rank == 10:
            filename = input("What is the name of the *.json file? ")
            with open(f"../data/{filename}.json", "w", encoding='UTF-8') as outfile:
                json.dump(dict_movie, outfile)
                print("The file " + filename + ".json should be in your data directory")
                break

if __name__ == "__main__":
    main()
