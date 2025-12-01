#Take 10 user inputs. If the number is prime, skip it (use `continue`).If it is divisible by 10,
#stop the loop (use `break`). Use `else` to confirm normal loop completion.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(10):
    num = int(input("Enter number : \n"))

    if is_prime(num):
        print("Number is prime !")
        continue
    if num % 10 == 0:
        print("Number is divisible by 10!")
        break
    print("Accepted number : ",num)

else:
    print("Loop completed after break!")