from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk


class Editor:
    def __init__(self, master):
        self.text_area = Text(master, font="Arial 12")
        self.text_area.grid(column=0, row=1, columnspan=3, stick="news")

        self.toolbar_left = Frame(master)
        self.toolbar_left.grid(column=0, row=0, columnspan=1, sticky="w")

        self.toolbar_right = Frame(master)
        self.toolbar_right.grid(column=2, row=0, columnspan=1, sticky="e")

        self.open_button = Button(self.toolbar_left, text="Open")
        self.open_button["command"] = lambda: self.open_file()
        self.open_button.grid(column=0, row=0, sticky="ns")

        self.save_button = Button(self.toolbar_left, text="Save")
        self.save_button["command"] = lambda: self.save_file()
        self.save_button.grid(column=1, row=0)

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
        self.font_families_dropdown.grid(column=2, row=0, sticky="ns")

        self.font_sizes_dropdown = ttk.OptionMenu(
            self.toolbar_right,
            self.current_font_size,
            str(self.available_font_sizes[0]),
            *self.available_font_sizes,
            direction="below",
            command=self.change_font
        )
        self.font_sizes_dropdown.grid(column=3, row=0)

    def open_file(self):
        file_path = askopenfilename()

        if not file_path:
            return

        with open(file_path, "r") as file:
            file_text = file.read()

        self.text_area.delete(1.0, END)
        self.text_area.insert(END, file_text)

    def save_file(self):
        file_path = asksaveasfilename()

        if not file_path:
            return

        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, END))

    def change_font(self, argument):
        font_name = self.current_font_family.get()
        font_size = self.current_font_size.get()

        self.text_area["font"] = f"{font_name} {font_size}"


root = Tk()
root.title("X Editor")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

Editor(root)
root.mainloop()
