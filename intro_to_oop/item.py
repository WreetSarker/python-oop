import csv


class Item:
    pay_rate = 0.8  # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):

        # Run validations on received arguments
        assert price >= 0, f"Price {price} can't be negative"
        assert quantity >= 0, f"Quantity {quantity} can't be negative"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name too long")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("Price can't be negative")
        else:
            self.__price = value

    def calculate_price(self):
        return self.__price*self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count the floats that are point 0

        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
