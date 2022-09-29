#!usr/bin/env python3
""" Alta3 Research | BCopeland
    Lists Challenge"""
import random

def main():
    #Part 1 and 2
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif",
                  "Brent", "Cedric", "Chris",
                  "Cory", "Ebrima", "Franco",
                  "Greg", "Hoon", "Joey",
                  "Jordan", "JC", "LB",
                  "Mabel", "Shon", "Pat", "Zach"]
    #Part 3
    wordbank.append(4)
    print(wordbank)

    #Part 4 and 5
    is_valid=True
    num=int(input("Pick a number between 0 and 18, press enter!\n"), 10)
    student_name=""
    while is_valid:
        if num >= 0 and num <= 18 and num != None:
            print(f"You selected {num}.")
            student_name=tlgstudents[num]
            is_valid=False
        else:
            print(f"The number {num} is not between 0 and 18. Please try again?")
    
    #Part 6
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    #Super Bonus
    random_student = tlgstudents[random.randint(0, 18)]
    print(random_student)
    #Mega Bonus
main()
