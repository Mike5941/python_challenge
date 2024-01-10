from user_data import UserData

class CreateUser:

    def __init__(self):
        print("Welcome to Won Soong's Flight Club.")
        print("We find the best flight deals and email you.")

    def create_or_not(self):
        ask = input("Do you want to create an account? Y/N").upper()
        if ask == "Y":
            return True
        else:
            return False

    def ask_username(self):
        self.first_name = input("What is your first name?")
        self.last_name = input("What is your last name?")

    def ask_email(self):
        self.email = input("What is your email?")
        self.recheck_email = input("Type your email again")
        self.is_email_matched()

    def is_email_matched(self):
        if self.email != self.recheck_email:
            print("The email is not matched, try again")
            self.ask_email()
        else:
            print("You're in the club!")

    def create_userdata(self):
        user_data = UserData(self.first_name, self.last_name, self.email)
        return user_data

