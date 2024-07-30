def calculator():
    # noinspection PyGlobalUndefined
    global result
    while True:
        print("Please choose an operation: ")
        print("1-addition")
        print("2-subtraction")
        print("3-multiplication")
        print("4-division")
        print("exit")
        choice = input("1, 2, 3, 4 or exit? ")
        if choice.lower() == "exit":
            break
        if choice in ["1", "2", "3", "4"]:
            try:
                first_number = float(input("Please enter the first number: "))
                second_number = float(input("Please enter the second number: "))
            except ValueError:
                print("Invalid Input!")
                continue

            if choice == "1":
                result = first_number + second_number
            elif choice == "2":
                result = first_number - second_number
            elif choice == "3":
                result = first_number * second_number
            elif choice == "4":
                if second_number == 0:
                    print("Invalid")
                    continue
                result = first_number / second_number
            print(result)


calculator()
