class Ninja:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, pirate):
        damage = self.calculate_damage()
        pirate.health -= damage
        print(f"{self.name} attacks {pirate.name} for {damage} damage!")
        return self

    def calculate_damage(self):
        return self.strength * 2

    @classmethod
    def from_master(cls, master_name):
        return cls(master_name + " Master")

    @staticmethod
    def battle_cry():
        return "For honor and glory!"
