from tkinter import *
from cryptography.fernet import Fernet


def cryptographer(editor_content):
    class App:
        def __init__(self, master):
            # Bottom side
            self.message_entry = Text(master, font="Arial 14")
            self.message_entry.grid(row=1, column=0, columnspan=4, sticky="news")
            self.message_entry.insert(END, editor_content)

            # Toolbar
            self.left_toolbar = Frame(master)
            self.left_toolbar.grid(row=0, column=0, columnspan=2, sticky="nsw")

            self.right_toolbar = Frame(master)
            self.right_toolbar.grid(row=0, column=2, columnspan=2, sticky="nse")

            self.encrypt_button = Button(self.left_toolbar, text="Encrypt", command=lambda: self.encrypt_message())
            self.encrypt_button.grid(row=0, column=0, sticky="news")

            self.decrypt_button = Button(self.left_toolbar, text="Decrypt", command=lambda: self.decrypt_message())
            self.decrypt_button.grid(row=0, column=1, sticky="news")

            self.key_entry = Entry(self.right_toolbar, width=50, font="Arial 10")
            self.key_entry.grid(row=0, column=2, sticky="news")

            self.generate_key_button = Button(self.right_toolbar, text="Generate key", command=lambda: self.generate_key())
            self.generate_key_button.grid(row=0, column=3, sticky="news")

        def generate_key(self):
            key = (Fernet.generate_key())
            self.key_entry.delete(0, END)
            self.key_entry.insert(END, key)

        def encrypt_message(self):
            key = self.key_entry.get()
            fer = Fernet(key)

            decrypted_message = self.message_entry.get(1.0, END)
            encrypted_message = fer.encrypt(decrypted_message.encode()).decode()
            self.message_entry.delete(1.0, END)
            self.message_entry.insert(END, encrypted_message)

        def decrypt_message(self):
            key = self.key_entry.get()
            fer = Fernet(key)

            encrypted_message = self.message_entry.get(1.0, END)
            decrypted_message = fer.decrypt(encrypted_message.encode().decode())
            self.message_entry.delete(1.0, END)
            self.message_entry.insert(END, decrypted_message)

    root = Tk()
    root.title("Cryptographer")

    root.grid_rowconfigure(1, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)

    App(root)
    root.mainloop()
