#!/usr/bin/env python3

""" Alta3 Research | BCopeland """

import matplotlib.pyplot as plt
import time

def main():
    user_input = input("Would you like to build the perfect pizza? [y/n]...")
    if user_input.lower() == "y":
        print("Your perfect pizza is being summoned!!!")
        time.sleep(2)
        build_graph()
        print("Pizza. Pizza. Enjoy!!")
    else:
        print("Good Bye!")

def build_graph():
    fig, ax = plt.subplots()

    fruits = ['tomato sauce', 'mozzarella', 'basil', 'tomato slices']
    counts = [100, 30, 15, 25]
    bar_labels = ['tomato sauce', 'mozzarella', 'basil', 'tomato slices']
    bar_colors = ['tab:red', 'tab:orange', 'tab:green', 'tab:blue']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('percentage')
    ax.set_title('Perfect Pizza Ingredients and color')
    ax.legend(title='Pizza Ingredients')

    plt.savefig("/home/student/static/perfectPizza.png")

main()
