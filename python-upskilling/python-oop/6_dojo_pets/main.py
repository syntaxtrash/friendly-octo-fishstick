from ninja import Ninja
from pet import Dog, Cat

kurasbo = Dog("Kurasbo", ["Fetch", "Roll over"])

ninja_aaron = Ninja("Aaron", "Pogi", treats=5, pet_food=10, pet=kurasbo)

# Have the Ninja feed, walk , and bathe their pet.
ninja_aaron.feed()
ninja_aaron.walk()
ninja_aaron.bathe()
