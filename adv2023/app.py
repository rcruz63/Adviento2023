"""This is the main application file for the adv2023 package. """
from adv2023.dia1.dia1 import dia1_1, dia1_2
from adv2023.dia2.dia2 import dia2_1, dia2_2
from adv2023.dia3.dia3 import dia3_1, dia3_2
from adv2023.dia4.dia4 import dia4_1, dia4_2
from adv2023.dia5.dia52 import dia5_2
from adv2023.dia6.dia6 import dia6_1, dia6_2
from adv2023.dia7.dia7 import dia7_1, dia7_2
from adv2023.dia8.dia8 import dia8_1
from adv2023.dia9.dia9 import dia9_1
from adv2023.dia10.dia10 import dia10_1


def run():
    """This is the main function for the adv2023 package. """
    # Use a loop to keep representing a menu until the user chooses to exit
    while True:
        # Print the menu
        print("Welcome to the menu")
        print("1. Dia 1")
        print("2. Dia 2")
        print("3. Dia 3")
        print("4. Dia 4")
        print("5. Dia 5")
        print("6. Dia 6")
        print("7. Dia 7")
        print("8. Dia 8")
        print("9. Dia 9")
        print("10. Dia 10")
        print("Q. Exit")

        # Ask the user for a choice
        choice = input("What would you like to do? ")
        # If the user chooses option 1, call option1()
        if choice == "1":
            dia1_1("data1_1.txt")
            dia1_2("data1_2.txt")
        elif choice == "2":
            dia2_1("data2_1.txt", False)
            dia2_2("data2_2.txt", False)
        elif choice == "3":
            dia3_1("data3_1.txt", False)
            dia3_2("data3_2.txt", False)
        elif choice == "4":
            dia4_1("data4_1.txt", False)
            dia4_2("data4_2.txt", False)
        elif choice == "5":
            dia5_2("data5_1.txt", False)
        elif choice == "6":
            dia6_1("data6_1.txt", False)
            dia6_2("data6_1.txt", False)
        elif choice == "7":
            dia7_1("data7_1.txt", False)
            dia7_2("data7_1.txt", False)
        elif choice == "8":
            dia8_1(3, "data8_1.txt", False)
        elif choice == "9":
            dia9_1("data9_1.txt", False)
        elif choice == "10":
            dia10_1("data10_1.txt", False)
        # If the user chooses Q, exit the loop
        elif choice.upper() == "Q":
            break
        else:
            print("That is not a valid option")
