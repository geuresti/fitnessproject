# fitnessproject
a system that allows the user to make an account, log their workouts, lookup their workouts, log in, log out, and more

## pleateau schedule

PART 1. 
Write a program that allows me to log exercises and store them to a file. I should be able to access logs by date.
	- what is included in a log?
		> date
		> user input (new workout: exercises: reps / weights)
		> write to file along with DATE ADDED ( use datetime )
	- Error checking
		> empty groups
		> missing input
		> no numbers in group, reps/weight
		> no comma in between group and reps/weight
		> non strings in type, exercise 
	- Access logs by date 
		> access logs
		> error message if log does not exist
		> maybe implement a more efficient search algorithm
	- Edit / delete logs?
		> ...
PART 2.
Write a program that allows me to create an account (username, password). The password should have requirements and use regex to enforce those conventions. The account information should be stored to a file with the encrypted password. (email password reset?)
	- Making an account
		> (use regex) username, password, email, and an id (provided automatically)
		> username and encrypted password are stored to a file
		> logging in (what happens when checkInfo returns true?)
	- Using an account
		> each account should have a unique workout log 
		> account should be able to calculate calories (using weight, activity, etc.)
		> logging out
PART 3.
Use the tkinter module to create a GUI for the program.
	- gui pages / options
		> create account
		> log in
		> profile
		> log workouts
		> view / edit* logs
