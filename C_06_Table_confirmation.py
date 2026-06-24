#
# def table_confirmation():
#     while True:
#         print(recipie_string)
#         confirm_continue = yes_no("Does this table look correct? ")
#
#         if confirm_continue == "no":
#             # Ask the user which row is incorrect
#             incorrect_row = int_checker("What row is incorrect (🔎 HINT: Use the number at the beginning of the row. 🔍)? ")
#
#             # Asks the user for new data
#             name_change = input("New Name: ")
#             new_unit_value = quantity_checker(f"Please enter the new amount and unit of {name_change} that you require per batch: ")
#
#             # Updates data
#             required_resources[incorrect_row] = not_blank(name_change)
#             recipie_value[incorrect_row] = new_unit_value[0]
#             recipie_unit[incorrect_row] = new_unit_value[1]
#
#             # Update pandas
#             recipie_string = panda_frame_maker(recipie_dict)
#         else:
#             break