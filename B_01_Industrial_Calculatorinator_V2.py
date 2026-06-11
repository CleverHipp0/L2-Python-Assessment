import re
import math
import pandas
from tabulate import tabulate

# Dictionaries
# Mass (standard kg)
mass_dict = {
    "g": 0.001,
    "t": 1000,
    "kg": 1,
    "mg": 0.000001,
}
# Volume (standard l)
volume_dict = {
    "l": 1,
    "ml": 0.001,
}
# Distance (standard m)
distance_dict = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
}

# Combine all dictionaries
mega_dictionary = distance_dict | volume_dict | mass_dict

def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no(inquiry):
    """An even simpler version of my original yes no checker. Asks a question and
    checks if the answer is yes or no."""

    # Error message
    error = "🚨 ERROR: This Field is required. Please enter a 'yes' or 'no' response. 🚨"

    # Repats the question like a pesky child until it is correctly answered.
    while True:
        response = input(inquiry).lower().strip()

        # Compares the answer to see whether it is a yes or no.
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        # If there is no match print an error.
        else:
            print(error)

def not_blank(inquiry):
    """Checks whether an answer is not blank."""

    # This repeats the inquiry until it is answered
    while True:
        element = input(inquiry)

        # Checks the length of the answer and outputs an error if it is too short.
        if len(element.strip()) > 0:
            return element
        else:
            print("🚨 ERROR: This Field is required. Please enter a response. 🚨")

def int_checker(question, int_float=int, exit_c=""):
    """Checks if a number is an integer or a float depending on the situation"""

    # Error message set up
    if int_float == int:
        error = "🚨 ERROR: Please enter an integer (whole number) more than zero. 🚨"
    else:
        error = "🚨 ERROR: Please enter a number more than zero. 🚨"


    while True:
        # Strips unnecessary character
        result = input(question).strip(r"\ ")

        # If the exit code is entered, exit.
        if result == exit_c and result != "":
            return result


        else:
            # Converts result to int or float if possible, else it prints an error.
            try:

                if int_float(result) > 0:
                    return int_float(result)
                else:
                    print(error)

            except ValueError:
                print(error)

def quantity_checker(inquiry, mode=None):
    """This will separate units from amounts and check for valid units."""
    # Sets up an error for units, floats and numbers.
    unit_error = "🚨 ERROR: This unit is not supported. Please enter a valid unit from this list. 🚨"
    float_error = "🚨 ERROR: No Number was entered. Make sure to enter a number. 🚨"
    number_error = "🚨 ERROR: Too Many Numbers were entered. Make sure there are no spaces between numbers. 🚨"

    # THIS WORKS DO NOT TOUCH
    # Finds the digits within the input.
    pattern = r"-?\d*\.?\d+"

    # Loops the input until all parameters are satisfied.
    while True:
        # Asks the user the question
        inpt = not_blank(inquiry).lower()

        # This is a list ⬇.
        amount_raw = re.findall(pattern, inpt)

        # Make sure there is a number entered.
        if len(amount_raw) == 1:
            amount = abs(float(amount_raw[0]))
            print(amount)

        # Number error if too many numbers are entered
        elif len(amount_raw) > 1:
            print(number_error)
            continue

        # If no number is entered print an error
        else:
            print(float_error)
            continue

        # Remove the value from the unit
        unit_raw = inpt.replace(str(amount_raw[0]), "").strip()

        # Allows "" to work while checking for a valid unit.
        if unit_raw == "" or unit_raw in mega_dictionary:
            unit = unit_raw

        # Error if no valid unit is entered
        else:
            print(unit_error)
            # Prints valid units
            for i in mega_dictionary:
              print(f" - {i}")
            continue

        # Formatting the output.
        if unit == "":
            print(f"You entered {amount} | Amount: {amount} | Unit: -")
        else:
            print(f"You entered {amount}{unit} | Amount: {amount} | Unit: {unit}")

        # Returning a float and a string
        return float(amount), unit

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None


# Main Routine.
# Generates the title as a string.
heading = statement_generator("Industrial Calculatorinator 2.0", "🏗️")
print(f"\n{heading}\n")

# Asks the user if they would like to skip the instructions.
skip_instructions = yes_no("Would you like to skip the instructions? ")
if skip_instructions == "n":
    print('''Instructions
blah
blah
blah
''')

# Asks the user how many products are in one batch. per_batch{int}
per_batch = int_checker("\nHow many products does one batch make? ")

# Asks the user how many products they would like to make. per_batch{int}
product_count = int_checker("How many products would you like to make? ")

# Calculates the multiplier to multiply the required resources by.
product_multiplier = product_count / per_batch

# Required resources:
# An empty list to append the required resources to.
required_resources = []

# Empty variable before loop to exit the loop is "" is entered.
exit_code = 1

# Spacer between the "how many products" question and the Part 1 header.
print()
# Small header for Part 1 of the program.
print(statement_generator("Part 1", "🎬"))

# Loop to ask how many required resources.
while exit_code != "":

    # Asks the user to enter the name of their required resources.
    print("\nPlease enter the name of your required resources. Press <enter> to continue.")
    required_resource_raw = input("ADD: ")

    # Makes sure that the user has entered more than 2 resources before continuing.
    if required_resource_raw == "" and len(required_resources) < 2:
        print("🚨 ERROR: You have not entered resources. Please enter more before continuing. 🚨")

    # Lets the user exit by leaving the field blank and pressing <enter>.
    elif required_resource_raw == "":
        exit_code = required_resource_raw
        print("Continuing...")

    # Lets the user know if they have a double up resource and won't enter it.
    elif required_resource_raw in required_resources:
        print(f"⚠️ CAUTION: You have already entered {required_resource_raw}. Note it will not be added again. ⚠️")

    # If everything checks out, adds the new resource to the required resource list.
    else:
        required_resources.append(required_resource_raw)


# Set up the list for the amount of resource needed per product. I need this to avoid errors. Tuples{No}. amount_per_product{int}
amount_per_product = []
# Set up the list for the unit of resource needed per product. I need this to avoid errors. Tuples{No}. required_resource{str}
required_resource_unit = []

# Looking for the amount of each resource required per product.
for resource in required_resources:

    # Asks how much of the resource is required per batch.
    print(f"\nHow much of {resource} do you need per batch?")

    # This is a list ⬇. amount{float} = [0], unit{str} = [1]. It finds the amount and unit for the resource per batch.
    resource_quantity_data = quantity_checker(f"AMOUNT: ")

    # This finds out how much of the resource is required for one product and adds it to the list. amount{float}/per_batch{int}
    amount_per_product.append(resource_quantity_data[0]/per_batch)
    # This finds out the unit of the resource needed and adds it to a list. unit{str}
    required_resource_unit.append(resource_quantity_data[1])

# Spacer between the "how much" question and the Part 2 header.
print()
# A simple header for Part 2 of the program.
print(statement_generator("Part 2", "🎬"))

# We need to find the







