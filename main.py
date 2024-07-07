from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


window_width = 1000
window_height = 600

buttons_width = 8


def open_file(window, text_area):
    file_path = askopenfilename()  # filetypes=[("Text Files", "*.txt")]

    if not file_path:
        return

    text_area.delete(1.0, END)  # That line will delete all text inside text_area from line 1 and character 0 to the END
    with open(file_path, "r") as file:
        content = file.read()
        text_area.insert(END, content)  # We have deleted all the text, so the end should be the beginning of the text

    window.title(f"Open File: {file_path}")


def save_file(window, textarea):
    file_path = asksaveasfilename()

    if not file_path:
        return

    with open(file_path, "w") as file:
        content = textarea.get(1.0, END)
        file.write(content)
        window.title(f"Saved: {file_path}")


def change_font(font_name, text_area):
    text_area["font"] = f"{font_name} 18"


def main():
    window = Tk()
    window.title("Text Editor")
    window.geometry(f"{window_width}x{window_height}")
    window.maxsize(window_width, window_height)
    window.minsize(window_width, window_height)

    text_area = Text(window, font="Arial 18", bg="white", fg="black")  # width = 100% of the screen
    text_area.grid(row=1, column=0)

    frame = Frame(window)
    frame.grid(row=0, column=0, sticky="ew")

    top_frame = Frame(frame)
    top_frame.grid(row=0, column=0)

    bottom_frame = Frame(frame, padx=100)
    bottom_frame.grid(row=0, column=1)

    open_button = Button(top_frame, text="Open", width=buttons_width, command=lambda: open_file(window, text_area))
    open_button.grid(row=0, column=0, sticky="ns")

    save_button = Button(top_frame, text="Save", width=buttons_width, command=lambda: save_file(window, text_area))
    save_button.grid(row=0, column=1, sticky="ns")

    font = StringVar(window)
    font.set("Font")

    arial_button = Button(bottom_frame, text="Arial", width=buttons_width)
    arial_button["command"] = lambda: change_font("Arial", text_area)
    arial_button.grid(row=0, column=0, sticky="ew")

    verdana_button = Button(bottom_frame, text="Verdana", width=buttons_width)
    verdana_button["command"] = lambda: change_font("Verdana", text_area)
    verdana_button.grid(row=0, column=1, sticky="ew")

    courier_button = Button(bottom_frame, text="Courier", width=buttons_width)
    courier_button["command"] = lambda: change_font("Courier", text_area)
    courier_button.grid(row=0, column=2, sticky="ew")

    likhan_button = Button(bottom_frame, text="Likhan", width=buttons_width)
    likhan_button["command"] = lambda: change_font("Likhan", text_area)
    likhan_button.grid(row=0, column=3)

    window.bind("<Control-o>", lambda x: open_file(window, text_area))
    window.bind("<Control-s>", lambda x: save_file(window, text_area))
    window.bind("<Control-q>", lambda x: quit())

    window.mainloop()


main()
