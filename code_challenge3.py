from getpass import getpass
username = input("Enter your username: ")
password = getpass("Enter your password: ")
uname = 'blackianaisgone'
pwd = 'glindakilledher'
if uname == username and pwd == password :
	print("Access Granted!")
else :
	print("Access Denied!")