import re

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

currency_dict = {
    "$": 1,
    "c": 0.01,
}

# Combine all dictionaries
mega_dictionary = distance_dict | volume_dict | mass_dict | currency_dict

def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}")

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

def quantity_checker(inquiry):
    """This will separate units from amounts and check for valid units."""

    # Blank to avoid error
    unit = 0

    # Sets up an error for units and floats.
    unit_error = "🚨 ERROR: This unit is not supported. Please enter a valid unit from this list. 🚨"
    float_error = "🚨 ERROR: No Number was entered. Make sure to enter a number. 🚨"
    number_error = "🚨 ERROR: Too Many Numbers were entered. Make sure there are no spaces between numbers. 🚨"

    # THIS WORKS DO NOT TOUCH
    # Finds the digits within the input.
    pattern = r"-?\d*\.?\d+"

    while True:
        # Asks the user the question
        inpt = not_blank(inquiry).lower()

        # This is a list. ⬇
        amount_raw = re.findall(pattern, inpt)

        # Make sure there is a number entered.
        if len(amount_raw) == 1:
            amount = abs(float(amount_raw[0]))
            print(amount)

        # Number error if too many numbers are entered
        elif len(amount_raw) > 1:
            print(number_error)
            continue

        else:
            print(float_error)
            continue

        # Number error if too many numbers are entered



        # Remove the value from the unit
        unit_raw = inpt.replace(str(amount_raw[0]), "").strip()

        # Lets no unit slide and checks for valid unit.
        if unit_raw == "" or unit_raw in mega_dictionary:
            unit = unit_raw

        else:
            print(unit_error)
            for item in mega_dictionary:
              print(f" - {item}")
            continue

        if unit == "$":
            print(f"You entered {unit}{amount} | Amount: {amount} | Unit: {unit}")

        elif unit == "":
            print(f"You entered {amount} | Amount: {amount} | Unit: -")
        else:
            print(f"You entered {amount}{unit} | Amount: {amount} | Unit: {unit}")

        return amount, unit

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None


# Main routine goes here.
print()
statement_generator("Industrial Calculatorinator", "🏗️")
print()

# Asks the user if the want to skip the instructions
want_instructions = yes_no("Would you like to skip the instructions? ")

if want_instructions == "no":
    statement_generator("Instructions", "ℹ️")
    print('''
- Blah
- Blah
- Blah
''')

# list of required resources
required_resources = []

# Start of recipie units and vales
recipie_unit = []
recipie_value = []

# Units and values that you buy in
purchase_unit = []
purchase_value = []



# Loop
while True:

    # Asks the question to loop.
    print()
    print("Please enter the resource or enter 'xxx' to quit.")
    new_resource = not_blank("ADD: ").lower().strip(r"\ ")

    # Makes sure they don't exit with less than one item entered.
    if new_resource == "xxx" and len(required_resources) < 2:
        print("🚨 ERROR: There are too few resources. Please enter 2 or more resources or quit. 🚨")
        continue

    # Exit code.
    elif new_resource == "xxx":
        break

    # Makes sure that there won't be a double up before entering.
    if new_resource not in required_resources:
        required_resources.append(new_resource)

    elif new_resource in required_resources:
        print(f"⚠️ CAUTION: You have already entered '{new_resource}'. It will not be added again. ⚠️")

for resource in required_resources:
    unit_value = quantity_checker(f"Please enter the amount and unit of {resource} that you require per batch: ")





































