class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.energy += 25

    def eat(self):
        print(f"{self.name} is eating.")
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print(f"{self.name} makes a noise!")


class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, type="Dog", tricks=tricks)

    def bark(self):
        print(f"{self.name} barks!")


class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, type="Cat", tricks=tricks)

    def meow(self):
        print(f"{self.name} meows!")
