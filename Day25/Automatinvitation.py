#accessing names
nameFile = "names.txt"
list_of_names = []
with open(nameFile, "r") as data:
	name_list = str(data.read())
	list_of_names =  name_list.split('\n')

# acessing the invitation template

for name in list_of_names:
	invitationTemplate = "invitation.txt"
	with open(invitationTemplate, "r") as data:
		invitation_content = data.read()

		invitation_content = invitation_content.replace("name", name)
	#	
	with open(f"invitation_to_{name}", "w") as invitation_letter:
		invitation_letter.write(invitation_content)


