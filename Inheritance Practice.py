class Myself:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address



class Activities(Myself):
    def __init__(self, name, age, address, uni_name, favourite_game):
        super().__init__(name, age, address)
        self.uni_name = uni_name
        self.favourite_game = favourite_game
        def details_info_myself(self):
            print(f"My name is {self.name}\nAge: {self.age}\nAddress: {self.address}")
        print(f"University Name: {uni_name}\nFavourite Sport: {favourite_game}")

    def feedback(self):
        print("He is a university student")

person1 = Activities("JIM", 24, "Ashulia Dhaka", "Daffodil International University", "Cricket")
person1.feedback()
person1.details_info_myself()  # Calling the method from the parent class
