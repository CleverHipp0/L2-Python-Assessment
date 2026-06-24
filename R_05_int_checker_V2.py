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
                    return result
                else:
                    print(error)

            except ValueError:
                print(error)

# Main routine
print(int_checker("Number to check: ", float, ""))

