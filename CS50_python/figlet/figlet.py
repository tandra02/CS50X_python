import pyfiglet
import sys
import random

fig = pyfiglet.Figlet()
fonts = fig.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    print("Output:\n" + fig.renderText(text))
    sys.exit()

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font_name = sys.argv[2]
    if font_name not in fonts:
        sys.exit("Invalid usage")
    text = input("Input: ")
    print(f"Output (Font: {font_name}):\n" + pyfiglet.figlet_format(text, font=font_name))
    sys.exit()

else:
    sys.exit("Invalid usage")
