# Function to find the GCD of two numbers using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Take two integer inputs from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function and print the GCD of the two numbers
print("The GCD of", a, "and", b, "is:", gcd(a, b))
