from datetime import date

# input a workout to be stored in the workout data text file
def log_workout(filename):
    log_date = date.today()

    exerciseNumber = 1

    workoutType = input("Enter the type of workout: ")

    def has_number():
        for letter in workoutType:
            if letter.isdigit():
                return True
        return False

    hasNum = has_number()

    while hasNum:
        print("Please only use letters.")
        workoutType = input("Enter the type of workout: ")
        hasNum = has_number()

    numberGroups = input("Enter the number of groups: ")
    while not numberGroups.isdigit():
        print("Please enter a number.")
        numberGroups = input("Enter the number of groups: ")

    numberGroups = int(numberGroups)

    print("\nType the name of the exercise\nPress 'Enter' to continue\n")

    f = open(filename, "a")
    f.write(f"{log_date}, {workoutType}|")

    for i in range(1, numberGroups+1):
        addExercise = True
        print(f"Group {i}:")
        s = f"Group {i}"
        f.write(s)

        while addExercise is True:
            exercise = input(f"{exerciseNumber}. ")

            if exercise == "":
                f.write("|")
                addExercise = False
                break
            else:
                reps = input("    reps: ")

                while reps == "" or not reps.isdigit():
                    print("Provide proper input for reps.")
                    reps = input("    reps: ")

                weight = input("    weight: ")
                while weight == "" or not weight.isdigit():
                    print("Provide proper input for weight.")
                    weight = input("    weight: ")

                f.write(", " + exercise + " " + reps + " x " + weight)

            exerciseNumber += 1

    f.write("\n")
    f.close()
    print("-Workout Logged-")

# look up a workout by date and display it
def display_log(filename, date):
    # xxxx-xx-xx format, datetime.date(x,y,z)
    f = open(filename, "r")

    for line in f:
        if line[0:line.find(",")] == date:
            f.close()
            return display_line(line)

    f.close()
    print(f"Workout from '{date}' not found.")
    return ""

# format a line (workout) from the workout data text file
def display_line(line):

    line = line.split("|")
    for data in line:
        print(data)

# any uses outside of testing? (DELETE)
def display_data():
    data = []

    with open('workout_log.txt', 'r') as f:

        workouts = f.read()

        log = workouts.split("|")
     #   log.remove("\n")

        for item in log:
            item_list = item.split(",")
            cleaned = []

            for i in item_list:
                cleaned.append(i.strip())

            data.append(cleaned)

        f.close()
    print(data)


if __name__ == "__main__":
  #   display_log('2020-11-24')
  pass
