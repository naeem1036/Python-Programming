# Function to find the second largest number in a list
def second_largest(numbers):
    # Remove duplicates and sort the list in descending order
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    # Check if there are at least two distinct numbers
    if len(unique_numbers) < 2:
        return "No second largest number exists."

    # Return the second largest number
    return unique_numbers[1]


# Take a list of numbers as input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the function and print the second largest number
print("The second largest number is:", second_largest(numbers))
