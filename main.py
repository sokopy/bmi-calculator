# Clearing console
import os
os.system("cls")

# Declaring variables.
height_input = float(input("Enter your height in meters: "))
weight_input = float(input("Enter your weight in kilograms: "))
bmi = weight_input/(height_input*height_input)

# Coding.
os.system("cls")
print(f"Your BMI is {int(bmi)}\n")
if bmi < 18.5:
    print("You are below a normal BMI! As a programmer, I cannot tell you what to do, but you should check that with a doctor.")
elif (bmi > 18.5) & (bmi < 24.9):
    print("Your BMI is normal! Remember to eat healthy and make exercise to keep it in the normal range.")
elif (bmi > 24.9) & (bmi < 29.9):
    print("Your BMI indicates overweight! I am not a doctor, but you should check that with one.")
elif bmi > 29.9:
    print("Your BMI is 30 or above, which indicates overweight! As a non-doctor I can only tell you to check it with a medic.")