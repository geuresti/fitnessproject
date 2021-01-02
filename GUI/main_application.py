import tkinter as tk
from create_account import CreateAccount
from log_in import LogIn
    

class MainApplication:

    label_text = """Fitness Application
     Version 1.0

     This program allows you to log your workouts in order
     to help you keep track of your progress and
     achieve your fitness-related goals.

     Programmed by Gio"""

    current_user = None
   

    def __init__(self, window, user=[]):
        self.current_user = user
        
        self.window = window
        self.window.title("Main Menu")
        self.window.geometry("340x230+1000+400")
        self.window.bind("<Escape>", lambda x : window.destroy())

        # testing bind, tab shows current user
        self.window.bind("<Tab>", lambda x : print(self.current_user))

        self.frameA = tk.Frame(master=window, bg="#386641", relief=tk.FLAT)
        
        self.labelA = tk.Label (
            master=self.frameA,
            text=self.label_text,
            bg="#A7C957",
            relief="ridge",
            borderwidth=5,
            width=45,
            height=10,
        )

        self.btn_new_acc = tk.Button (
            master=self.frameA,
            command=self.create_acc_menu,
            text="Create Account",
            bg="#F2E8CF",
            width=18,
        )

        self.btn_log_in = tk.Button (
           master=self.frameA,
           command=self.log_in_menu,
           text="Log In",
           bg="#F2E8CF",
           width=18,
        )
        
        self.frameA.pack(fill=tk.BOTH, expand=True)
        self.labelA.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.btn_new_acc.grid(row=1, column=0, padx=5, pady=5)
        self.btn_log_in.grid(row=1, column=1, padx=5, pady=5)

    # will log in info carry over if the class re-instantiates?
    def log_in_menu(self):
        self.window.destroy()
        
        log_in_page = tk.Tk()
        logger = LogIn(log_in_page)

       # user = logger (returns class object)
       
        user = logger.return_user()
        
        log_in_page.mainloop()

        root = tk.Tk()
        MainApplication(root, user) 
        root.mainloop()

    # will log in info carry over if the class re-instantiates?
    def create_acc_menu(self):
        self.window.destroy()
        
        create_acc_page = tk.Tk()
        CreateAccount(create_acc_page)
        create_acc_page.mainloop()

        root = tk.Tk()
        MainApplication(root)
        root.mainloop()
            
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
