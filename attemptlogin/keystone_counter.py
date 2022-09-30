#!/usr/bin/env python3

def main():
   
    loginfail = 0
    successful = 0

    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as k_file:
        for line in k_file:
            if "- - - - -] Authorization failed" in line:
                loginfail += 1
                print(line.split(" ")[-1])
            elif "-] Authorization failed" in line:
                successful += 1
    print("The number of failed log in attempts is", loginfail)
    print("The number of successful log in attempts is", successful)
main()
