from cs50 import get_string

greet = get_string("Greeting: ").strip().capitalize()

if greet[0:5] == 'Hello':
    print("$0")
elif greet[0] == 'H' and greet[1:] != 'ello':
    print("$20")
else:
    print("$100")