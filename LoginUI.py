from mainaccess import *

"""Simple UI to display what a potential log in screen could look like
and how it interacts with the back-end logic

Credit @NeuralNine (@all socials) for UI inspiration
"""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def confirm_login():
    unAttempt = entry1.get()
    pwAttempt = bytes(entry2.get(),'utf-8')
    validate_credentials(unAttempt, pwAttempt)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show='*')
entry2.pack(pady=12, padx=10)

button =customtkinter.CTkButton(master=frame, text='Login', command=confirm_login)
button.pack(pady=12, padx= 10)

root.mainloop()