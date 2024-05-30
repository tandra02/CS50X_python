# Write a program that reads a positive integer n as input and prints the sum of the first n positive odd integers. 
# The program should use a while loop to calculate the sum. The program should: - Read a single positive integer n from the user - 
# Print the sum of the first n positive odd integers

# Read a single positive integer n from the user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_odd_integers = 0
current_odd_number = 1
count = 0

# Use a while loop to calculate the sum of the first n positive odd integers
while count < n:
    sum_of_odd_integers += current_odd_number
    current_odd_number += 2  # Move to the next odd number
    count += 1  # Increment the count of odd numbers summed

# Print the result
print(sum_of_odd_integers)
