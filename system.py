from account import Account
import workout

# The system class allows for account creating, log in, log out, as well as
# the ability to write to the account's workout data
class System:
    logged_in = False
    
    id = None
    username = None
    email = None
    workout_file = None
    

    # constructor for account object
    def create_account(self):
        if not self.logged_in:
            new_user = input("\tCreate a username: ")
            while Account.has_user_or_email(new_user):
                print("That username is already taken.")
                new_user = input("\tCreate a username: ")
                      
            new_password = input("\tCreate a password: ")
            
            new_email = input("\tEnter your email: ")
            while "@" not in new_email:
                print("Invalid email address, please try again.")
                new_email = input("\tEnter your email: ")

                if Account.has_user_or_email(new_email):
                    print("That email is already being used.")
                    new_email = input("\tEnter your email: ")

            Account(new_user, new_password, new_email)
            self.log_in(new_user, new_password)
                
        else:
            print("You must log out first.")

    # return true if log in information matches any account data
    def log_in(self, user, password):
        info = Account.check_info([user, password])
        if info is not False:
            self.logged_in = True
            self.id = info[0]
            self.username = info[1]
            self.email = info[3]
            self.workout_file = info[4]

    # set logged_in to false
    def log_out(self):
        if self.logged_in:
            self.logged_in = False
            self.id = None
            self.account = None
            self.email = None
            self.workout_file = None
            print("-Logged out-")
        else:
            print("No account is logged in.")

    # add a workout
    def enter_log(self):
        if self.logged_in:
            workout.log_workout(self.workout_file)
        else:
            print("You need to log in first.")

    # look up a workout
    def lookup_log(self):
        if self.logged_in:
            date = input("\tEnter a date (year-month-day): ")
            workout.display_log(self.workout_file, date)
        else:
            print("You need to log in first.")

    # accept user input
    def run_program(self):
        System.usage()
        user_input = ""

        while user_input != "exit":
            user_input = input("Enter a command: ")
            self.process_command(user_input)

    # display profile information
    def view_profile(self):

        if self.logged_in:
            print("\t" + self.username + ", " +self.email)
            Account.display_profile(self.workout_file)
        else:
            print("You need to log in first.")
        
    # read the input and perform the proper commands
    def process_command(self, command):
        parsed = command.split()

        if len(parsed) == 1:
            if command == "log":
                self.enter_log()
            elif command == "help":
                System.usage()
            elif command == "profile":
                self.view_profile();
                
            elif command == "lookup":
                self.lookup_log()
            elif command == "exit":
                print("-Program Terminated-")
            else:
                print("Command '" + command + "' not recognized, type 'help' for command options")
        elif len(parsed) == 2:
            if parsed[0] == "log" and parsed[1] == "in":
                username_attempt = input("\tEnter your username: ")
                password_attempt = input("\tEnter your password: ")
                self.log_in(username_attempt, password_attempt)
            elif parsed[0] == "log" and parsed[1] == "out":
                self.log_out()
            elif parsed[0] == "create" and parsed[1] == "account":
                self.create_account()
            else:
                print("Command '" + command + "' not recognized, type 'help' for command options")
        else:
            print("Command '" + command + "' not recognized, type 'help' for command options")
            

    # display the CLI options
    def usage():
        print("""
[COMMAND OPTIONS]
-create account
-log in
-log out
-log
-lookup
-profile
-exit
""")            

    # for testing
    def display_account(self):
        if self.logged_in:
            print(f"ID: {self.id}\nUsername: {self.username}\n\
Email: {self.email}\nFile: {self.workout_file}")
        else:
            print("You must log in first")

if __name__ == '__main__':
    # sponge_bob, krusty_krab, bikini_bottom@gmail.com
    # username_test, password_test, email_test@gmail.com
    program = System()
    program.run_program();
