#!/usr/bin/env python3
""" Alta3 Research | BCopeland 
   Creating json data."""

def main():
    #Runtime
    import json
        
    dict_movie = {}
    print("Hello! This program will make you a *.json file\n")
    print("What are your top 10 favorite movies? Starting at #1 your most favorite.")
    rank = 1
    while rank <= 10:
        input_movie = input(f"\nMovie#{rank}... ")
        dict_movie[f"{rank}"] = input_movie
        keep_going = input(f"\nEnter to continue, or \
        enter 'q' to quit: ")
        rank += 1
        if (keep_going.lower() == 'q'):
            break

    filename = input("\nWhat is the name of the *.json file? ")
    dict_movie
    with open(f"./data/{filename}.json", "w") as outfile:
        json.dump(dict_movie, outfile)
    

    print("The file " + filename + ".json should be in your data directory")

main()
