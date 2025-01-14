# Description: This script creates a list and a dictionary with reversed elements based on user input.
# Tags: List, Dictionary

n = int(input("Въведете цяло число: "))

number_list = list(range(1, n + 1))

reversed_list = number_list[::-1]
result_dict = dict(zip(number_list, reversed_list))

print("Списък:", number_list)
print("Речник:", result_dict)
