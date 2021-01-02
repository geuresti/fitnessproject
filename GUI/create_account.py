import tkinter as tk
from tkinter import messagebox
import sys

sys.path.append("C:\\Users\\Gio\\Documents\\Computer Science\\fitnessproject")

from account import Account

class CreateAccount:
    
    requirement_text = """Username must be between
6 and 20 characters. It may contain
letters, numbers, and special characters
(except "." and "@")

*Password currently has no requisites.*"""

    def __init__(self, window):
        self.window = window
        self.window.title("New Account")
        self.window.geometry("220x220+1000+140")
        self.window.bind("<Escape>", lambda x : window.destroy())
        self.window.bind("<Return>", lambda x : self.attempt_create (
                self.ent_user.get(),
                self.ent_psswrd.get(),
                self.ent_email.get(),
            )
        )
        
        self.frameA = tk.Frame(master=window, bg="#386641")

        self.ent_user = tk.Entry(master=self.frameA)
        self.lbl_user = tk.Label(master=self.frameA, bg="#6A994E", text="Username: ")

        self.ent_psswrd = tk.Entry(master=self.frameA)
        self.lbl_psswrd = tk.Label(master=self.frameA, bg="#6A994E", text="Password: ")

        self.ent_email = tk.Entry(master=self.frameA)
        self.lbl_email = tk.Label(master=self.frameA, bg="#6A994E", text="Email: ")

        self.lbl_reqs = tk.Label(
            master=self.frameA,
            bg="#A7C957",
            text=self.requirement_text,
        )

        self.btn_back = tk.Button(
            master=self.frameA,
            command=self.back,
            bg="#F2E8CF",
            text="Back",
            width=5,
            )
       
        self.frameA.pack(fill=tk.BOTH, expand=True)

        self.lbl_user.grid(row=1, column=0, sticky="W")
        self.ent_user.grid(row=1, column=1, padx=5, pady=3)

        self.lbl_psswrd.grid(row=2, column=0, sticky="W")
        self.ent_psswrd.grid(row=2, column=1, padx=3, pady=3)

        self.lbl_email.grid(row=3, column=0, sticky="W")
        self.ent_email.grid(row=3, column=1, padx=3, pady=3)

        self.lbl_reqs.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_back.grid(row=0, column=0, padx=1, pady=5)
        
    def attempt_create(self, user, password, email):
        if user == "" or password == "" or email == "":
            messagebox.showerror(
                f"Info Error",
                "One or more entries have been left unfilled."
            )
        else: 
            CreateAccount.validate_input([user, password, email])
           

# check for errors with inputted username, password, and info
    def validate_input(items):

        entry = ""
        error_list = ""
        error_id = None
    
        codes = {
            1:"success",
            0:f"{entry} does not fulfill requisites",
            -1:f"{entry} is already taken"
        }
        
        for i in range(len(items)):
            if i == 0:
                entry = "Username"
                error_id = Account.valid_user(items[i])
            elif i == 1:
                entry = "Password"
                error_id = Account.valid_psswrd(items[i])
            else:
                entry = "Email"
                error_id = Account.valid_email(items[i])

            if error_id != 1:
                error_list += (entry + codes[error_id] + "\n")

        if error_list:
            messagebox.showerror("Error", error_list)
            return False
        else:
            messagebox.showinfo("Success", "Account succesfully created")
            return True

    def back(self):
        #self.window.destroy()
        print("return to home page")


if __name__ == "__main__":
    root = tk.Tk()
    CreateAccount(root)
    root.mainloop()
