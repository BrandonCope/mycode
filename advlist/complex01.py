#!/usr/bin/env python3
"""Alta3 Research | BCopeland
   List - simple list"""

def main():
    # create a list
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list
    print(list1)

    #display 2nd index
    print(list1[1])

    list2 = ["juniper"]
    
    #spread list2 into list1 and display list1
    list1.extend(list2)
    print(list1)
    
    #add list3 to list1 and display list1
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    list1.append(list3)
    print(list1)
    
    #display item 5 in list1
    print(list1[4])
    
    #display first IP adress in list1
    print(list1[4][0])

    animals = ["Fox", "Bee", "Cat", "Dog", "Cow"]
    for i in animals:
        print(i, end=" ")
    print(end="\n")

main()

