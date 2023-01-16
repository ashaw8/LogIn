import sqlite3

connection = sqlite3.connect("UserLogin.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR, password VARCHAR)")
cursor.execute("""
    INSERT INTO users VALUES
    ("username123", "b'$2b$12$AolD0C12BJ..z8KxohQwceUF/O/yuU4sZ6AIxJY0s.ZyKAg2bO0FO'"),
    ("admin123", "b'$2b$12$49WcIP63QTxi9ek4.cQZgefcq99VV/iWyGIVlr16LpBIk.Oq5wANq'")
""")
connection.commit()