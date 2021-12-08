numbers = [1, 2, 3]

new_list = [num + 1 for num in numbers]

print(numbers)
print(new_list)

name = "Krishna"

new_name = [ch for ch in name]

print(name)
print(new_name)


new_list = [num * 2 for num in range(1, 5)]

print(numbers)
print(new_list)

new_list = [num for num in range(1, 11) if num % 2 == 0]

print(numbers)
print(new_list)

names = ["Krishna", "Paras", "chandler", "joey"]

upper_case_list = [name.upper() for name in names]

print(names)
print(upper_case_list)