import time
import random

def print_pause(text):
    print(text)
    time.sleep(1)

def get_valid_gender():
    while True:
        gender = input("Choose your gender by entering 'male' or 'female': ").strip().lower()
        if gender in ['male', 'female']:
            return gender
        print("Invalid input. Please enter 'male' or 'female'.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 1 <= age <= 120:
                return age
            else:
                print("Invalid input. Age must be between 1 and 120.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            if 30 <= height <= 300:
                return height
            else:
                print("Invalid input. Height must be between 30 and 300 cm.")
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if 1 <= weight <= 300:
                return weight
            else:
                print("Invalid input. Weight must be between 1 and 300 kg.")
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")

def get_valid_activity_level():
    while True:
        try:
            activity = int(input("""How active are you?
1- Sedentary (little or no exercise)
2- Lightly active (sports 1-3 days)
3- Moderately active (sports 3-5 days)
4- Very active (sports 6-7 days)
5- Super active (hard exercise/physical job): """))
            if activity in [1, 2, 3, 4, 5]:
                return activity
            else:
                print("Invalid input. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number for activity level.")

def get_valid_goal():
    while True:
        try:
            goal = int(input("""What is your goal?
1- Bulking
2- Cutting and losing weight
3- Staying in shape: """))
            if goal in [1, 2, 3]:
                return goal
            else:
                print("Invalid input. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number for goal.")

def get_valid_action():
    while True:
        try:
            action = int(input("""What do you want to do?
1- Heart rate monitor
2- Steps counter
3- Sleep tracker
4- Blood Oxygen level
5- Calories Calculator
6- Exit: """))
            print("")
            if action in [1, 2, 3, 4, 5, 6]:
                return action
            else:
                print("Invalid input. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number for action.")

def meal(carb_percent, protein_percent, fat_percent):
    global carbs_calories, carbs_grams
    global protein_calories, protein_grams
    global fat_calories, fat_grams
    carb_percent /= 100
    protein_percent /= 100
    fat_percent /= 100
    
    carbs_calories = round(carb_percent * calories, 1)
    protein_calories = round(protein_percent * calories, 1)
    fat_calories = round(fat_percent * calories, 1)

    carbs_grams = round(carbs_calories / 4, 1)
    protein_grams = round(protein_calories / 4, 1)
    fat_grams = round(fat_calories / 9, 1)

# Lists of sample data
heart_rates = [60, 72, 85, 90, 100, 110, 125, 130, 140, 150]
steps_counts = [3000, 5000, 7000, 9000, 10000, 12000, 15000]
sleep_hours = [4, 5, 6, 7, 8, 9, 10]
blood_oxygen_levels = [95, 96, 97, 98, 99, 100]

# Display the welcome message once
print_pause("Welcome to Galaxy Fitness")

# Get user inputs with validations
name = input("Enter your name: ")
print_pause("")
gender = get_valid_gender()
print_pause("")
age = get_valid_age()
print_pause("")
height = get_valid_height()
print_pause("")
weight = get_valid_weight()
print_pause("")
activity = get_valid_activity_level()
print_pause("")

# Calculate BMR and TDEE based on gender
if gender == "male":
    calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
elif gender == "female":
    calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

# Adjust calories based on activity level
activity_multipliers = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

calories *= activity_multipliers[activity]
calories = round(calories, 1)

# Main loop
while True:
    action = get_valid_action()

    if action == 1:
        heart_rate = random.choice(heart_rates)
        print_pause(f"Your heart rate is: {heart_rate} bpm")
    elif action == 2:
        steps = random.choice(steps_counts)
        print_pause(f"Your step count is: {steps} steps")
    elif action == 3:
        sleep = random.choice(sleep_hours)
        print_pause(f"Your sleep duration is: {sleep} hours")
    elif action == 4:
        oxygen_level = random.choice(blood_oxygen_levels)
        print_pause(f"Your blood oxygen level is: {oxygen_level}%")
    elif action == 5:
        print_pause(f"Okay {name}, your daily calories are {calories} kcal")
        print_pause("")
        goal = get_valid_goal()
        if goal == 1:
            print_pause("")
            meal(50, 30, 20)
            print_pause(f"""For bulking, you should eat:
                  Carbs: {carbs_calories} kcal or {carbs_grams} grams
                  Protein: {protein_calories} kcal or {protein_grams} grams
                  Fat: {fat_calories} kcal or {fat_grams} grams""")
        elif goal == 2:
            print_pause("")
            meal(35, 40, 25)
            print_pause(f"""For cutting and losing weight, you should eat:
                  Carbs: {carbs_calories} kcal or {carbs_grams} grams
                  Protein: {protein_calories} kcal or {protein_grams} grams
                  Fat: {fat_calories} kcal or {fat_grams} grams""")
        elif goal == 3:
            print_pause("")
            meal(50, 20, 30)
            print_pause(f"""To stay in shape, you should eat:
                  Carbs: {carbs_calories} kcal or {carbs_grams} grams
                  Protein: {protein_calories} kcal or {protein_grams} grams
                  Fat: {fat_calories} kcal or {fat_grams} grams""")
    elif action == 6:
        print_pause("Thank you for using Galaxy Fitness. Goodbye!")
        exit()

    # Option to continue or exit
    while True:
        print_pause("")
        choice = input("Would you like to perform another action or exit? Enter '1' for another action or '2' to exit: ").strip()
        print_pause("")
        if choice == '1':
            break
        elif choice == '2':
            print_pause("Thank you for using Galaxy Fitness. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter '1' or '2'.")
