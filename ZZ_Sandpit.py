# import re
# import random
#
# # Dictionaries
# # Mass (standard kg)
# mass_dictionary = {
#     "t": 1000,
#     "kg": 1,
#     "g": 0.001,
#     "mg": 0.000001,
# }
# # Volume (standard l)
# volume_dictionary = {
#     "l": 1,
#     "ml": 0.001,
# }
# # Distance (standard m)
# distance_dictionary = {
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01,
#     "mm": 0.001,
# }
#
# # Combine all dictionaries
# mega_dictionary = distance_dictionary | volume_dictionary | mass_dictionary
#
# for item in mass_dictionary:
#     print(item)
#
# test = "$45"
# to_strip = " "
# if test[0] == "$":
#     print("dollar amount")
#
#     to_strip += "$"
#     amount = test.strip(r"")
#     print(amount)
#
#
# else:
#     print("nay")
#
# print(test.strip(to_strip))
#
# a = "dskufhskfhjfisjfiojdxjfuioHIDjanijsfigjsilozgjsg"
# if "an" in a:
#     print("Pass")
#
# else:
#     print("Fail")
#
# inpt = "banana"
# letter = "a"
# unit_placement = f"{inpt[0] + inpt[1] + inpt[-1] + inpt[-2]}"
# print(unit_placement)
#
# amount_raw = inpt.strip(f"{unit_placement}")
# print(amount_raw)
#
# pattern = r"\d+"
# amount_raw = re.search(pattern, "123, fred")
# print(amount_raw.group())
#
# print(4**7%17)
#
# print(3.0)
#
# print(int(3.0))
#
# def function():
#
#     af = 0
#     bf = 0
#     for thing in range(0, 1):
#         af = random.randint(0, 10)
#         bf = random.randint(0, 10)
#
#     return af, bf
#
# rect = []
# for thingy in range(0, 3):
#     rect.append(function())
# print(rect)
# print(rect[0])
#
#
# print("=== string concatenation expt ====")
# num1 = 4
# num2 = 3
#
# print(str(num1 * num2) + " hello world ")
from operator import index
#
# test_list = ["a", "b", "c", "d", "e"]
# for item in test_list:
#     print(test_list[-test_list.index(item) -1])
# print(f"0/5 {0/5}")
# print(f"5/0 {5/0}")
#
# test_list = ["a", "b", "c"]
# for item in range(0, 2):
#     print(test_list[item])




