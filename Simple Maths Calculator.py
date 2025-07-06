# Simple Math Calculator
from math import sqrt, pow

print("🧮 Welcome to the Mini Calculator 🧮")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = num1 / pow(num2, 2) - num3
print("\nResult after calculation: ", result)
print("Square root of result: ", sqrt(result))

feedback = input("\nAre you satisfied with our services? (yey/ney): ").lower()
if feedback == "yey":
    print("✅ Okay thanks for the feedback!")
elif feedback == "ney":
    print("😅 Go ask ChatGPT then dummy!")