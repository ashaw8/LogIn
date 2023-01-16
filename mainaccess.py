"""@Aidan Shawyer
    1/16/2023

    Basic log in screen for user. Connects to database and validates exisiting credentials
"""
import bcrypt
import sqlite3

#encrypt the passowrd for the first time
#hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))
#Check if encrypted password matches normal password
connection = sqlite3.connect("UserLogin.db")
cursor = connection.cursor()
#name = "admin123"
#res = cursor.execute("SELECT password FROM users")
#res = cursor.execute("SELECT password FROM users WHERE username = ?", (name,))
#query= res.fetchall()
#username = "admin123"
#resUSER = cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
#qu = resUSER.fetchall()
#print(qu[0][0])
def validate_credentials(username, password):
    #Grab the password from DB based off of username
    resPW = cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    queryPW = resPW.fetchall()
    #fetch the entered user name from the database
    resUSER = cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    
    #Need to convert str query to bytes before checkpw
    queryUSER = resUSER.fetchall()
    hashed_password = bytes(queryPW[0][0][2:-1:],'utf-8')
    if len(queryUSER) != 0 and queryUSER[0][0] == username:
        if bcrypt.checkpw(password, hashed_password) == True:
            #direct to any other piece of content here if user is valid in database
            print("Valid password")
        else:
            print("Invalid password")
    else:
        print("Invalid password")

def main():
    username = input("Enter username:")
    password = input("Enter the users password")
    validate_credentials(username, password.encode('utf-8'))



main()
