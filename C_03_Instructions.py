# Functions go here
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


# Main Routine
# Loop for testing purposes
while True:
    want_instructions = yes_no("Would you like to skip the instructions? ")
    if want_instructions == "no":
        statement_generator("Instructions", "ℹ️")
        print('''
    - Blah
    - Blah
    - Blah
    ''')














