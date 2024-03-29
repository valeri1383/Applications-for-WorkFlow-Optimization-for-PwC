import tkinter as tk
from cryptography.fernet import Fernet
import pyperclip
import pyttsx3
from tkinter import messagebox


def text_to_speach(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


key = b'_1Z0cZ30MHGpJvqTADoBkbegv4k_LQDl6b7NwDZB9Zc='
cipher_suite = Fernet(key)


def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password


def encrypt_button_click():
    password = entry_password.get()
    encrypted_password = encrypt_password(password)
    encrypted_password_str = str(encrypted_password, 'utf-8')
    #label_encrypted_password.config(text="Encrypted Password: " + encrypted_password_str)
    entry_encrypted_display.delete(0, tk.END)
    entry_encrypted_display.insert(0, encrypted_password_str)
    pyperclip.copy(encrypted_password_str)


def decrypt_button_click():
    encrypted_password = entry_encrypted_password.get()
    try:
        decrypted_password = decrypt_password(encrypted_password.encode())
        label_decrypted_password.config(text="Decrypted Password: " + decrypted_password)
        text_to_speach('The password has been decrypted.')
    except:
        messagebox.showerror('Error', 'The password pattern is not matching.')
        text_to_speach('The encrypted pattern is incorrect. ')


def clear_fields():
    entry_password.delete(0, tk.END)
    entry_encrypted_password.delete(0, tk.END)
    entry_encrypted_display.delete(0, tk.END)
    label_encrypted_password.config(text="Encrypted Password: ")
    label_decrypted_password.config(text="Decrypted Password: ")
    text_to_speach('Fields has been cleared')

# Create the main window
root = tk.Tk()
root.title("Password Sharing Cipher App")
root.geometry('550x250')
text_to_speach('Welcome to the password sharing application')



# Configure grid to center content
root.grid_columnconfigure(1, weight=1)

# Center content vertically and horizontally
for widget in root.winfo_children():
    widget.grid_configure(padx=1, pady=1, sticky="nsew")

# Create widgets
label_password = tk.Label(root, text="Enter Password:", font='bold')
entry_password = tk.Entry(root, show='*')

label_encrypted_password = tk.Label(root, text="Encrypted Password:", font='bold')
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_button_click, bg='ivory2')

copy_button = tk.Button(root, text="Copy Encrypted\n Password", command=encrypt_button_click, bg='ivory2')

label_encrypted_input = tk.Label(root, text="Enter Encrypted Password:", font='bold')
entry_encrypted_password = tk.Entry(root)

label_decrypted_password = tk.Label(root, text="Decrypted Password:", font='bold')
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_button_click, bg='ivory2')

button_clear = tk.Button(root, text="Clear Fields", command=clear_fields, bg='ivory2')

label_encrypted_display = tk.Label(root, text="Encrypted Password Display:")
entry_encrypted_display = tk.Entry(root, state='readonly', readonlybackground='lightgray')

# Arrange widgets using grid layout
label_password.grid(row=0, column=0, padx=10, pady=5)
entry_password.grid(row=0, column=1, padx=10, pady=5)

label_encrypted_password.grid(row=1, column=0, padx=10, pady=5)
button_encrypt.grid(row=1, column=1, padx=10, pady=5)
copy_button.grid(row=1, column=2, padx=10, pady=5)

label_encrypted_input.grid(row=2, column=0, padx=10, pady=5)
entry_encrypted_password.grid(row=2, column=1, padx=10, pady=5)

label_decrypted_password.grid(row=3, column=0, padx=10, pady=5)
button_decrypt.grid(row=3, column=1, padx=10, pady=5)

button_clear.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#label_encrypted_display.grid(row=5, column=0, padx=10, pady=5)
#entry_encrypted_display.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
text_to_speach('Goodbye')
