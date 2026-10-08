cart={
    "LAPTOP":45000,
    "MOUSE":700,
    "KEYBOARD":1200
}

total=0

for product,price in cart.items():
    print(product,":",price)
    total+=price

print("-----------")
print("total price:",total)