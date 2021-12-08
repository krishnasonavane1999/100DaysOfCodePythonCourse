list1 = []
list2 = []
with open("file1.txt", "r") as file1:
  data = str(file1.read())
  data = data.split('\n')
  list1 = [int(n) for n in data if n.isnumeric() ]
  print(list1)
with open("file2.txt", "r") as file2:
  data = str(file2.read())
  data = data.split('\n')
  list2 = [int(n) for n in data if n.isnumeric() ]
  print(list2)

result = [n for n in list1 if n in list2]

# Write your code above 👆

print(result)


