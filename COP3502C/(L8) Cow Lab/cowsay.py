# cowsay.py
import sys
from heifer_generator import get_cows
from dragon import Dragon  # NEW: for isinstance check

def list_cows(cows):
    names = [cow.get_name() for cow in cows]
    print("Cows available:", " ".join(names))

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def print_message_and_image(message, cow):
    print(message)
    print(cow.get_image())
    # If it's a Dragon (includes IceDragon), print the fire-breathing line
    if isinstance(cow, Dragon):
        print()  # matches the blank line before the sentence in the sample
        if cow.can_breath_fire():
            print("This dragon can breathe fire.")
        else:
            print("This dragon cannot breathe fire.")

def main():
    cows = get_cows()
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage:")
        print("python cowsay.py -l")
        print("python cowsay.py MESSAGE")
        print("python cowsay.py -n COW MESSAGE")
        return

    if args[0] == "-l":
        list_cows(cows)
    elif args[0] == "-n":
        if len(args) < 3:
            print("Invalid input. Usage: python cowsay.py -n COW MESSAGE")
            return
        cow_name = args[1]
        message = " ".join(args[2:])
        cow = find_cow(cow_name, cows)
        if cow is None:
            print(f"Could not find {cow_name} cow!")
        else:
            print_message_and_image(message, cow)
    else:
        message = " ".join(args)
        # default to heifer
        cow = find_cow("heifer", cows)
        print_message_and_image(message, cow)

if __name__ == "__main__":
    main()
