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


def conversion_calculator(quantity_per_product, product_unit, resource):
    """This takes in the quantity per product and the first unit
    and converts it to the final unit that it asks for."""

    # Avoid errors.
    product_unit_dictionary = {}

    # Finds the dictionary to use.
    if product_unit in mass_dict:
        product_unit_dictionary = mass_dict

    elif product_unit in volume_dict:
        product_unit_dictionary = volume_dict

    elif product_unit in distance_dict:
        product_unit_dictionary = distance_dict

    # If the user doesn't enter a unit, let the function continue.
    elif product_unit == "":
        product_unit_dictionary = {}

    # Error if somehow the product unit is invalid. This should never be triggered.
    else:
        print(f"🚨 CODE ERROR - LINE 124: Product unit: {product_unit}, is not a valid unit. 🚨")

    # Loop until the user enters a valid answer for "What is the container size for {resource}? "
    while True:

        # Asks the user for the container size of the product
        print(f"What is the container size that {resource} is bought in? ")
        # This is a list ⬇. amount{float} = [0], unit{str} = [1]. It finds the amount and unit for the container size.
        container_size_data = quantity_checker("SIZE: ")

        # Separate container_size_data into value and unit.
        container_size_value = container_size_data[0]
        container_size_unit = container_size_data[1]


        # Makes sure that the container size unit is in the same dictionary as the product unit.
        if container_size_unit not in product_unit_dictionary and container_size_unit != product_unit:
            print(f"🚨 ERROR: The unit {container_size_unit} is not of the same unit type as {product_unit}. 🚨")
            continue

        # If the container size unit and the product unit are the same, skip the conversion.
        elif container_size_unit == product_unit:
            quantity_per_product_in_unit = product_unit
            print("Skipping conversion...")


        # This is a small status update.
        else:
            print("Converting...")

            # quantity_per_product -> container size unit. This does the conversion.
            # Converts the quantity per product to the standard unit (where one is in the dictionary).
            quantity_per_product_standard_unit = quantity_per_product * product_unit_dictionary[product_unit]
            # quantity_per_product{float} * product_unit_dictionary[container_size_unit{str}]{float}
            quantity_per_product_in_unit = quantity_per_product_standard_unit / product_unit_dictionary[container_size_unit]

            print(f"Quantity per product standard unit = {quantity_per_product_standard_unit} = {quantity_per_product} * {product_unit_dictionary[product_unit]} | product_unit = {product_unit}")
            print(f"Quantity per product in unit = {quantity_per_product_in_unit} = {quantity_per_product_standard_unit} / {product_unit_dictionary[container_size_unit]} | container_size_unit = {container_size_unit}")

        # Returns container_size_data {tuple (amount{float}, unit{str})} and quantity_per_product_in_unit{float}.
        return container_size_data, quantity_per_product_in_unit

    # Explict return none because of a weird error.
    return None

# Main routine
while True:

    test_resource = input("Resource: ")
    test_data = quantity_checker("Test Case: ")
    print(conversion_calculator(test_data[0], test_data[1], test_resource))