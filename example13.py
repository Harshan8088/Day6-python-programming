# add new dictionary data

student={
    "name":"Rahul",
    "course":"CSE"
}

student["marks"]=85
print(student)

# dictionary loop

student={
    "name":"Rahul",
    "course":"CSE",
    "marks":85
}

for key, value in student.items():
    print(key,":",value)