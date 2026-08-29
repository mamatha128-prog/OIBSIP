# ==========================================
# OIBSIP - Python Programming
# Task 2: BMI Calculator
# Beginner Tier
# ==========================================

def calculate_bmi():
    print("================================")
    print("       BMI CALCULATOR")
    print("================================")

    # Get weight
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))

            if weight <= 0:
                print("Error: Weight must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    # Get height
    while True:
        try:
            height = float(input("Enter your height (m): "))

            if height <= 0:
                print("Error: Height must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Display result
    print("\n================================")
    print("           BMI RESULT")
    print("================================")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    print("================================")


# Start the program
calculate_bmi()
