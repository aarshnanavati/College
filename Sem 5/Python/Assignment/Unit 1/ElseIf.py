#Write a Python program which will have Main Menu for selecting Elective Subjects as follows: 
#Main Menu: 1. Joomla 2. Ruby onRails 3. Drupal 4. Android
#5. iOS Display proper message for every choice. Use elif to create a menu:

subject = []
n = int(input("Enter the number of elective subjects you want to add: "))

for i in range(n):
    subject_name = input("Enter the elective sub name: ")
    subject.append(subject_name)
print("Your elective subjects list:\n", subject)
choice = int(input("Enter your choice (1-5): "))

if choice == 1 : 
    print("You have selected Joomla. It is a free and open-source content management system (CMS) for publishing web content.")
elif choice == 2:
    print("You have selected Ruby on Rails. It is a server-side web application framework written in Ruby under the MIT License.")
elif choice == 3:
    print("You have selected Drupal. It is a free and open-source web content management framework written in PHP.")
elif choice == 4:
    print("You have selected Android. It is a mobile operating system based on a modified version of the Linux kernel and other open source software.")     
elif choice == 5:
    print("You have selected iOS. It is a mobile operating system created and developed by Apple Inc. exclusively for its hardware.")
else:
    print("Invalid choice. Please select a number between 1 and 5.")
