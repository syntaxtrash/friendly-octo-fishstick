class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is taking {self.pet.name} for a walk.")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} is taking {self.pet.name} for a bath.")
        self.pet.noise()