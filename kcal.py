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
2- Cutting and lose weight
3- Staying in shape: """))
            if goal in [1, 2, 3]:
                return goal
            else:
                print("Invalid input. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number for goal.")

# Get user inputs with validations
name = input("Enter your name: ")
gender = get_valid_gender()
age = get_valid_age()
height = get_valid_height()
weight = get_valid_weight()
activity = get_valid_activity_level()
goal = get_valid_goal()

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

print(f"Okay {name}, your daily calories are {calories} kcal")

if goal == 1:
    meal(50, 30, 20)
    print(f"""For bulking, you should eat:
          Carbs: {carbs_calories} kcal or {carbs_grams} grams
          Protein: {protein_calories} kcal or {protein_grams} grams
          Fat: {fat_calories} kcal or {fat_grams} grams""")
elif goal == 2:
    meal(35, 40, 25)
    print(f"""For cutting and losing weight, you should eat:
          Carbs: {carbs_calories} kcal or {carbs_grams} grams
          Protein: {protein_calories} kcal or {protein_grams} grams
          Fat: {fat_calories} kcal or {fat_grams} grams""")
elif goal == 3:
    meal(50, 20, 30)
    print(f"""To stay in shape, you should eat:
          Carbs: {carbs_calories} kcal or {carbs_grams} grams
          Protein: {protein_calories} kcal or {protein_grams} grams
          Fat: {fat_calories} kcal or {fat_grams} grams""")
