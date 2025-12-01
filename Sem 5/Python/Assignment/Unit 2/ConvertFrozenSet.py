#Create a set of vowels found in a user-given sentence.
#Then convert the set to a frozenset and try to remove an element (handle the exception).

sentence = input("Enter the sentence :")
vowels = set("aeiou")
found = {ch for ch in sentence if ch in vowels }
print("vowels found!!",found)

frozen = frozenset(found)
print("Frozen set : ",frozen)

try:
    frozen.remove('a')
except AttributeError:
    print("Cannot remove from frozenset!")