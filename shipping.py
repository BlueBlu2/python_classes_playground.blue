import iso6346


class ShippingContainer:
    next_serial = 1020

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(owner_code=owner_code, serial= ShippingContainer._generate_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6),category="R")

c4 = ShippingContainer('hai', ["go"])
c5 = ShippingContainer('hia', ["go"])
r4 = RefrigeratedShippingContainer('hiw', ["go"])
r5 = RefrigeratedShippingContainer('hie', ["go"])
print(c4.bic)
print(c4.next_serial)
print(c5.bic)
print(c5.next_serial)
print(r4.bic)
print(r4.next_serial)
print(r5.bic)
print(r5.next_serial)

