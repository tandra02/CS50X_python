'''You are given a name and a positive integer. You are required to print a greeting message using the name and a number of 
exclamation marks equal to the given integer. For example, if the given name is 'John' and the integer is 3, the output should be 
'Hello, John!!!'. You will first take a string as input representing the name and then take an integer as input representing the number 
of exclamation marks.'''

[name, exclamation_number] = [input() for _ in range(2)]
print(f'Hello {name}{int(exclamation_number) * "!"}')