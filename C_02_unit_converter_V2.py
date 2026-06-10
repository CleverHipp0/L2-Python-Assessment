import re

# Dictionaries
# Mass (standard kg)
mass_dict = {
    "t": 1000,
    "kg": 1,
    "g": 0.001,
    "mg": 0.000001,
}
# Volume (standard l)
volume_dict = {
    "l": 1,
    "ml": 0.001,
}
# Distance (standard m)
distance_dict = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
}

# Combine all dictionaries
mega_dictionary = distance_dict | volume_dict | mass_dict

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


def conversion_calculator(quantity_per_product, first_unit, resource):
    """This takes in the quantity per product and the first unit
    and converts it to the final unit that it asks for."""

    # Avoid errors.
    dictionary = {}

    # Finds the dictionary to use.
    if first_unit in mass_dict:
        dictionary = mass_dict

    elif first_unit in volume_dict:
        dictionary = volume_dict

    elif first_unit in distance_dict:
        dictionary = distance_dict

    # If the user doesn't enter a unit, let the function continue.
    elif first_unit == "":
        dictionary = ""

    # Error if somehow the first unit is invalid. This should never be triggered.
    else:
        print(f"🚨 CODE ERROR - LINE 124: First unit: {first_unit}, is not a valid unit. 🚨")

    # Loop until the user enters a valid answer for "What is the container size for {resource}? "
    while True:

        # Asks the user for the container size of the product
        print(f"What is the container size that {resource} is bought in? ")
        # This is a list ⬇. amount{float} = [0], unit{str} = [1]. It finds the amount and unit for the container size.
        container_size_data = quantity_checker("SIZE: ")

        # Separate container_size_data into

        # Makes sure both units are in the same dictionary.
        if final not in dictionary:
            print("Conversion Fail")
            continue

        else:
            print("Awesome")

        # Conversion amount.
        amount_a = abs(float(input("Number: ")))

        # Does the conversion.
        modifier = dictionary[initial] / dictionary[final]
        print(modifier)
        print(amount_a * modifier)
        print()


