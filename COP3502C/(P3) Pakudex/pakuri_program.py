from pakudex import Pakudex

def pakudex_menu():
    print("""Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
""")
    choice_str = input("What would you like to do? ")
    try:
        return int(choice_str)
    except ValueError:
        return -1


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    # EXACT message required by autograder:
    while True:
        cap_str = input("Enter max capacity of the Pakudex: ")
        try:
            max_cap = int(cap_str)
            if max_cap > 0:
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")
    print(f"The Pakudex can hold {max_cap} species of Pakuri.\n")

    dex = Pakudex(max_cap)

    while True:
        choice = pakudex_menu()

        if choice == 1:
            species = dex.get_species_array()
            if species is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i, name in enumerate(species, start=1):
                    print(f"{i}. {name}")

        elif choice == 2:
            name = input("Enter the name of the species to display: ")
            stats = dex.get_stats(name)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                atk, df, spd = stats
                print(f"\nSpecies: {name}")
                print(f"Attack: {atk}")
                print(f"Defense: {df}")
                print(f"Speed: {spd}")

        elif choice == 3:
            # Check full BEFORE prompting for a name
            if dex.get_size() == dex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                name = input("Enter the name of the species to add: ")
                current = dex.get_species_array() or []
                if name in current:
                    print("Error: Pakudex already contains this species!")
                else:
                    if dex.add_pakuri(name):
                        print(f"Pakuri species {name} successfully added!")
                    else:
                        print("Error: Could not add Pakuri!")

        elif choice == 4:
            name = input("Enter the name of the species to evolve: ")
            if dex.evolve_species(name):
                print(f"{name} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == 5:
            dex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()
