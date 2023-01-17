## Login UI screen with hooked-up back end verification and hashing

Script includes back-end logic, SQLite database to store log-ins, standard login UI 

### Description 
Basic login screen built with customtkinter that is attached to a backend that verifies usernames and passwords.
All username/password combinations are stored in a SQLite database which is used to later retrieve valid users. 
Users not found in the database will not be allowed entry. The script has a place for putting a redirection if users are 
successfully allowed to login. Can add new users to the username/password database aslong as username is not already taken.

Libaries used:
* Customtkinter
* SQLite3
* Bcrypt

### How to use Login script w/ UI
* Download all contents into the same directory
* Run LoginUI.py from commandline or in favorite editor

### How to use Login script w/o UI
* Download all contents into the same directory
* Run mainaccess.py from commandline or in favorite editor
* Main function gives two commands; add user or login

### Future Plans
* Forgot username/password recovery option
* Allow back-end to be customized to preferred variation of SQL


