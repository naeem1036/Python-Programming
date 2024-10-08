# Function to count vowels in a string
def count_vowels(s):
    # Convert the string to lowercase to handle both upper and lower case vowels
    s = s.lower()
    # List of vowels
    vowels = "aeiou"
    count = 0
    # Loop through each character and check if it's a vowel
    for char in s:
        if char in vowels:
            count += 1
    return count

# Take input from user
s = input("Enter a string: ")

# Call the function and print the number of vowels
print("Number of vowels:", count_vowels(s))
