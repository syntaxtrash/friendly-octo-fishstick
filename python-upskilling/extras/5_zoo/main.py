from animal import Lion, Tiger, Bear
from zoo import Zoo

def main():
    zoo1 = Zoo("Aaron's Zoo")
    zoo1.add_animal(Lion("Nala", 5))
    zoo1.add_animal(Lion("Simba", 4))
    zoo1.add_animal(Tiger("Rajah", 3))
    zoo1.add_animal(Tiger("Shere Khan", 6))
    zoo1.add_animal(Bear("Baloo", 8))

    zoo1.print_all_info()

if __name__ == "__main__":
    main()
