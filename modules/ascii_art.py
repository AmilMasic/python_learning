import pyfiglet
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

msg = input("what would you like to print?")
color = input("what color?")

if color not in valid_colors:
    color = "magenta"
    
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)

print(colored_ascii)
