inventory={
    "laptop":5,
    "mouse":20,
    "keyboard":10,
    "monitor":7
}

product=input("enter the product:")
product=product.lower()
if product in inventory:
    print("available:",inventory[product])
else:
    print("product not available")