import math
calculator_menu = '''Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
'''
current_result = 0.0
calc_sum = 0
calc_cnt = 0
last_result = 0
run_calculator = True
print(f"Current Result: {current_result}\n")
print(calculator_menu)
while run_calculator:
    menu_selection = int(input("Enter Menu Selection: "))
    if menu_selection == 0:
        print("Thanks for using this calculator. Goodbye!")
        run_calculator = False
    elif menu_selection == 1:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = float(first_op) + float(sec_op)
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 2:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = float(first_op) - float(sec_op)
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 3:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = float(first_op) * float(sec_op)
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 4:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = float(first_op) / float(sec_op)
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 5:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = float(first_op) ** float(sec_op)
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 6:
        first_op = input("Enter first operand: ")
        if first_op == "RESULT":
            first_op = last_result
        sec_op = input("Enter second operand: ")
        if sec_op == "RESULT":
            sec_op = last_result
        current_result = math.log(float(sec_op),float(first_op))
        print(f"Current Result: {current_result}\n")
        calc_sum += current_result
        calc_cnt += 1
        last_result = current_result
        print(calculator_menu)
    elif menu_selection == 7:
        if calc_cnt == 0:
            print("Error: No calculations yet to average!\n")
        else:
            print(f"Sum of calculations: {float(calc_sum)}")
            print(f"Number of calculations: {calc_cnt}")
            print(f"Average of calculations: {round(calc_sum / calc_cnt,2)}\n")
    else:
        print("Error: Invalid selection!\n")