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
    negative_error = "🚨 ERROR: You entered a negative number. Please do not enter negative numbers. 🚨"


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
            amount = float(amount_raw[0])
            print(amount)

        # Number error if too many numbers are entered
        elif len(amount_raw) > 1:
            print(number_error)
            continue

        # If no number is entered print an error
        else:
            print(float_error)
            continue

        # Make sure that -ve numbers aren't entered
        if amount < 0:
            print(negative_error)
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











while True:
    returned = quantity_checker("test: ")
    print()