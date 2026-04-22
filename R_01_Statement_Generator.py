# Functions go here
def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}")



# Main Routine goes here
statement_generator("Cameron is Awesome!", "😎")
