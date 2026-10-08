# update product stock

inventory={
    "laptop":5,
    "mouse":20,
    "keyboard":10,
}
product=input("enter the product:")
quantity=int(input("enter the quantity:"))
if product in inventory:
    inventory[product]=quantity
    print("stock updated")
else:
    print("product not available")

print(inventory)