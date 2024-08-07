#Construct a dictionary from two lists:

students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}
print(student_subject_dict)
