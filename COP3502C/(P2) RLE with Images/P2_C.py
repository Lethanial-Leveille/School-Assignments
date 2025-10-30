import console_gfx

def to_hex_string(data):
    s = ''
    for num in data:
        s += format(num, 'x')
    return s

def count_runs(flat_data):
    count = 1
    run = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1] and run < 15:
            run += 1
        else:
            run = 1
            count += 1
    return count

def encode_rle(flat_data):
    encoded = []
    run = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1] and run < 15:
            run += 1
        else:
            encoded += [run, flat_data[i - 1]]
            run = 1
    encoded += [run, flat_data[-1]]
    return encoded

def get_decoded_length(rle_data):
    total = 0
    for i in range(0, len(rle_data), 2):
        total += rle_data[i]
    return total

def decode_rle(rle_data):
    decoded = []
    for i in range(0, len(rle_data), 2):
        decoded += [rle_data[i + 1]] * rle_data[i]
    return decoded

def string_to_data(data_string):
    data = []
    for ch in data_string:
        data.append(int(ch, 16))
    return data

def to_rle_string(rle_data):
    s = ''
    for i in range(0, len(rle_data), 2):
        s += str(rle_data[i]) + format(rle_data[i + 1], 'x')
        if i + 2 < len(rle_data):
            s += ':'
    return s

def string_to_rle(rle_string):
    parts = rle_string.split(':')
    rle = []
    for p in parts:
        val = int(p[-1], 16)
        run = int(p[:-1])
        rle += [run, val]
    return rle

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    image_data = []
    while True:
        print()
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        choice = input("\nSelect a Menu Option: ")
        print()
        if choice == '0':
            break
        elif choice == '1':
            name = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(name)
            print("File loaded.")
        elif choice == '2':
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif choice == '3':
            rle_str = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(rle_str))
        elif choice == '4':
            rle_hex = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(rle_hex))
        elif choice == '5':
            flat_hex = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex)
        elif choice == '6':
            print("Displaying image...")
            console_gfx.display_image(image_data)
        elif choice == '7':
            print("RLE representation:", to_rle_string(encode_rle(image_data)))
        elif choice == '8':
            print("RLE hex values:", to_hex_string(encode_rle(image_data)))
        elif choice == '9':
            print("Flat hex values:", to_hex_string(image_data))

if __name__ == "__main__":
    main()

