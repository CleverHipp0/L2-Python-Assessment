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

# Main routine
required_resources = []

# Loop
while True:

    # Asks the question to loop.
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


















