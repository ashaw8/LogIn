"""@Aidan Shawyer
    1/16/2023

    Basic log in screen for user. Connects to database and validates exisiting credentials
"""
import bcrypt
import sqlite3
import customtkinter
#Connect to database created in createDB.py script
connection = sqlite3.connect("UserLogin.db")
cursor = connection.cursor()

def validate_credentials(username, password):
    #Grab the password from DB based off of username
    resPW = cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    queryPW = resPW.fetchall()
    #fetch the entered user name from the database
    resUSER = cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    
    #Need to convert str query to bytes before checkpw
    queryUSER = resUSER.fetchall()
  
    if len(queryUSER) == 0: #Dont continue if no results from Database
        print("Not a valid username/password")
        return

    #Depending on pasword data type, preform different operations
    if type(queryPW[0][0]) == str:
        queryPW = bytes(queryPW[0][0][2:-1:],'utf-8')

    elif type(queryPW[0][0]) == bytes:
        queryPW = queryPW[0][0]
  
    #Check username and password hash match eachother
    if queryUSER[0][0] == username and bcrypt.checkpw(password, queryPW) == True: 
            #direct to any other piece of content here if user is valid in database
            print("Valid password")
    else:
        print("Invalid username/password combination")


def add_users(desired_username, password):
    #Adding users to database if desired name is not already taken
    if existing_users(desired_username) == False:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))
        cursor.execute("INSERT INTO users VALUES (?,?)",(desired_username,hashed_password))
        connection.commit()
        print("Success!")
    else:
        print("Failed")


def existing_users(desired_username):
    #Check if the username desire is already taken in database
    dbcheck = cursor.execute("SELECT * FROM users")
    results = dbcheck.fetchall()
    users_in_db = []
    for i in results:
        users_in_db.append(i[0])#Append only the username in user/pw set
    
    if desired_username in users_in_db:
        print("Username is taken")
        return True
    else:
        return False


def main():
    request = input("Login | AddUser ")
    match request:
        case "Login":
            username = input("Enter username:")
            password = input("Enter the users password")
            validate_credentials(username, password.encode('utf-8'))
        case "AddUser":
            DUN = input("Desired username: ")
            pw = input("Password: ")
            add_users(DUN, pw)


#main()

