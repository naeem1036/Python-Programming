# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Take input from user
s = input("Enter a string: ")

# Call the function and print whether the string is a palindrome
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
