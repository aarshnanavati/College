# Write a function that takes a string as input and returns the number of vowels in it.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


s = input("Enter a String : ")
print("Vowels in String are : ",count_vowels(s))