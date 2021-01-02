# fitnessproject
a system that allows the user to make an account, log their workouts, lookup their workouts, log in, log out, and more

## pleateau schedule

PART 1. 
Write a program that allows me to log exercises and store them to a file. I should be able to access logs by date.
	- what is included in a log?
		> date
		> user select [ push day / pull day / legs day ]
		> user input (new set: exercises: reps / weights)
		> write to file along with DATE ADDED ( import datetime )
	- Error checking
		> empty groups
		> missing input
		> no numbers in group, reps/weight
		> no comma in between group and reps/weight
		> non strings in type, exercise 
	- Access logs by date 
		> access logs
		> error message if log does not exist
> more efficient search algorithm (works under the presumption that there no is more than one workout on a given day
- Edit / delete logs?

PART 2.
Write a program that allows me to create an account (username, password). The password should have requirements and use regex to enforce those conventions. The account information should be stored to a file with the encrypted password. (email password reset?)
	- Making an account	
		> (use regex) username, password, email, and an id (provided automatically)
		> should not allow same usernames/emails
> username and encrypted password are stored to a file
    key = Fernet.generate_key()
    file = open('encrypt_key.key', 'wb')
    file.write(key)
    file.close()
> logging in (what happens when checkInfo returns true?)
	- Using an account
		> each account should have a unique workout log 
		> account should be able to calculate calories (using weight, activity, etc.)
		> display data trends? 
		> provide workouts?
		> logging out
		
PART 3.
Command line interface for using program
		> create account, log in, log out
		> log workout, lookup workout, view/edit profile
		> help menu, exit
		
PART 4.
Use the tkinter module to create a GUI for the program.
	- gui pages / options (follow draft image)
		> create account
		> log in
		> forgot password
		> profile, edit profile
		> log workouts
		> view / edit* logs

Notes / To Do: 
	- should fitness_app be a class? *
	- add docstrings*
	- looking up log only displays the most recent log on a given date, so it there are more than one it only displays the latest addition *
	- where am I sending newly created workout files? Maybe make a folder for them *
	- I think the account_data file needs to be initialized (for when running the program for the first time with zero accounts created)
	- need to add ability to edit/add profile info
	- account for similar account usernames / emails
	- when implementing regex, make sure usernames cannot contain “@” 
