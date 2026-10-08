marks={
    "python":85,
    "java":78,
    "DBMS":90,
    "maths":75
}

total =sum(marks.values())
average=total/len(marks)

print("total:",total)
print("average:",average)
print("maximam",max(marks.values()))