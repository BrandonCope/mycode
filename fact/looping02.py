#!/usr/bin/env python3
""" Alta3 Research | BCopeland
    For - Using a file's lines as a source for the for-loop """

def main():
    
    with open("dnsservers.txt", "r") as dnsfile:
        for svr in dnsfile:
            print(svr, end="")
main()
