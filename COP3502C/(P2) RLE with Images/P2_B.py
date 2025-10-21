import console_gfx


# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def to_hex_string(data):
    """Return lowercase hex string representing a list of 0–15 values."""
    result = ""
    for n in data:
        result += format(n, "x")
    return result


def string_to_data(data_string):
    """Return list of ints from a hex string."""
    result = []
    for ch in data_string:
        result.append(int(ch, 16))
    return result


def count_runs(flat_data):
    """Return number of runs in the flat data (no run longer than 15)."""
    if not flat_data:
        return 0

    runs = 1
    current = flat_data[0]
    length = 1

    for val in flat_data[1:]:
        if val == current and length < 15:
            length += 1
        else:
            runs += 1
            current = val
            length = 1
    return runs


def encode_rle(flat_data):
    """Return RLE list [len,val,len,val,…] representing flat data."""
    if not flat_data:
        return []

    encoded = []
    current = flat_data[0]
    length = 1

    for val in flat_data[1:]:
        if val == current and length < 15:
            length += 1
        else:
            encoded.extend([length, current])
            current = val
            length = 1
    encoded.extend([length, current])
    return encoded


def get_decoded_length(rle_data):
    """Return number of pixels represented by RLE data."""
    total = 0
    for i in range(0, len(rle_data), 2):
        total += rle_data[i]
    return total


def decode_rle(rle_data):
    """Return flat data list decoded from RLE data."""
    decoded = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i + 1]
        decoded.extend([value] * count)
    return decoded


def to_rle_string(rle_data):
    """Return human-readable RLE string such as '15f:64'."""
    parts = []
    for i in range(0, len(rle_data), 2):
        run_len = str(rle_data[i])
        value_hex = format(rle_data[i + 1], "x")
        parts.append(run_len + value_hex)
    return ":".join(parts)


def string_to_rle(rle_string):
    """Return RLE list converted from string like '15f:64'."""
    if not rle_string:
        return []
    result = []
    runs = rle_string.split(":")
    for run in runs:
        run_len = int(run[:-1])
        value = int(run[-1], 16)
        result.extend([run_len, value])
    return result


# ------------------------------------------------------------
# Stand-alone driver (menu)
# ------------------------------------------------------------

def main():
    image_data = None
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    while True:
        print()
        print("""RLE Menu
---------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data""")

        choice = input("Select a Menu Option: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)
            print("Image file loaded.")

        elif choice == "2":
            image_data = console_gfx.test_image
            print("Test image data loaded.")

        elif choice == "3":
            rle_string = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_string))
            print("RLE string decoded and image loaded.")

        elif choice == "4":
            rle_hex = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex))
            print("RLE hex string decoded and image loaded.")

        elif choice == "5":
            flat_hex = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex)
            print("Flat data loaded.")

        elif choice == "6":
            if image_data is None:
                print("No image loaded.")
            else:
                console_gfx.display_image(image_data)

        else:
            print("Feature not implemented yet.")


# ------------------------------------------------------------
if __name__ == "__main__":
    main()




