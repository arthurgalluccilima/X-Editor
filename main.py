from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window_width = 1000
window_height = 650


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


def main():
    window = Tk()
    window.title("Text Editor")
    window.geometry(f"{window_width}x{window_height}")
    window.maxsize(window_width, window_height)
    window.minsize(window_width, window_height)

    text_area = Text(window, font="Arial 18", bg="white", fg="black")
    text_area.grid(row=0, column=1)

    frame = Frame(window, padx=5)
    frame.grid(row=0, column=0, sticky="ns")

    save_button = Button(frame, text="Save", padx=5, pady=5, command=lambda: save_file(window, text_area))
    save_button.grid(row=0, column=0, sticky="ew")

    open_button = Button(frame, text="Open", padx=5, pady=5, command=lambda: open_file(window, text_area))
    open_button.grid(row=1, column=0, sticky="ew")

    window.bind("<Control-s>", lambda x: save_file(window, text_area))
    window.bind("<Control-o>", lambda x: open_file(window, text_area))
    window.bind("<Control-q>", lambda x: quit())

    window.mainloop()


main()
