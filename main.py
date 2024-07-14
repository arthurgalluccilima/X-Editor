from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
from cryptographer import cryptographer


class Editor:
    filetype = "txt"

    def __init__(self, master):
        self.toolbar_left = Frame(master)
        self.toolbar_left.grid(column=0, row=0, columnspan=1, sticky="w")

        self.toolbar_right = Frame(master)
        self.toolbar_right.grid(column=2, row=0, columnspan=1, sticky="e")

        self.text_area = Text(master, font="Arial 12")
        self.text_area.grid(column=0, row=1, columnspan=3, stick="news")

        self.open_button = Button(self.toolbar_left, text="Open")
        self.open_button["command"] = lambda: self.open_file()
        self.open_button.grid(column=0, row=0, sticky="ns")

        self.save_button = Button(self.toolbar_left, text="Save")
        self.save_button["command"] = lambda: self.save_file()
        self.save_button.grid(column=1, row=0)

        self.cryptographer_button = Button(self.toolbar_left, text="Cryptographer", command=lambda: cryptographer(self.text_area.get(1.0, END)))
        self.cryptographer_button.grid(column=2, row=0)

        self.available_font_sizes = [12, 14, 16, 18, 20, 24, 26, 28, 30]
        self.current_font_size = IntVar()
        self.available_font_families = ["Arial", "Verdana", "Georgia", "Tahoma"]
        self.current_font_family = StringVar()

        self.font_families_dropdown = ttk.OptionMenu(
            self.toolbar_right,
            self.current_font_family,
            self.available_font_families[0],
            *self.available_font_families,
            direction="below",
            command=self.change_font
        )
        self.font_families_dropdown.grid(column=3, row=0, sticky="ns")

        self.font_sizes_dropdown = ttk.OptionMenu(
            self.toolbar_right,
            self.current_font_size,
            str(self.available_font_sizes[0]),
            *self.available_font_sizes,
            direction="below",
            command=self.change_font
        )
        self.font_sizes_dropdown.grid(column=4, row=0)

        master.bind("<Control-o>", lambda *args: self.open_file())
        master.bind("<Control-s>", lambda *args: self.save_file())
        master.bind("<Control-q>", lambda *args: quit())

    def open_file(self):
        file_path = askopenfilename()

        if not file_path:
            return

        with open(file_path, "r") as file:
            file_text = file.read()

        self.text_area.delete(1.0, END)
        self.text_area.insert(END, file_text)

        filename = file_path.split("/")[-1]
        root.title(f"X Editor: {filename}")

        self.mark_programming_language(filename)

    def save_file(self):
        file_path = asksaveasfilename()

        if not file_path:
            return

        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, END))

        filename = file_path.split("/")[-1]
        root.title(f"X Editor: {filename}")

    def change_font(self, *args):
        font_name = self.current_font_family.get()
        font_size = self.current_font_size.get()

        self.text_area["font"] = f"{font_name} {font_size}"

    def mark_programming_language(self, filename):
        filetype = filename.split(".")[-1]
        if filetype == "txt":
            print("Text")
        elif filetype == "py":
            print("Python")
            for line in self.text_area.get(1.0, END).splitlines():
                with open("reserved_words_python.txt", "r") as reserved_words_file:
                    for word in reserved_words_file:
                        print(self.text_area.get(1.0, END).find(word))

        else:
            print("That's text or we dont have support to this language yet.")


root = Tk()
root.title("X Editor")
icon = PhotoImage(file="icon.png")
root.wm_iconphoto(False, icon)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

Editor(root)
root.mainloop()
