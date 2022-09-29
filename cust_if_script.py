#!/usr/bin/env python3
"""Alta3 Research | BCopeland
    Grading Scale"""

def main():
    score = int(input("Enter student score(100-0) to determine letter grade(A-F): \n"))
    if score >= 90 and score <= 100:
        print("Letter Grade: A")
        print("Congratulations!!!")
    elif score >= 80 and score <= 89:
        print("Letter Grade: B")
        print("Good work!")
    elif score >= 70 and score <= 79:
        print("Letter Grade: C")
        print("Ok work, try harder.")
    elif score >= 60 and score <= 69:
        print("Letter Grade: D")
        print("Work needs improvement.")
    elif score < 60:
        print("Letter Grade: F")
        print("Failed to grasp concepts. Try Again!")
    else:
        print("Invalid Input: Please enter a score between 0 and 100...")
main()
    
