#Input a paragraph and count the number of words, vowels, and consonants. Store word frequencies in a dictionary.

text = input("Enter the text : ")
words = text.split()
print("Total Words :",len(words))

vowels_list = "aeiouAEIOU"
vowels = 0
constonents = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels_list:
            vowels += 1
        else:
            constonents += 1

print("Vowels : ",vowels)
print("Constonents : ",constonents)

freq = {}
for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequencies : ",freq)