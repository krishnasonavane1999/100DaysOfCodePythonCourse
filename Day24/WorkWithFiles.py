#opening and reading content from the file in read mode
with open("start.md", "r") as file:
	fileContent = file.read()
	print(fileContent)

# opening new file which is not exist in write mode only
# so it will create that file and write the content in tha file
with open("newstart.md", "w") as file:
	file.write("\n Hey, How you doin?")


# opening existing file in append mode and appending the content
with open("start.md", "a") as file:
	file.write("\nThis is appended content")