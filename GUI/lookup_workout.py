# lookup workout
import tkinter as tk

class LookupWorkout:

    user = None

    def __init__(self, window, user):
        self.user = user

        self.workout_title_window = window
        self.workout_title_window.title("Lookup Workout")
        self.workout_title_window.geometry("250x100+1300+200")

        wt_background = tk.Frame(master=self.workout_title_window, bg="#386641")
        wt_background.pack(fill=tk.BOTH, expand=True)
        

    def get_user(self):
        return self.user


if __name__ == "__main__":

    place_holder = [
        "2",
        "sponge_bob",
        b'gAAAAABf157vyIHMblE-apcogGg0LQw1hWXlzzsGP0SGd7PzaxSFisO9LSCY8Gd4I078g9e7UhfE-9_7JXXJzZY4-cpVuUo6xw==',
        "bikini_bottom@gmail.com",
        "sponge_bob2.txt",
    ]
    
    root = tk.Tk()
    LookupWorkout(root, place_holder)
    root.mainloop()
