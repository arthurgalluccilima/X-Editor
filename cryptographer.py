def cryptographer():
    import tkinter
    from cryptography.fernet import Fernet

    class App:
        def __init__(self, master):
            # Left side
            self.message_entry = tkinter.Text(master, font="Arial 14")
            self.message_entry.grid(row=0, column=0, sticky="news")

            self.encrypt_button = tkinter.Button(master, text="Encrypt", command=lambda: self.encrypt_message())
            self.encrypt_button.grid(row=1, column=0, sticky="news")

            self.decrypt_button = tkinter.Button(master, text="Decrypt", command=lambda: self.decrypt_message())
            self.decrypt_button.grid(row=2, column=0, sticky="news")

            # Right side
            self.key_entry = tkinter.Text(master, font="Arial 10")
            self.key_entry.grid(row=0, column=1, sticky="news")

            self.generate_key_button = tkinter.Button(master, text="Generate key", command=lambda: self.generate_key())
            self.generate_key_button.grid(row=1, column=1, sticky="news")

        def generate_key(self):
            key = Fernet.generate_key()
            self.key_entry.delete(1.0, tkinter.END)
            self.key_entry.insert(tkinter.END, key)

        def encrypt_message(self):
            key = self.key_entry.get(1.0, tkinter.END)
            fer = Fernet(key)

            decrypted_message = self.message_entry.get(1.0, tkinter.END)
            encrypted_message = fer.encrypt(decrypted_message.encode()).decode()
            self.message_entry.delete(1.0, tkinter.END)
            self.message_entry.insert(tkinter.END, encrypted_message)

        def decrypt_message(self):
            key = self.key_entry.get(1.0, tkinter.END)
            fer = Fernet(key)

            encrypted_message = self.message_entry.get(1.0, tkinter.END)
            decrypted_message = fer.decrypt(encrypted_message.encode().decode())
            self.message_entry.delete(1.0, tkinter.END)
            self.message_entry.insert(tkinter.END, decrypted_message)

    root = tkinter.Tk()
    root.title("Cryptographer")

    root.geometry("800x600")
    root.minsize(800, 600)
    root.maxsize(800, 600)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)

    App(root)
    root.mainloop()
