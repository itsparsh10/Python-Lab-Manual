class LU:
    def __init__(self, lu_code):
        self.lu_code = lu_code

    def display_info(self):
        print(f"LU Code: {self.lu_code}")

    def method(self):
        print("LU Work")

class ITM:
    def __init__(self, itm_code):
        self.itm_code = itm_code

    def display_info(self):
        print(f"ITM Code: {self.itm_code}")

    def method(self):
        print("ITM Work")

class DerivedClass(LU, ITM):
    def __init__(self, lu_code, itm_code, derived_code):
        super().__init__(lu_code)
        self.derived_code = derived_code

    def display_info(self):
        super(DerivedClass, self).display_info()
        print(f"Derived Code: {self.derived_code}")

    def method(self):
        super(DerivedClass, self).method()
        print("Derived Work")

derived_object = DerivedClass("LU1010", "ITM420", "DL11")

derived_object.display_info()
derived_object.method()
