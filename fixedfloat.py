class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    def __str__(self):
        return f'{self.amount:.2f}'

    # making this a classmothod instead of staticmethod will return an object of the same class as the 
    # one used to create it. Otherwise it will always be FixedFloat object. 
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1+value2)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

    def __str__(self):
        return f'{self.symbol}{self.amount:.2f}'


my_float = FixedFloat(12.33421)
print(my_float)

my_new_float = FixedFloat.from_sum(12.33312, 19.0344112)
print(my_new_float)

my_euro = Euro(14.44320)
print(my_euro)

money = Euro.from_sum(12.22201, 14.1333)
print(money)


