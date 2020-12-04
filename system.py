# runs the whole program
from account import Account
import fitness_app

class System:
    logged_in = False
    account = None

    def createAccount(self, username, password, email):
        return Account(username, password, email)

    def logIn(self, username, password):
        if Account.checkInfo([username, password]) is True:
            self.logged_in = True
            print(self.logged_in)
            account = username

    def logOut(self):
        logged_in = False
        print("Logged out")

    def enterLog(self):
        print(self.logged_in)
        if self.logged_in:
            while self.logged_in:
                fitness_app.LogWorkout(id) #asks for logs infinitely
        else:
            print("You need to log in first.")

if __name__ == '__main__':

    program = System()

    print(program.createAccount("username_test", "password_test", "email_test@gmail.com"))

    #fitness_app.DisplayData()
    #program.enterLog()
    program.logIn("test_dummy", "redLines123")
    program.enterLog()
