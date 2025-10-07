import operator as op

def choose_number():
    number_choosen = input("Choose a number: ")
    return number_choosen

def choose_operator():
    while _ == True:
        user_input = input("Enter the number of the operator choosen: ")

        print("""
            What operator do you want to use ?
            [1]: add
            [2]: substract
            [3]: multiply
            [4]: divide
            """)
        if user_input == float(user_input):
            _ = False

        else:
            print("Wrong input, please enter a number next time.")


    operator_choosen = input("Enter the number of the operator choosen: ")
    return operator_choosen

