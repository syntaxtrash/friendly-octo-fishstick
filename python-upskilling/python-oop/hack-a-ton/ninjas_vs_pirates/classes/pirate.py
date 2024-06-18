class Pirate:
    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, ninja):
        damage = self.calculate_damage()
        ninja.health -= damage
        print(f"{self.name} attacks {ninja.name} for {damage} damage!")
        return self

    def calculate_damage(self):
        return self.strength * 2

    @classmethod
    def from_captain(cls, captain_name):
        return cls(captain_name + " Captain")

    @staticmethod
    def pirate_anthem():
        return "Yo ho ho and a bottle of rum!"
