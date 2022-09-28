#!/usr/bin/env python3
"""Alta3 Research | BCopeland
    Working with mixed lists"""
def main():
    my_list = [ "192.168.0.5", 5060, "UP" ]
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
    #print incoming list
    print(my_list)
    #print the first index within the list
    print("The first item in the list (IP): " + my_list[0])
    #print the second index (convert int to str with str())
    print("The second item in the list (port): " + str(my_list[1]))
    #print the last index with the the list
    print("The last item in the list (state): " + my_list[2])
    #print ip list
    print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
#call main
main()
