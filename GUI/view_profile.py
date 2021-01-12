import tkinter as tk
from log_workout import NewWorkout
from edit_workout import EditWorkout
from edit_profile import EditProfile
from lookup_workout import LookupWorkout

class Profile:

    user = None
    
    def __init__(self, window, user):
        self.user = user # there should always be a user

        filepath = "C:\\Users\\Gio\\Documents\\Computer Science\\fitnessproject\\" + user[4]
        file = open(filepath, "r")
        calorie_info = file.readline()
        calorie_info = calorie_info.split(",")

        weight = calorie_info[0]
        calories_bulk = calorie_info[1]
        calories_cut = calorie_info[2]
        calories_maintain = calorie_info[3]

        self.window = window
        self.window.title("Profile")
      #  self.window.geometry("320x340+1000+800")
        self.window.geometry("360x340+1200+200")

        self.window.bind("<Escape>", lambda x : self.window.destroy())

        self.frameA = tk.Frame(master=window, bg="#386641")
        self.frameA.pack(fill=tk.BOTH, expand=True)

        self.lbl_info = tk.Label(
            master=self.frameA,
            text=f"""User: {self.user[1]}
Email: {self.user[3]}
Account ID: {self.user[0]}

{weight}

Calorie Levels:
{calories_bulk}
{calories_cut}
{calories_maintain}
""",
            bg="#A7C957",
            relief="ridge",
            borderwidth=5,
            width=30,
            height=15,
        )

        self.frame_option_menu = tk.Frame(
            master=self.frameA,
            bg="#6A994E",
            relief="groove",
            borderwidth=2,
        )
        
        self.frame_option_menu.grid(row=1, column=3)#, rowspan=2)
            
        self.btn_log = tk.Button(
            master=self.frame_option_menu,
            command=self.log_workout,
            text="Log Workout",
            bg="#F2E8CF"
        )
        self.btn_lookup = tk.Button(
            master=self.frame_option_menu,
            command=self.lookup_workout,
            text="Lookup Workout",
            bg="#F2E8CF"
        )
        self.btn_edit_log = tk.Button(
            master=self.frame_option_menu,
            command=self.edit_workout,
            text="Edit Workout",
            bg="#F2E8CF"
        )

        self.btn_edit_info = tk.Button(
            master=self.frameA,
            command=self.edit_workout,
            text="Edit Info",
            bg="#F2E8CF"
        )
        self.btn_back = tk.Button(
            master=self.frameA,
           # command=self.back,
            text="Back",
            bg="#F2E8CF"
        )

        self.lbl_info.grid(row=1, column=0, rowspan=4, columnspan=2, padx=5, pady=5)

        self.btn_log.grid(row=0, column=0, padx=5, pady=5)
        self.btn_lookup.grid(row=1, column=0, padx=5, pady=5)
        self.btn_edit_log.grid(row=2, column=0, padx=5, pady=5)
        
        self.btn_edit_info.grid(row=5, column=0, padx=5, pady=5)
        self.btn_back.grid(row=0, column=0, padx=5, pady=2)

    def log_workout(self):
        self.window.destroy()
        
        new_window = tk.Tk()
        user_access = NewWorkout(new_window, self.user)
        new_window.mainloop()

        user = user_access.get_user()

        root = tk.Tk()
        Profile(root, user)
        root.mainloop()

    def edit_workout(self):
        self.window.destroy()
        
        new_window = tk.Tk()
        user_access = EditWorkout(new_window, self.user)
        new_window.mainloop()

        user = user_access.get_user()

        root = tk.Tk()
        Profile(root, user)
        root.mainloop()
        
    def lookup_workout(self):
        self.window.destroy()
        
        new_window = tk.Tk()
        user_access = LookupWorkout(new_window, self.user)
        new_window.mainloop()

        user = user_access.get_user()

        root = tk.Tk()
        Profile(root, user)
        root.mainloop()

    def edit_profile(self):
        self.window.destroy()
        
        new_window = tk.Tk()
        user_access = EditProfile(new_window, self.user)
        new_window.mainloop()

        user = user_access.get_user()

        root = tk.Tk()
        Profile(root, user)
        root.mainloop()

    def back(self):
        print("[return home]")

    # for maintaining user info in between windows
    def get_user(self):
        return self.user


if __name__ == "__main__":

    print("main ran")
    root = tk.Tk()
    place_holder = [
        "2",
        "sponge_bob",
        b'gAAAAABf157vyIHMblE-apcogGg0LQw1hWXlzzsGP0SGd7PzaxSFisO9LSCY8Gd4I078g9e7UhfE-9_7JXXJzZY4-cpVuUo6xw==',
        "bikini_bottom@gmail.com",
        "sponge_bob2.txt",
    ]
    
    Profile(root, place_holder)
    root.mainloop()
        
