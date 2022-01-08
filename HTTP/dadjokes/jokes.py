import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD JOKE 3000")
header = colored(header, color="magenta")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

results = res["results"]
num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}")
    print(results[0]["joke"])
else:
    print("Sorry, no jokes found with that term")
