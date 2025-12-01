# Write a Python program to select a random element from a list, set. Use random.choice()

import random

user_input = input("Enter elements separated by space: ")
my_list = user_input.split()

random_element = random.choice(my_list)
print("Randomly selected element: ", random_element)