import cryptography
from cryptography.fernet import Fernet

class Account:

    id = 0

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        #self.storeInfo(password)
        self.id = Account.idAccount()

    @classmethod
    def idAccount(cls):
        cls.id += 1
        return cls.id

    def storeInfo(self, password):
        f = open("account_data.txt", "a")
        pswrd = Account.encryptPassword(password)
        print(f"{self.username}|{pswrd}|{self.email}", file=f)
        f.close()

#    key = Fernet.generate_key()
#    file = open('encrypt_key.key', 'wb')
#    file.write(key)
#    file.close()
    def encryptPassword(msg):
        file = open('encrypt_key.key', 'rb')
        key = file.read()
        file.close()

        f = Fernet(key)
        message = msg.encode()
        encrypted_message = f.encrypt(message)

        return encrypted_message

    def decryptPassword(msg):
        file = open('encrypt_key.key', 'rb')
        key = file.read()
        file.close()

        f = Fernet(key)
        decrypted_password = f.decrypt(msg)

        return decrypted_password

    # refactor
    @classmethod
    def checkInfo(cls, info):
        f = open("account_data.txt", "r")
        for line in f:
            data = line.split("|")
            data[2] = data[2].strip("\n")

            if data[0] == info[0]:
                stuff = data[1]
                stuff = stuff[2:len(stuff)-1]
                stuff = stuff.encode()
                stuff = Account.decryptPassword(stuff)

                info[1] = info[1].encode()

                if stuff == info[1]:
                    f.close()
                    print("Logged in")
                    return True

        print("Log in failed")
        f.close()
        return False

    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}"

if __name__ == '__main__':
    log_in_attempt = ["test_dummy", "redLines123"]
    Account.checkInfo(log_in_attempt)
    user = Account("new_person", "new_password", "new_email@something.com")
    print(type(user))  # store accounts to file as Account objects for logging in?
    print(user.id)
    print(Account.id)
    user_two = Account("new_person_two", "new_pass", "new_email@xd.com")
    print(user_two.id)
    print(Account.id)
