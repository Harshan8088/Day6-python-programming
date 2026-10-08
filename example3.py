# Adiing students

students=["Rahul","Pooja","Kiran"]

new_students=input("enter new students name:")

students.append(new_students)

print(students)


# removing students

students=["Rahul","Pooja","Kiran"]


name=input("enter the name:")


if name in students:
    students.remove(name)
    print("student removed")

else:
    print("no student found")

print(students)