# Outer function
def outer_function(a, b):
    # Inner function
    def inner_function():
        return a + b  # calculate addition of a and b
    
    # Call inner function and add 5
    result = inner_function() + 5
    return result

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

final_result = outer_function(num1, num2)
print("Final result (addition + 5):", final_result)
