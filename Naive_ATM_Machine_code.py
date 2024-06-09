class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
    Hi, How can i help you?
    1.Press 1 to create pin
    2.Press 2 to change pin
    3.press 3 to check balance
    4.press 4 to withdraw
    5. exit

    """)

        if user_input == '1':
            self.createpin()


        elif user_input == '2':
            self.changepin()

        elif user_input == '3':
            self.checkbalance()

        elif user_input == '4':
            self.Withdraw()

        else:
            exit()

    def createpin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin

        user_balance = int(input("enter you balance"))
        self.balance = user_balance
        self.menu()

    def changepin(self):
        old_pin = input("enter your pin")
        if old_pin == self.pin:
            new_pin = input("ente your new pin")
            self.pin = new_pin
            print("Pin changed successfully")
            self.menu()

        else:
            print("incorrect pin")
            self.menu()

    def checkbalance(self):
        user_pin = input("enter your pin")
        if user_pin == self.pin:
            print("your balance is :", self.balance)
            self.menu()

        else:
            print("incorrect pin")
            self.menu()

    def Withdraw(self):
        user_pin = input("enter your pin")
        if user_pin == self.pin:
            new_balance = int(input("enter the amount you want to withdraw"))
            if self.balance > new_balance:

                self.balance = self.balance - new_balance
                print("your balance is :", self.balance)

            else:
                print("Insufficient balance")
            self.menu()


        else:
            print("incorrect pin")
            self.menu()
obj=Atm()




