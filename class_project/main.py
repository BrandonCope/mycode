#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    Class Project """
from models.home import display_home
from models.search import prompt_search, get_top10_data
from models.helper import display_404, close_app

def main():
    """on runtime """
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

if __name__ == "__main__":
    main()
