import tkinter as tk
from tkinter import messagebox
import sys

sys.path.append("C:\\Users\\Gio\\Documents\\Computer Science\\fitnessproject")

from account import Account

class LogIn:

    current_user = None

    def __init__(self, window):
        self.window = window
        self.window.title("Log In")
        self.window.geometry("230x170+1300+200")
        self.window.bind("<Escape>", lambda x : self.finale())
        self.window.bind("<Return>", lambda x : self.attempt_log(
            self.ent_user.get(),
            self.ent_psswrd.get()
            )
        )
        
        self.frameA = tk.Frame(master=window, bg="#386641")

        self.ent_user = tk.Entry(master=self.frameA)
        self.lbl_user = tk.Label(master=self.frameA, text="Username: ", bg="#6A994E")
        
        self.ent_psswrd = tk.Entry(master=self.frameA)
        self.lbl_psswrd = tk.Label(master=self.frameA, text="Password: ", bg="#6A994E")


        self.frameA.pack(fill=tk.BOTH, expand=True)
        self.lbl_user.grid(row=0, column=0, padx=5, pady=3)
        self.ent_user.grid(row=0, column=1)

        self.lbl_psswrd.grid(row=1, column=0)
        self.ent_psswrd.grid(row=1, column=1, padx=3, pady=3)
        
    # returns false or [id, user, psswrd, email, file]
    def attempt_log(self, user, psswrd):
        info = Account.check_info([user, psswrd])

        if info is False:
            messagebox.showerror("Log in failed", "Incorrect username or password")
        else:
            self.current_user = info

    def finale(self):
        self.window.destroy()
        return self.current_user
    
    #@staticmethod, doesn't have access to class attributes
    def return_user(self):

        while self.current_user is None:
            pass

        print(self.current_user)
        return self.current_user
        

if __name__ == "__main__":
    test = tk.Tk()
    LogIn(test)
    test.mainloop()
