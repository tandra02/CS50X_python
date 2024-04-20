from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h >= 1 and h < 9:
        break

for i in range(h):
    print(' ' * (h-1-i), end='')
    print('#' * (i+1), end='') # incrementing with i value + 1
    print(' ' * 2, end='') # needs two spaces thats why multiplying with 2
    print('#' * (i+1)) # needs two spaces thats why multiplying with 2, mirorring the previous hashes pattern
