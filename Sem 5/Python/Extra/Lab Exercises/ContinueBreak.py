#Take 10 numbers from the user. Use `continue` to skip numbers divisible by both 3 and 5. 
#Use `break` if number is negative.If loop completes, use `else` to print “Input complete”.

count = 0
nums = []
for i in range(10):
    num = int(input("Enter the number : "))

    if num < 0:
        print("Negative numbers entered")
        break
    if num % 3 == 0 and num % 5 == 0:
        print("Skipped divisible!")
        continue
    nums.append(num)
    print("You entered",num)
    count += 1

else:
    print("Input complete!")