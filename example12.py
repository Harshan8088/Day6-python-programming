# student profile

student={
    "name":"Rahul",
    "usn":"1A23CS001",
    "course":"CSE",
    "semester":3
}

print("name:",student["name"])
print("usn:",student["usn"])
print("course:",student["course"])
print("semester:",student["semester"])


# update student data

student={
    "name":"Rahul",
    "course":"CSE",
    "semester":3
}

student["semester"]=4
print(student)