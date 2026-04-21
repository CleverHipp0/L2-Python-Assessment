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

numbers = "1234567890"

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

def quantity_checker(inquiry):
    """This will separate units from amounts and check for valid units."""

    # Blank to avoid error
    unit = 0

    # Sets up an error for units and floats.
    unit_error = "🚨 ERROR: This unit is not supported. Please enter a valid unit from this list. 🚨"
    float_error = "🚨 ERROR: No Number was entered. Make sure to enter a number. 🚨"

    # THIS WOKS DO NOT TOUCH
    # Finds the digits within the input.
    pattern = r"-?\d*\.?\d+"

    while True:
        # Asks the user the question
        inpt = not_blank(inquiry).lower()

        # This is a list. ⬇
        amount_raw = re.findall(pattern, inpt)

        # Make sure there is a number entered.
        if len(amount_raw) >= 1:
            amount = abs(float(amount_raw[0]))
            print(amount)

        else:
            # To fix errors of amount not existing later on
            print(float_error)
            continue

        # Remove the value from the unit
        unit_raw = inpt.replace(str(amount_raw[0]), "").strip()
        print(unit_raw)

        # Lets no unit slide and checks for valid unit.
        if unit_raw == "" or unit_raw in mega_dictionary:
            unit = unit_raw

        else:
            print(unit_error)
            continue

        return amount, unit

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None



while True:
    returned = quantity_checker("test: ")
    print(returned)