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
    print("😂 Hahaha… that wasn't even a real choice. Goodbye anyway!")

# Last troll
further = input("\nFor the last time, what are you looking for today G? A or B (this is your last chance!): ").strip().upper()
if further not in ["A", "B"]:
    print("❌ Still invalid. Goodbye G! HAHAHA 😂")
else:
    print("🤪 You really thought there was a correct answer? Goodbye G! HAHAHA 😂")

print("\n👋 Thanks for chatting with us, have a great day!")
print("🕒 Hope I succeeded in wasting your time 😈")
exit()
