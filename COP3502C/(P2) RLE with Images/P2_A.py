import console_gfx

image_data = None
print("""
Welcome to the RLE image encoder!\n
Displaying Spectrum Image:""")
console_gfx.display_image(console_gfx.test_rainbow)

run_code = True
while run_code:
    print("")
    print("""RLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data\n""")

    user_input = int(input("Select a Menu Option:"))

    if user_input == 0:
        run_code = False
    elif user_input == 1:
        test_file = input("Enter name of file to load: ")
        image_data = console_gfx.load_file(test_file)
    elif user_input == 2:
        image_data = console_gfx.test_image
        print("Test image data loaded.")
    elif user_input == 6:
        console_gfx.display_image(image_data)



