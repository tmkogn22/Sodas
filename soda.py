class Soda:
    def __init__(self, name, taste, color):
        self.name = name
        self.taste = taste
        self.color = color

    def display_info(self):
        print(self.name, "is:", self.taste, "taste, and", self.color, "color")


soda_one = Soda(name="Coca-Cola", taste="unique citrus, caramel and cola nut", color="dark brown")
soda_two = Soda(name="Fanta", taste="orange", color="orange")
soda_three = Soda(name="Sprite", taste="Lemon&Lime", color="clear")
soda_four = Soda(name="Dr Pepper", taste="cherry Cola", color="dark brown")
soda_five = Soda(name="Mountain Dew", taste="citrus", color="green")
soda_six = Soda(name="Just Soda", taste=" ", color="clear")


signal_exit = False
while not signal_exit:
    user_choice = str(input("Please, type name of soda you are interested in:"
                            "'Coca-Cola', 'Fanta', 'Sprite', 'Dr Pepper', 'Mountain Dew', 'Just Soda', or"
                            "if you want to exit, type 'exit': "))

    if user_choice == "Coca-Cola":
        if soda_one.taste != " ":
            soda_one.display_info()
        else:
            print(f"{soda_one.name} is {soda_one.color} color and regular sweet taste")
    elif user_choice == "Fanta":
        if soda_two.taste != " ":
            soda_two.display_info()
        else:
            print(f"{soda_two.name} is {soda_two.color} color and regular sweet taste")
    elif user_choice == "Sprite":
        if soda_three.taste != " ":
            soda_three.display_info()
        else:
            print(f"{soda_three.name} is {soda_three.color} color and regular sweet taste")
    elif user_choice == "Dr Pepper":
        if soda_four.taste != " ":
            soda_four.display_info()
        else:
            print(f"{soda_four.name} is {soda_four.color} color and regular sweet taste")
    elif user_choice == "Mountain Dew":
        if soda_five.taste != " ":
            soda_five.display_info()
        else:
            print(f"{soda_five.name} is {soda_five.color} color and regular sweet taste")
    elif user_choice == "Just Soda":
        if soda_six.taste != " ":
            soda_six.display_info()
        else:
            print(f"{soda_six.name} is {soda_six.color} color and regular sweet taste")
    elif user_choice == "exit":
        signal_exit = True
    else:
        print("Sorry, I don't understand. Type soda name from list: "
              "'Coca-Cola', 'Fanta', 'Sprite', 'Dr Pepper', 'Just Soda' or 'Mountain Dew'")
