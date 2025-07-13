# 🤖 Fun Chatbot Script
print("🤖 Hi there! Welcome to the Chatbot 🤖\n")

# Ask for name
name = input("What is your name? ")
print(f"Great! {name}? Ha! Welcome aboard, {name}! 🎉\n")

# Ask for age
try:
    age = int(input("And how old are you? "))
except ValueError:
    print("❌ That's not a valid number! Restart me and try again.")
    exit()

if age < 18:
    print("🚫 BOUNCE kid! You’re too young.")
    exit()
else:
    print(f"✅ {age} is quite qualified here! Do you mind filling out these other confidential details?\n")

# Ask for consent
consent = input("Do you want to proceed? (YEY or NEY): ").strip().lower()
if consent == "ney":
    print("🚪 Okay, bounce then mate!")
    exit()
elif consent == "yey":
    print(f"✅ Alright, {name}! Let's go...\n")
else:
    print("🤔 Invalid response. Restart me and type YEY or NEY next time!")
    exit()

# Fake question loop
further = input("What are you looking forward to finding here? A or B: ").strip().upper()
if further not in ["A", "B"]:
    print("❌ Invalid response. Goodbye, come back later.")
else:
    print("😂 Hahaha… that wasn't even a real choice. Goodbye!")

# Last troll
further = input("\nFor the last time, what are you looking for today G? A or B (this is your last chance!): ").strip().upper()
if further not in ["A", "B"]:
    print("❌ Still invalid. Goodbye G! HAHAHA 😂")
else:
    print("🤪 You really thought there was a correct answer? Goodbye G! HAHAHA 😂")

print("\n👋 Thanks for chatting with us, have a great day!")
print("🕒 Hope I succeeded in wasting your time 😈")

import random
import time
import sys

# Helper for dramatic typing effect
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Colors using ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Start guessing game
print(f'\n{YELLOW}WAIT WAIT, Hold on don\'t go yet! I have one last game I want you to play 😈{RESET}')

# Ask if user wants to play
while True:
    guessing_game_approval = input('Do you want to play? (yey or ney): ').strip().lower()
    if guessing_game_approval in ['yey', 'ney']:
        break
    else:
        print(f'{RED}❌ Please type "yey" or "ney" only!{RESET}')

if guessing_game_approval == "ney":
    typewriter(f"{CYAN}🚪 Fine! No games for you. Goodbye!{RESET}")
    exit()

# Begin dramatic intro
typewriter(f"\n{CYAN}🎯 Guessing Game Loading...{RESET}")
for i in range(3, 0, -1):
    print(f"{YELLOW}Starting in {i}...{RESET}")
    time.sleep(1)

# Random word selection
words = ['singer', 'actor', 'teacher', 'pilot', 'doctor']
word = random.choice(words)
hint = f"{CYAN}This is your hint: The word is a noun and a profession often associated with popular people. 😉{RESET}"

print(hint)

guess = ''
num_guesses = 0
guess_limit = 5
out_of_guesses = False

# Game loop
while guess != word and not out_of_guesses:
    if num_guesses < guess_limit:
        guess = input('\nEnter your guess: ').strip().lower()
        num_guesses += 1
    else:
        out_of_guesses = True

# Dramatic countdown before result
typewriter(f"\n{YELLOW}Analyzing your guesses...{RESET}", 0.08)
for i in range(3, 0, -1):
    print(f"{RED}💥 {i}...{RESET}")
    time.sleep(0.7)

# Result
if out_of_guesses:
    typewriter(f"\n{RED}😂 You just suck G… YOU LOSE!! Better luck next time anyways🥲{RESET}", 0.1)
else:
    typewriter(f"\n{GREEN}😲 Did not think you could get this far… it hurts me to say YOU WIN G!!{RESET}", 0.1)
    typewriter(f"{YELLOW}This success won’t last for long anyway 😏{RESET}", 0.08)

typewriter(f"\n{CYAN}Okay bye for real now, HAVE A GREAT DAY: 😊{RESET}"  + name , 0.07)
