student_dict = {
	"student": ["Chandler", "Joey", "Monica"],
	"score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
# 	print(value)

import pandas

student_data_frames = pandas.DataFrame(student_dict)

for (index, row) in student_data_frames.iterrows():
	print(row.student)