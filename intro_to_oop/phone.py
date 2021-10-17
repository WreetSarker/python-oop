from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones=0):

        super().__init__(name, price, quantity)
        # Run validations on received arguments
        assert broken_phones >= 0, f"Quantity {broken_phones} can't be negative"

        # Assign to self object
        self.broken_phones = broken_phones
