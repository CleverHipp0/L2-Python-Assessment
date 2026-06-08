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

currency_dict = {
    "$": 1,
    "c": 0.01,
}

# Combine all dictionaries
mega_dictionary = distance_dict | volume_dict | mass_dict

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

def int_checker(question, int_float=int, exit_code=""):
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
        if result == exit_code and result != "":
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

    # Select mode
    if mode == "$":
        used_dictionary = currency_dict
    else:
        used_dictionary = mega_dictionary

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
        if unit_raw == "" or unit_raw in used_dictionary:
            unit = unit_raw

        else:
            print(unit_error)
            for i in used_dictionary:
              print(f" - {i}")
            continue

        if unit == "$":
            print(f"You entered {unit}{amount} | Amount: {amount} | Unit: {unit}")

        elif unit == "":
            print(f"You entered {amount} | Amount: {amount} | Unit: -")
        else:
            print(f"You entered {amount}{unit} | Amount: {amount} | Unit: {unit}")

        return float(amount), unit

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None

def panda_frame_maker(dictionary, mode=None):
    """Generates a panda frame"""
    # Pandas Data frame
    frame = pandas.DataFrame(dictionary)

    if mode == "recipie":
        # Add total amount needed for all batches.
        frame['Batch Amount'] = frame['Amount'] * batch_count

    frame_string = tabulate(frame, headers="keys", tablefmt="psql")

    return frame_string

def table_confirmation(value, unit, table, mode="recipie"):
    """Confirms you have entered all items into the table correctly"""
    print(table)
    confirm_continue = yes_no("Does this table look correct? ")

    if confirm_continue == "no":
        # Ask the user which row is incorrect
        incorrect_row = int_checker("What row is incorrect (🔎 HINT: Use the number at the beginning of the row. 🔍)? ")



        if mode == "recipie":
            # Asks the user for new data
            name_change = input("New Name: ")
            new_unit_value = quantity_checker(f"Please enter the new amount and unit of {name_change} that you require per batch: ")
            required_resources[incorrect_row] = not_blank(name_change)
        else:
            new_unit_value_raw = unit_converter(unit, value)
            new_unit_value = new_unit_value_raw[1]

        # Updates data
        value[incorrect_row] = new_unit_value[0]
        unit[incorrect_row] = new_unit_value[1]
        return value, unit

    # if nothing needs to be changed exit code.
    else:
        return "xxx"


def unit_converter(original_unit, original_amount):
    """Converts from one unit to another"""
    while True:
        # Avoid errors.
        dictionary = {}
        standard_unit_original = 1
        standard_unit_final = 1
        mission_impossible_name_variable = 0

        # Finds the dictionary to use.
        if original_unit in mass_dict:
            dictionary = mass_dict

        elif original_unit in volume_dict:
            dictionary = volume_dict

        elif original_unit in distance_dict:
            dictionary = distance_dict

        elif original_unit in currency_dict:
            dictionary = currency_dict

        else:
            dictionary = [""]

        final = quantity_checker(f"Container size (eg. Flour is bought in 1.5kg bags so you would enter 1.5kg): ")

        # Makes sure both units are in the same dictionary.
        if final[1] not in dictionary and final[1] != "":
            print("Conversion Fail")
            continue
        elif final[1] == "":
            modifier = 1

        else:
            # Finds out how much it will cost
            standard_unit_original = original_amount / dictionary[original_unit]
            standard_unit_final = final[0] / dictionary[final[1]]

            mission_impossible_name_variable = standard_unit_original/standard_unit_final
            print(f"{standard_unit_original}/{standard_unit_final} = {mission_impossible_name_variable}")
            # Does the conversion.
            modifier = dictionary[final[1]]

        return standard_unit_original * modifier, final, mission_impossible_name_variable

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None


# Main routine goes here.
# Title
print()
statement_generator("Industrial Calculatorinator", "🏗️")
print()

# Instructions
# Asks the user if the want to skip the instructions
want_instructions = yes_no("Would you like to skip the instructions? ")

if want_instructions == "no":
    statement_generator("Instructions", "ℹ️")
    print('''
- Blah
- Blah
- Blah
''')


# Batch Total, product name, how many batches
product_name = input("What is the name of the product? ")
per_batch = int_checker("How many does a batch make? ", float)
# Replace this with an amount wanted??
number_of_items = int_checker(f"How many would you like to make (NOT batches)? ", float)

batch_count = number_of_items/per_batch

# Set up
# list of required resources
required_resources = []

# Avoid errors
# List of 1 container worth of blah
quantity_cost = []
# Amount of resource needed for 1 blah
need_to_use = []
# Cost to make one portion of blah
cost_per_product = []
# This is a tuple
buying_quantity = []
# How many containers of blah needed
need_to_buy = []
resource_buying_cost = []
number_to_buy = []
buying_standard_unit = []
amount_in_unit = []

# Change this name please please please
the_bane_of_my_existence = []

# Start of recipie units and vales
recipie_unit = []
recipie_value = []

recipie_dict = {
    "Resource": required_resources,
    "Amount": recipie_value,
    "Unit": recipie_unit,
}


# Units and values that you buy in
purchase_unit = []
purchase_value = []



# Loop getting the recipe resources.
while True:

    # Asks the user the question to loop.
    print("\nPlease enter the resource or enter 'xxx' to continue.")
    new_resource = not_blank("ADD: ").strip(r"\ ")

    # Makes sure they don't exit with less than one item entered.
    if new_resource == "xxx" and len(required_resources) < 2:
        print("🚨 ERROR: There are too few resources. Please enter 2 or more resources. 🚨")
        continue

    # Exit code.
    elif new_resource == "xxx":
        break

    # Makes sure that there won't be a double up before entering.
    if new_resource not in required_resources:
        required_resources.append(new_resource)

    # Takes care of double ups.
    elif new_resource in required_resources:
        print(f"⚠️ CAUTION: You have already entered '{new_resource}'. It will not be added again. ⚠️")

# Asks the user how much of each resource is required
for resource in required_resources:

    # Quantity checks gets unit + value
    unit_value = quantity_checker(f"\nPlease enter the amount and unit of {resource} that you require per batch: ")

    # Adds it to lists for pandas
    recipie_value.append(unit_value[0])
    recipie_unit.append(unit_value[1])

# Pandas Data frame
recipie_string = panda_frame_maker(recipie_dict, "recipie")

# Confirm table 1
while True:
    new_recipie_data = table_confirmation(recipie_value, recipie_unit, recipie_string)

    # Exit if nothing is wrong
    if new_recipie_data == "xxx":
        break

    else:
        recipie_value = new_recipie_data[0]
        recipie_unit = new_recipie_data[1]

        recipie_string = panda_frame_maker(recipie_dict, "recipie")


# Figure out costs and economical adult things to do with money and taxes
for item in required_resources:



    # Unit conversion to accurately buy the correct amount
    converter_data = unit_converter(recipie_unit[required_resources.index(item)], recipie_value[required_resources.index(item)])
    amount_in_unit.append(converter_data[0])

    # Container size
    buying_quantity.append(converter_data[1])

    # I know what this does (standard o/ standard f) but idk a name
    the_bane_of_my_existence.append(converter_data[2])

    # cost per container
    quantity_cost_raw = quantity_checker(f"How much does it cost to buy 1 container of {item} including GST (please add a $ or c for units)? ", "$")
    quantity_cost.append(quantity_cost_raw[0])

product_dict = {
    "required resource": required_resources,
    "quantity bought in": buying_quantity,
    "cost per container": quantity_cost,
}

product_string = panda_frame_maker(product_dict)

# Confirm table 2
while True:
    new_recipie_data = table_confirmation(buying_quantity, recipie_unit, product_string)

    # Exit if nothing is wrong
    if new_recipie_data == "xxx":
        break

    else:
        recipie_value = new_recipie_data[0]
        recipie_unit = new_recipie_data[1]

        product_string = panda_frame_maker(recipie_dict)

# Super PANDA
# To avoid errors
recipie_amount_plus_unit = []
product_amount = []


# Adds the unit and amount together
for resource in required_resources:
    resource_index = required_resources.index(resource)

    recipie_amount_plus_unit.append(str(recipie_value[resource_index]) + recipie_unit[resource_index])

    # Value for one batch
    print()
    product_amount_raw = recipie_value[resource_index] / per_batch
    print(f"Product Amount Raw: {recipie_value[resource_index]} / {per_batch} = {product_amount_raw}")
    cost_per_product.append(the_bane_of_my_existence[resource_index] * quantity_cost[resource_index])
    print(f"Cost per product: ({the_bane_of_my_existence}) x {quantity_cost[resource_index]}")

    # Calculate how much is needed tobe used
    need_to_use_raw = recipie_value[resource_index] * batch_count
    need_to_use.append(str(need_to_use_raw) + recipie_unit[resource_index])

    print(f"Number to buy: {recipie_value[resource_index]} / {per_batch * recipie_value[resource_index]} = {math.ceil(recipie_value[resource_index] / (per_batch * recipie_value[resource_index]))}")
    number_to_buy.append(math.ceil(recipie_value[resource_index] / (per_batch * recipie_value[resource_index])))


    buying_quantity_reversed = list(reversed(buying_quantity))
    need_to_buy.append(f"{number_to_buy[resource_index]} x {buying_quantity_reversed[resource_index][0]}{buying_quantity_reversed[resource_index][1]}")
    print(number_to_buy)

    resource_buying_cost.append(f"{number_to_buy[resource_index]} x ${list(reversed(quantity_cost))[resource_index]}")


# Dictionary for panda
super_panda_dictionary = {
    "Required Resource": required_resources,
    "Amount/Batch": recipie_amount_plus_unit,
    "Value of material used to make one product": cost_per_product,
    "You will need to use": need_to_use,
    "You will need to buy": list(reversed(need_to_buy)),
    "How much it will cost to buy all of the resources": list(reversed(resource_buying_cost)),
}

super_panda_string = panda_frame_maker(super_panda_dictionary)
print(super_panda_string)



















