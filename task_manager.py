#Step-by-step Implementation:

#Follow the below steps to implement a personalized task manager using Python:

#Step 1: Create a folder name ‘Task Manager’. Open it in your favorite code editor.
#Step 2: Create a python file with the name ‘task_manager.py’.
#Step 3: Now we are ready to code our software

def signup():
	print("Please enter the username by which you \
	wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")

#Step 4: Now we will create a ‘user_information’
 # pssd means password, ussnm is username
def user_information(ussnm, pssd):
	name = input("enter your name please: ")
	address = input("your address")
	age = input("Your age please")
	ussnm_ = ussnm+" task.txt"
	
	f = open(ussnm_, 'a')
	f.write(pssd)
	f.write("\nName: ")
	f.write(name)
	f.write('\n')
	f.write("Address :")

	f.write(address)
	f.write('\n')
	f.write("Age :")
	f.write(age)
	f.write('\n')
	f.close()


def signup():
	print("Please enter the username by which you\
	wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
	user_information(username, password)

#Step 5: Once the text file is created by the user_information function, it’s time that we code our log-in function

def login():
	print("Please enter your username ")
	user_nm = input("Enter here: ")
	
	# Password as entered while logging in
	pssd_wr = (input("enterr the password"))+'\n'
	try:
		usernm = user_nm+" task.txt"
		f_ = open(usernm, 'r')
		
		# variable 'k' contains the password as saved
		# in the file
		k = f_.readlines(0)[0]
		f_.close()
		
		# Checking if the Password entered is same as
		# the password saved while signing in
		if pssd_wr == k: 
			print(
				"1--to view your data \n2--To add task \n3--Update\
				task status \n4--View task status")
			a = input()
		else:
			print("SIR YOUR PASSWORD OR USERNAME IS WRONG , Plz enter Again")
			login()
	except Exception as e:
		print(e)
		login()

#Step 6: In this step, we will make sure that after the user signs in we can ask him/her to log in to their account.

def signup():
	print("Please enter the username by which you wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
	user_information(username, password)
	print("Sir please proceed towards log in")
	login()

#Let’s complete the four important functions as mentioned in the ‘login ‘block.

def login():
	print("Please enter your username ")
	user_nm = input("Enter here: ")
	
	# Password as entered while logging in
	pssd_wr = (input("enterr the password"))+'\n'
	try:
		usernm = user_nm+" task.txt"
		f_ = open(usernm, 'r')
		
		# variable 'k' contains the password as
		# saved in the file
		k = f_.readlines(0)[0]
		f_.close()
		
		# Checking if the Password entered is same
		# as the password saved while signing in
		if pssd_wr == k: 
			print(
				"1--to view your data \n2--To add task \n3--Update\
				task \n4--VIEW TASK STATUS")
			a = input()
			
			if a == '1':
				view_data(usernm)
			elif a == '2':
				# add task
				task_information(usernm)
			elif a == '3':
				task_update(user_nm)
			elif a == '4':
				task_update_viewer(user_nm)
			else:
				print("Wrong input ! ")
		else:
			print("SIR YOUR PASSWORD OR USERNAME IS WRONG")
			login()

	except Exception as e:
		print(e)
		login()


def view_data(username):
	pass

def task_information(username):
	pass

def task_update(username):
	pass

def task_update_viewer(username):
	pass

#Step 8: Let’s code the view data block.

def view_data(username):
	ff = open(username, 'r')
	print(ff.read())
	ff.close()

#Step 9: To code the task information block we need to keep in mind the basic concepts of text handling in python.

def task_information(username):
	print("Sir enter n.o of task you want to ADD")
	j = int(input())
	f1 = open(username, 'a')
	
	for i in range(1, j+1):
		task = input("enter the task")
		target = input("enter the target")
		pp = "TASK "+str(i)+' :'
		qq = "TARGET "+str(i)+" :"
		
		f1.write(pp)
		f1.write(task)
		f1.write('\n')
		f1.write(qq)
		f1.write(target)
		f1.write('\n')
		
		print("Do u want to stop press space bar otherwise enter")
		s = input()
		if s == ' ':
			break
	f1.close()


#Updating the task status goes in the similar concept of text handling

   # That part of the text file will look like,

         #  2021-06-01 14:44:02.851506
           #COMPLETED TASK   1,3,4
           #ONGOING TASK  2
           #NOT YET STARTED 5

def task_update(username):
	username = username+" TASK.txt"
	print("Please enter the tasks which are completed ")
	
	task_completed = input()
	print("Enter task which are still not started by you")
	
	task_not_started = input()
	print("Enter task which you are doing")
	
	task_ongoing = input()
	fw = open(username, 'a')
	DT = str(datetime.datetime.now())
	
	fw.write(DT)
	fw.write("\n")
	fw.write("COMPLETED TASK \n")
	fw.write(task_completed)
	fw.write("\n")
	fw.write("ONGOING TASK \n")
	fw.write(task_ongoing)
	fw.write("\n")
	fw.write("NOT YET STARTED\n")
	fw.write(task_not_started)
	fw.write("\n")

#Step 11: Now we are left with the task update viewer function. This function is as simple as the ‘view_data’ function.

def task_update_viewer(username):
	ussnm = username+" TASK.txt"
	o = open(ussnm, 'r')
	print(o.read())
	o.close()

#Step 12: The main function.
if __name__ == '__main__':
	print("WELCOME TO ANURAG`S TASK MANAGER")
	print("sir are you new to this software")
	a = int(input("Type 1 if new otherwise press 0 ::"))
	
	if a == 1:
		signup()
	elif a == 0:
		login()
	else:
		print("You have provided wrong input !")
#This marks the end of the code. You should try to do suitable changes to this code so that the software becomes more beautiful.

#Source Code:
import datetime

# pssd means password, ussnm is username
def user_information(ussnm, pssd): 
	name = input("enter your name please: ")
	address = input("your address")
	age = input("Your age please")
	ussnm_ = ussnm+" task.txt"
	f = open(ussnm_, 'a')
	f.write(pssd)
	f.write("\nName: ")
	f.write(name)
	f.write('\n')
	f.write("Address :")

	f.write(address)
	f.write('\n')
	f.write("Age :")
	f.write(age)
	f.write('\n')
	f.close()


def signup():
	print("Please enter the username by which you wanna access your account")
	username = input("please enter here: ")
	password = input("Enter a password: ")
	user_information(username, password)
	print("Sir please proceed towards log in")
	login()


def login():
	print("Please enter your username ")
	user_nm = input("Enter here: ")
	
	# Password as entered while logging in
	pssd_wr = (input("enterr the password"))+'\n'
	try:
		usernm = user_nm+" task.txt"
		f_ = open(usernm, 'r')
		
		# variable 'k' contains the password as saved
		# in the file
		k = f_.readlines(0)[0]
		f_.close()
		
		# Checking if the Password entered is same as 
		# the password saved while signing in
		if pssd_wr == k: 
			print(
				"1--to view your data \n2--To add task \n3--Update\
				task \n4--VIEW TASK STATUS")
			a = input()
			
			if a == '1':
				view_data(usernm)
			elif a == '2':
				# add task
				task_information(usernm)
			elif a == '3':
				task_update(user_nm)
			elif a == '4':
				task_update_viewer(user_nm)
			else:
				print("Wrong input ! bhai dekh kr input dal")
		else:
			print("SIR YOUR PASSWORD OR USERNAME IS WRONG")
			login()

	except Exception as e:
		print(e)
		login()


def view_data(username):
	ff = open(username, 'r')
	print(ff.read())
	ff.close()


def task_information(username):
	print("Sir enter n.o of task you want to ADD")
	j = int(input())
	f1 = open(username, 'a')
	
	for i in range(1, j+1):
		task = input("enter the task")
		target = input("enter the target")
		pp = "TASK "+str(i)+' :'
		qq = "TARGET "+str(i)+" :"
		
		f1.write(pp)
		f1.write(task)
		f1.write('\n')
		f1.write(qq)
		f1.write(target)
		f1.write('\n')
		print("Do u want to stop press space bar otherwise enter")
		s = input()
		if s == ' ':
			break
	f1.close()


def task_update(username):
	username = username+" TASK.txt"
	print("Please enter the tasks which are completed ")
	task_completed = input()
	
	print("Enter task which are still not started by you")
	task_not_started = input()
	
	print("Enter task which you are doing")
	task_ongoing = input()
	
	fw = open(username, 'a')
	DT = str(datetime.datetime.now())
	fw.write(DT)
	fw.write("\n")
	fw.write("COMPLETED TASK \n")
	fw.write(task_completed)
	fw.write("\n")
	fw.write("ONGOING TASK \n")
	fw.write(task_ongoing)
	fw.write("\n")
	fw.write("NOT YET STARTED\n")
	fw.write(task_not_started)
	fw.write("\n")


def task_update_viewer(username):
	ussnm = username+" TASK.txt"
	o = open(ussnm, 'r')
	print(o.read())
	o.close()


if __name__ == '__main__':
	print("WELCOME TO ANURAG`S TASK MANAGER")
	print("sir are you new to this software")
	a = int(input("Type 1 if new otherwise press 0 ::"))
	if a == 1:
		signup()
	elif a == 0:
		login()
	else:
		print("You have provided wrong input !")







