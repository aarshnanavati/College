#Write a program that reads a list of words and returns a dictionary where keys are word lengths
#and values are lists of words of that length.

words = input("Enter words : ").split()
length_dict = {}

for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = [word]
    else:
        length_dict[length].append(word)
print("Dictionary of word lengths:  ")
print(length_dict)