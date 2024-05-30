from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h >= 1 and h < 9: # Height can't be more than 8 or negative number
        break

for i in range(0, h): 
    for j in range(0, h):
        if i+j < h-1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
