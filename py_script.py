#!/usr/bin/python3
"""Alta3 Research | BCopeland
    Lab 14: Script Writing Challenge"""

def main():
    #pause and wait for username input
    user_name = input("What is your name?\n")

    #pause and wait for day of week input
    week_day = input("\nWhich day of the week is today?\n")

    #display the user inputs
    print(f"\nHello, {user_name.capitalize()}! Happy {week_day.capitalize()}!")

#call main
main()
