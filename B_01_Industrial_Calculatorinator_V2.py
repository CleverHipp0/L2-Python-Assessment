import re
import math
import time
import pandas
from tabulate import tabulate
from tqdm import tqdm



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
        result = input(question).strip(r"$\ ")

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

def conversion_calculator(quantity_per_product, product_unit, thing):
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
        print(f"🚨 CODE ERROR - LINE 124: Product unit: {product_unit}, is not a valid unit. 🚨\n")

    # Loop until the user enters a valid answer for "What is the container size for {resource}? "
    while True:

        # Asks the user for the container size of the product
        print(f"\nWhat is the container size that {thing} is bought in? ")
        # This is a list ⬇. amount{float} = [0], unit{str} = [1]. It finds the amount and unit for the container size.
        container_size_data = quantity_checker("SIZE: ")

        # Separate container_size_data into value and unit.
        container_size_value = container_size_data[0]
        container_size_unit = container_size_data[1]


        # Makes sure that the container size unit is in the same dictionary as the product unit.
        if container_size_unit not in product_unit_dictionary and container_size_unit != product_unit:
            print(f"🚨 ERROR: The unit {container_size_unit} is not of the same unit type as {product_unit}. 🚨\n")
            continue

        # If the container size unit and the product unit are the same, skip the conversion.
        elif container_size_unit == product_unit:
            quantity_per_product_in_unit = quantity_per_product
            print("Skipping conversion...\n")


        # This is a small status update.
        else:
            print("Converting...\n")

            # quantity_per_product -> container size unit. This does the conversion.
            # Converts the quantity per product to the standard unit (where one is in the dictionary).
            quantity_per_product_standard_unit = quantity_per_product * product_unit_dictionary[product_unit]
            # quantity_per_product{float} * product_unit_dictionary[container_size_unit{str}]{float}
            quantity_per_product_in_unit = quantity_per_product_standard_unit / product_unit_dictionary[container_size_unit]

        # Returns container_size_data {tuple (amount{float}, unit{str})} and quantity_per_product_in_unit{float}.
        return container_size_data, quantity_per_product_in_unit

    # Explict return none because of a weird error.
    return None

def currency(value):
    return "${:.2f}".format(value)

def loading(dictionary_column):
    """Iterates through a column in a table with a loading bar and gets the sum of the column"""

    # Set up the variable so that there are no errors
    final_answer = 0
    # TQDM makes a nice loading bar
    for item_raw in tqdm(frame[dictionary_column]):
        item = item_raw.strip('$')
        final_answer += float(item)
        time.sleep(0.1)

    return final_answer

# Main Routine.
# Generates the title as a string.
heading = statement_generator("Industrial Calculatorinator 2.0", "🏗️")
print(f"\n{heading}\n")

# Asks the user if they would like to skip the instructions.
skip_instructions = yes_no("Would you like to skip the instructions? ")
if skip_instructions == "no":
    statement_generator("Instructions", "ℹ️")
    print('''
1. Enter how many products a singular batch makes.
This should be a positive number more than 0.

2. Enter how many PRODUCTS you want. NOT batches.

3. Enter the name of one of the resources.

4. Repeat step 3 for all of the resources you need.

5. Enter how much of the prompted resource that you need.

6. Repeat step 5 for all of the resources you need.

7. Enter the amount that you buy the resource in.

8. Enter the cost to buy the amount in step 7.

9. Repeat step 7-8 for all of the resources you need.

10. Choose if you want a simple or complex rundown.

11. Choose if you would like to write to file.

12. Have a good rest of your day!
''')

# Asks the user how many products are in one batch. per_batch{int}
per_batch = int_checker("\nHow many products does one batch make? ", float)

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
required_resource_amount = []
# Set up the list for the unit of resource needed per product. I need this to avoid errors. Tuples{No}. required_resource{str}
required_resource_unit = []
# Set up a list for the final panda that is both amount and unit together in  a string.
required_resource_amount_plus_unit = []


# Looking for the amount of each resource required per product.
for resource in required_resources:

    # Asks how much of the resource is required per batch.
    print(f"\nHow much of {resource} do you need per batch?")

    # This is a list ⬇. amount{float} = [0], unit{str} = [1]. It finds the amount and unit for the resource per batch.
    resource_quantity_data = quantity_checker(f"AMOUNT: ")

    # This finds out how much of the resource is required for one product and adds it to the list. amount{float}/per_batch{int}
    required_resource_amount.append(resource_quantity_data[0] / per_batch)
    # This finds out the unit of the resource needed and adds it to a list. unit{str}
    required_resource_unit.append(resource_quantity_data[1])
    # This adds the amount and unit together for a list for the panda
    required_resource_amount_plus_unit.append(f"{resource_quantity_data[0]}{resource_quantity_data[1]}")

# Spacer between the "how much" question and the Part 2 header.
print()
# A simple header for Part 2 of the program.
print(statement_generator("Part 2", "🎬"))



# Set up the lists for the next for item loop
buying_quantity = []
buying_unit = []
required_quantity_in_buying_unit = []
cost_per_container = []

# We need to find the container size and cost.
for resource in required_resources:
    # Finds the common index. Will find the index for the resource that it is up to in the lists.
    required_resource_index = required_resources.index(resource)
    # This is a list ⬇. tuple{(buying quantity{float} = [0], buying unit{str} = [1])}, required quantity in the buying unit{float}. Finds the buying quantities, buying unit, and required quantity in the buying unit.
    container_data = conversion_calculator(required_resource_amount[required_resource_index], required_resource_unit[required_resource_index], resource)

    # Separates the container data into buying quantity{float}, buying unit{str}, and required quantity in the buying unit{float}
    buying_quantity.append(container_data[0][0])
    buying_unit.append(container_data[0][1])
    required_quantity_in_buying_unit.append(container_data[1])

    # Asks the user how much it will cost per container of blah
    cost_per_container.append(int_checker(f"How much will it cost to buy {buying_quantity[required_resource_index]}{buying_unit[required_resource_index]} of {resource} (please enter answer in dollars)? ", float))
    print()


# Required resources.
# Amount and unit per batch.

# This is the list for the fraction of the buying quantity that the amount per product is.
cost_per_product = []
amount_you_will_need_to_use = []
cost_of_amount_you_will_need_to_use = []
need_to_buy = []
need_to_buy_string = []
cost_to_buy = []
required_resource_amount_plus_unit_per_product = []

for resource in required_resources:
    # Finds the common index. Will find the index for the resource that it is up to in the lists.
    required_resource_index = required_resources.index(resource)

    # Value of material per product.
    # This is the fraction of the buying quantity that the amount per product is.
    # required_resource_amount / buying_quantity = fraction_of_buying_quantity_per_product
    fraction_of_buying_quantity_per_product = required_quantity_in_buying_unit[required_resource_index] / buying_quantity[required_resource_index]

    # Finds out how much it costs for the material blah to make one product.
    cost_per_product.append(f"{currency(cost_per_container[required_resource_index] * fraction_of_buying_quantity_per_product)}")

    # Amount of material that the user will need to use.
    # This multiplies the amount of resources for one product by the amount of product wanted
    amount_you_will_need_to_use.append(f"{required_resource_amount[required_resource_index] * product_count}{required_resource_unit[required_resource_index]}")


    # Amount that the user will need to buy.
    # This finds out how much material the user will need to use in the unit that it is bought in.
    amount_you_will_need_to_use_in_unit = required_quantity_in_buying_unit[required_resource_index] * product_count

    # Finds out the cost of material you will need to use.
    fraction_of_buying_quantity_for_neet_to_use = amount_you_will_need_to_use_in_unit / buying_quantity[required_resource_index]
    cost_of_amount_you_will_need_to_use.append(f"{currency(cost_per_container[required_resource_index] * fraction_of_buying_quantity_for_neet_to_use)}")

    # This finds out the amount that the user will need to buy
    # by dividing that amount needed to be used by the buying quantity.
    need_to_buy.append(math.ceil(amount_you_will_need_to_use_in_unit / buying_quantity[required_resource_index]))
    # This converts the need_to_buy into a string for the dictionary so that I can change the format.
    need_to_buy_string.append(f"{math.ceil(amount_you_will_need_to_use_in_unit / buying_quantity[required_resource_index])} x {buying_quantity[required_resource_index]}{buying_unit[required_resource_index]}")

    # How much it will cost to buy all the materials.
    cost_to_buy.append(f"{currency(need_to_buy[required_resource_index] * cost_per_container[required_resource_index])}")

    # Flipping annoying thing because some egg (me) decided that units are important. Adds the unit back onto the required resource amount.
    required_resource_amount_plus_unit_per_product = f"{required_resource_amount[required_resource_index]}{required_resource_unit[required_resource_index]}"

# Dictionary for Panda
panda_dict = {
    'Resource': required_resources,
    'Amount Per Batch': required_resource_amount_plus_unit,
    'You will need\nto use\nfor 1 product': required_resource_amount_plus_unit_per_product,
    'Cost for materials\nfor 1 product': cost_per_product,
    f'Amount of material you\nwill need to use\nfor {product_count} product/s': amount_you_will_need_to_use,
    f'Cost of material for\n{product_count} product/s': cost_of_amount_you_will_need_to_use,
    'Amount of containers of\nmaterial that you will\nneed to buy': need_to_buy_string,
    'Cost to buy containers\nof material': cost_to_buy,
}

# Makes the Panda frame
frame = pandas.DataFrame(panda_dict)

# Asks the user if they want a simple or complex rundown
simple_complex = yes_no("Would you like a complex rundown of the data? ")

# Makes the panda frame a string
frame_string_complex = tabulate(frame, headers="keys", tablefmt="psql", showindex=False, colalign=("left", "right", "right", "right", "right", "right", "right"))


if simple_complex != "yes":
    # Makes the panda frame a string
    frame_string_simple = tabulate(frame[['Resource', f'Amount of material you\nwill need to use\nfor {product_count} product/s', f'Cost of material for\n{product_count} product/s', 'Amount of containers of\nmaterial that you will\nneed to buy']], headers="keys", tablefmt="psql", showindex=False, colalign=("left", "right", "right", "right", "right", "right", "right"))
    # Displays
    print(frame_string_simple)
else:
    # Displays
    print(frame_string_complex)

# Status update
print("Calculating...")

# Final stats
total_cost_one_product = loading('Cost for materials\nfor 1 product')
total_cost_of_material = loading(f'Cost of material for\n{product_count} product/s')
total_cost_to_buy = loading('Cost to buy containers\nof material')

print()
final_stats = [f"Total to buy all of the materials: ${total_cost_to_buy}", f"Total cost to make {product_count} product/s: ${total_cost_of_material}", f"Total cost to make 1 product: ${total_cost_one_product}"]
for stat in final_stats:
    print(stat)

like_to_write = yes_no("Would you like this written to file? ")

if like_to_write == "yes":
    final_stats.append(frame_string_complex)

    # Make the text file
    write_to = "{}.txt".format("Industrial_Calculatorinator_Write_File")
    # Open the text file
    text_file = open(write_to, "w+")

    for a in final_stats:
        text_file.write(a)
        text_file.write("\n")

print("Thank you for using the Industrial Calculatorinator!")