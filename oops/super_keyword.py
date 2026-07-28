class Employee:
    def __init__(self, name, address):
        self.name = name
        self. address = address
    def show_details(self):
        print(f"name:{self.name}, address: {self.address}")

class Developer(Employee):
    def __init__(self, name, address, language):
        self.language = language
        super().__init__(name,address)
    
    def show_details(self):
        print(f"language: {self.language}")
        super().show_details()

d1 = Developer("ram", "ktm", "pyhthon")
print(d1.name)
d1.show_details()