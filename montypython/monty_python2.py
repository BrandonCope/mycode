#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    While Looping with Conditionals """

def main():
    turn = 0

    while True:
        turn += 1
        user_input = input('Finish the movie title: "Monty Python\'s The Life of ..."\n')
        if user_input.capitalize() == 'Brian':
            print('Correct!\n')
            break
        elif turn == 3:
            print('Sorry, the answer was Brian!\n')
            break
        elif user_input.lower() == 'shrubbery':
            print('You gave the super secret answer!\n')
            break
        else:
            print('Sorry. Try Again!')

    try_again = input('Would you like to play again? [y/n]\n')
    if try_again.lower() == 'y':
        main()
    elif try_again.lower() == 'n':
        print("Goodbye")

main()
