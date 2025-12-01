
from utilities.stringops import StrFunctions as sf

sample = "Hello World! Welcome to python!"

print("Original String : ",sample)
print("Reversed String : ",sf.reverse_string(sample))
print("Uppercase String : ",sf.toUpperCase(sample))
print("Lowercase String : ",sf.toLowerCase(sample))
print("Count of 'o",sf.count_subString(sample,"o"))
print("Replace world with universe",sf.replace_substring(sample,"world","universe"))