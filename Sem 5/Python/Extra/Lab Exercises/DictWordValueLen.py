#Accept a sentence and create a dictionary where each word is a key and value is its length. 
#Print the word(s) with the maximum length.

sentence = input("Enter the sentence : ")
words = sentence.split()
words_len = {word:len(word) for word in words}
print("Words length Dictionary : ",words_len)

max_length = max(words_len.values())

print("Words with maximum length : ")
for word,length in words_len.items():
    if length == max_length:
        print(word)