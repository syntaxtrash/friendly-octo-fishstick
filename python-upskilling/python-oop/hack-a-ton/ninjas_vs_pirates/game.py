from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelangelo")
jack_sparrow = Pirate("Jack Sparrow")

# Battle until one's health is depleted
while michelangelo.health > 0 and jack_sparrow.health > 0:
    michelangelo.attack(jack_sparrow)
    if jack_sparrow.health <= 0:
        print(f"{jack_sparrow.name} has been defeated by {michelangelo.name}!")
        break
    jack_sparrow.show_stats()
    
    jack_sparrow.attack(michelangelo)
    if michelangelo.health <= 0:
        print(f"{michelangelo.name} has been defeated by {jack_sparrow.name}!")
        break
    michelangelo.show_stats()
