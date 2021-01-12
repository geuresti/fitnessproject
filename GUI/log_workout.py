import tkinter as tk

class NewWorkout:

    user = None
    workout_name = None

    def __init__(self, window, user):
        self.user = user

        self.workout_title_window = window
        self.workout_title_window.title("New Workout")
        self.workout_title_window.geometry("250x100+1300+200")

        wt_background = tk.Frame(master=self.workout_title_window, bg="#386641")
        wt_background.pack(fill=tk.BOTH, expand=True)

        lbl_workout_title = tk.Label(
            master=wt_background,
            text="Workout title:",
            bg="#6A994E",
        )

        self.ent_workout_title = tk.Entry(master=wt_background)

        btn_next = tk.Button(
            master=wt_background,
            command=self.create_groups,
            text="Next",
            bg="#F2E8CF",
        )

        lbl_workout_title.grid(row=0, column=0, padx=5, pady=5)
        self.ent_workout_title.grid(row=0, column=1, pady=5)
        btn_next.grid(row=1, column=3, pady=5)


    def create_groups(self):

        self.workout_name = self.ent_workout_title.get()
        self.workout_title_window.destroy()

        group_num = 1
            
        create_group_window = tk.Tk()
        create_group_window.title(f"{self.workout_name}")
        create_group_window.geometry("350x170+1300+200")

        cg_background = tk.Frame(master=create_group_window, bg="#386641")
        cg_background.pack(fill=tk.BOTH, expand=True)

        lbl_group_num = tk.Label(
            master=cg_background,
            text=f"Group {group_num}",
            bg="#6A994E",
        )
        lbl_exercise_panel = tk.Label(master=cg_background, bg="#A7C957")
        lbl_exercise_name = tk.Label(
            master=lbl_exercise_panel,
            text="Exercise:",
            bg="#A7C957",
        )
        lbl_reps = tk.Label(master=lbl_exercise_panel, text="reps")
        lbl_weight = tk.Label(master=lbl_exercise_panel, text="weight")
        lbl_x = tk.Label(master=lbl_exercise_panel, text="x", bg="#A7C957")

        ent_exercise_name = tk.Entry(master=lbl_exercise_panel)
        ent_reps = tk.Entry(master=lbl_exercise_panel, width=5)
        ent_weight = tk.Entry(master=lbl_exercise_panel, width=5)

        btn_new_group = tk.Button(
            master=cg_background,
            bg="#F2E8CF",
            text="New Group",
        )
        btn_add_exercise = tk.Button(
            master=lbl_exercise_panel,
            bg="#F2E8CF",
            text="Add Exercise",
        )
        btn_submit_workout = tk.Button(
            master=cg_background,
            bg="#F2E8CF",
            text="Finish Workout",
        )

        lbl_group_num.grid(row=0, column=1, pady=5)
        btn_new_group.grid(row=0, column=2, pady=5)

        lbl_exercise_panel.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        lbl_exercise_name.grid(row=0, column=0, padx=5)
        ent_exercise_name.grid(row=0, column=1)

        ent_reps.grid(row=1, column=1, padx=3)
        lbl_x.grid(row=1, column=2)
        ent_weight.grid(row=1, column=3, padx=3)
        btn_add_exercise.grid(row=1, column=5, padx=10)

        btn_submit_workout.grid(row=2, column=1, pady=5)
        

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
    NewWorkout(root, place_holder)
    root.mainloop()
