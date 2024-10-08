# Function to count digits in a given string
def count_digit(s):
    digit_count = 0
    for ch in s:
        if ch.isdigit():
            digit_count += 1
    return digit_count

# Take input from user as string
s = input("Enter a string: ")

print("Number of digits:", count_digit(s))
