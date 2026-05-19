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
currency_dict = {
    "$": 1,
    "c": 0.01,
}

# Combine all dictionaries
mega_dictionary = distance_dict | volume_dict | mass_dict | currency_dict
def unit_converter(original_unit):
    while True:
        # Avoid errors.
        dictionary = {}

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


        final = input("Final: ").lower()

        # Makes sure both units are in the same dictionary.
        if final not in dictionary:
            print("Conversion Fail")
            continue

        else:
            print("Awesome")

        # Conversion amount.
        amount_a = abs(float(input("Number: ")))

        # Does the conversion.
        modifier = dictionary[original_unit] / dictionary[final]

        return amount_a * modifier

    # explicit return statement to avoid PEP8 error when we use 'continue' in the else statement above.
    return None


