#Write a Python program to flatten a nested list (e.g., `[[1, 2], [3, 4], [5]]`) 
#into a single list `[1, 2, 3, 4, 5]`without using built-in `sum()`.

nested_list = [[1,2],[3,4],[5]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Flattened List : ",flat_list)