
text = "Welcome to Python Programming"

#print whole text
print("FullText : ",text)

#print only 1st character of string
print("First character : ",text[0])

#print 3rd character to -1 character using slicing
print("3rd to -1 character : ",text[2:-1])

#print string from 4th character to end
print("4th character to end : ",text[3:])

#print whole string 5 times
print("5 times string repeated : ",text * 5)

#count the occurance of "to"
print("count of to : ",text.count("to"))

#print length of string
print("Length of string : ",len(text))

# Convert the string to lowercase
print("Lowercase :",text.lower())

# Find the substring "Python"
print("Index of python : ",text.find("python"))

# Remove leading spaces
print("Leadibg spaces removed : ",text.lstrip())

#Check if string ends with "is"
print("End with  "is" ? ",text.endswith("is"))