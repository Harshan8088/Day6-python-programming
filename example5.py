marks=[80,35,65,48,88]

print("Highest marks:",max(marks))
print("lowest marks:",min(marks))


# pass or fail count

marks=[80,35,72,28,65,40]

pass_count=0
fail_count=0

for mark in marks:
    if mark>=40:
        pass_count+=1
    else:
        fail_count+=1

print("pass count:",pass_count)
print("fail count:",fail_count)
        