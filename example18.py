student={
    "name":"Rahul",
    "usn":"1A23CS001",
    "marks":[85,75,90,65,86]
}

marks=student["marks"]
total=sum(marks)
average=total/len(marks)
print("Name:",student["name"])
print("USN:",student["usn"])
print("Total Marks:",total)
print("Average Marks:",average)

if average>=40:
    print("Result: Pass")
else:
    print("Result: Fail")
    