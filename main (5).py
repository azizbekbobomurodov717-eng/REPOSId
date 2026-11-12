
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kalkulyator")
app.geometry("350x500")
app.resizable(False, False)

display = ctk.CTkEntry(
    app,
    width=310,
    height=70,
    font=("Arial", 28),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


def add_value(value):
    display.insert("end", value)


def clear():
    display.delete(0, "end")


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, "end")
        display.insert(0, str(result))
    except:
        display.delete(0, "end")
        display.insert(0, "Xatolik")


buttons = [
    ("C", 1, 0, clear),
    ("(", 1, 1, lambda: add_value("(")),
    (")", 1, 2, lambda: add_value(")")),
    ("/", 1, 3, lambda: add_value("/")),

    ("7", 2, 0, lambda: add_value("7")),
    ("8", 2, 1, lambda: add_value("8")),
    ("9", 2, 2, lambda: add_value("9")),
    ("*", 2, 3, lambda: add_value("*")),

    ("4", 3, 0, lambda: add_value("4")),
    ("5", 3, 1, lambda: add_value("5")),
    ("6", 3, 2, lambda: add_value("6")),
    ("-", 3, 3, lambda: add_value("-")),

    ("1", 4, 0, lambda: add_value("1")),
    ("2", 4, 1, lambda: add_value("2")),
    ("3", 4, 2, lambda: add_value("3")),
    ("+", 4, 3, lambda: add_value("+")),

    ("0", 5, 0, lambda: add_value("0")),
    (".", 5, 1, lambda: add_value(".")),
    ("=", 5, 2, calculate),
]

for text, row, column, command in buttons:
    button = ctk.CTkButton(
        app,
        text=text,
        width=70,
        height=60,
        font=("Arial", 20, "bold"),
        command=command
    )
    button.grid(
        row=row,
        column=column,
        padx=7,
        pady=7
    )

app.mainloop()

