#Accept a string and create a dictionary where each key is a character and value is 
#its frequency. Ignore spaces and make it case-insensitive.

text = input("Enter a string : ")

text = text.lower().replace(" ", " ")

freq = {}

for char in text :
    freq[char] = freq.get(char,0)+1

print("Character Frequency : ",freq)