"""@Aidan Shawyer
    1/16/2023

    Basic log in screen for user. Connects to database and validates exisiting credentials
"""
import bcrypt

#encrypt the passowrd for the first time
#hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(12))
#Check if encrypted password matches normal password
#print(bcrypt.checkpw(password, hashed_password))

def validate_credentials(username, password):
    temp_db = {"username123":b'$2b$12$AolD0C12BJ..z8KxohQwceUF/O/yuU4sZ6AIxJY0s.ZyKAg2bO0FO', 
               "admin123":b'$2b$12$49WcIP63QTxi9ek4.cQZgefcq99VV/iWyGIVlr16LpBIk.Oq5wANq'}
    #Check if entered user name is in dict, check if password matches bcrypt encryption
    if username in temp_db.keys() and bcrypt.checkpw(password, temp_db[username]) == True:
        print("Password succesfull")
        return True
    else:
        print("Invalid username or password")
        return False

def main():
    username = input("Enter username:")
    password = input("Enter the users password")
    validate_credentials(username, password.encode('utf-8'))


main()
