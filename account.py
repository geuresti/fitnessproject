import cryptography
from cryptography.fernet import Fernet

# the Account class allows for the creationg of accounts, storing account
# information to a file, assigning an id, and password encrytion/decryption
class Account:
    # ID = 0
    # USERNAME = 1
    # PASSWORD = 2
    # EMAIL = 3
    # FILE = 4

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.id = Account.id_account()
        self.workout_file = self.username + str(self.id) + ".txt"

        # UNCOMMENT LINES BELOW WHEN ADDING NEW ACCOUNTS

        file = open(self.workout_file, "w")
        file.write("weight:,calories bulk:,calories cut:,calories maintenance:,")
        file.close()

        self.store_info(password)

    # check if there is already an account with the inputted username / email
    def has_user_or_email(info):
        file = open("account_data.txt", "r")

        if "@" in info:
            index = 3
        else:
            index = 1
            
        for line in file:
            line = line.split("|")
            if line[index] == info:
                return True
        return False
        
    # assigns an Account an id based on their line number, starts at 1
    def id_account():
        id = 1
        f = open("account_data.txt", "r")
        for line in f:
            id += 1
        return id

    # writes the account information to a text file. password is passed as
    # an argument so there isn't a password directly associated with
    # an Account object instance (the unencrypted password is unable to be looked up)
    def store_info(self, password):
        f = open("account_data.txt", "a")
        pswrd = Account.encrypt_password(password)
        print(f"{self.id}|{self.username}|{pswrd}|{self.email}|{self.workout_file}", file=f)
        f.close()
        
    # uses the encrypt_key.key file to encrypt a String argument
    def encrypt_password(msg):
        file = open('encrypt_key.key', 'rb')
        key = file.read()
        file.close()

        f = Fernet(key)
        message = msg.encode()
        encrypted_message = f.encrypt(message)

        return encrypted_message

    # takes an encrypted string and returns the its decrypted value
    def decrypt_password(msg):
        file = open('encrypt_key.key', 'rb')
        key = file.read()
        file.close()

        f = Fernet(key)
        decrypted_password = f.decrypt(msg)

        return decrypted_password

    def display_profile(workout_file):
        file = open(workout_file, "r")
        info = file.readline().split(",")
        for data in info:
            print(data)

    # *refactor*
    # compares the username and password (as a list) to information in the
    # account data text file, returns true if there is a match
    @classmethod
    def check_info(cls, info):
        f = open("account_data.txt", "r")
        for line in f:
            data = line.split("|")
            # this line orignally had data[2]
            data[4] = data[4].strip("\n")

            if data[1] == info[0]:
                stuff = data[2]
                stuff = stuff[2:len(stuff)-1]
                stuff = stuff.encode()
                stuff = Account.decrypt_password(stuff)

                info[1] = info[1].encode()

                if stuff == info[1]:
                    f.close()
                    print("-Logged in-")
                   # return True
                    return data

        print("-Log in failed-")
        f.close()
        return False

    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}"

if __name__ == '__main__':
    
    pass
