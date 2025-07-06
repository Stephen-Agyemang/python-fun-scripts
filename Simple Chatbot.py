# Fun Chatbot Script
print("Hi there! Welcome to the Chatbot ")

name = input("What is your name? ")
print(f"Great! {name}, welcome aboard!")

age = int(input("And how old are you? "))
if age < 18:
    print("BOUNCE kid! You’re too young.")
    exit()
else:
    print(f"{age} is quite qualified here, do you mind filling these other confidential details?")

consent = input("Do you want to proceed? (YEY or NEY): ").lower()
if consent == "ney":
    print("🚪 Okay, bounce then mate!")
    exit()
elif consent == "yey":
    print(f" Alright " + name )

further = input(" What are you looking forward to finding here? A or B")
if further == "A":
    print("Invalid response. Goodbye comeback later.")
elif further =="B":
    print("Invalid response. Goodbye comeback later.")

print("\nThanks for chatting with us, have a great day!")

further = input("\nFor the last time, What are you looking forward to finding today G? A or B, this you last chance by the way")
if further == "B":
    print("Still Invalid response. Goodbye G! HAHAHA")
elif further =="A":
    print("Still Invalid response. Goodbye G! HAHAHA")

print("\nThanks for chatting with us, have a great day!")

print("Hope i succeeded in wasting your time")
exit()
