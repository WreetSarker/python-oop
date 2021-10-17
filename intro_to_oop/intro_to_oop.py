from item import Item

item1 = Item("My Item", 750)
item1.price = 10
item1.apply_discount()
print(item1.price)
