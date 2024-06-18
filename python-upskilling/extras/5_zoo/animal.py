class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)
        self.roar_level = 5

    def roar(self):
        print("ROAARRR!")

    def feed(self):
        super().feed()
        self.roar_level += 2


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=95, happiness=85)
        self.stripe_count = 50

    def purr(self):
        print("Purrr...")

    def feed(self):
        super().feed()
        self.stripe_count += 5


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=85, happiness=90)
        self.fish_eaten = 0

    def fish(self):
        print("I love fish!")

    def feed(self):
        super().feed()
        self.fish_eaten += 1
