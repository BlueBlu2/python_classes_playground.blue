class ShippingContainer:

    next_serial = 1020
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1



c4 = ShippingContainer('hi', ["go"])
c5 = ShippingContainer('hi', ["go"])
c6 = ShippingContainer('hi', ["go"])
c7 = ShippingContainer('hi', ["go"])
c9 = ShippingContainer('hi', ["go"])
print(c4.serial)
print(c4.next_serial)
print(c5.serial)
print(c5.next_serial)
print(c6.serial)
print(c6.next_serial)
print(c7.serial)
print(c7.next_serial)
print(c9.serial)
print(c9.next_serial)