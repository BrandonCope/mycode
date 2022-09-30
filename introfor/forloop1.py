#!/usr/bin/env python3
""" Alta3 Research | BCopeland
   learning about for logic"""

def main():
    
    # create the list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    # create list of approved vendors
    approved_vendors = ["cisco", "juniper", "big_ip"]
    # loop across vendors list
    for x in vendors:
        print("\nThe vendor is:" + x, end="")
        if x not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")  # when the loop ends print this

main()
