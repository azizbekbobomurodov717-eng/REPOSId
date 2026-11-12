from customtkinter import *

def get_text():
    change_matnn = entry.get()
    matn.configure(text=change_matnn)
    entry.delete(0, END)
    root.configure(fg_color=change_matnn)

root = CTk()
root.geometry("400x300")
root.title("First CTK")

matn = CTkLabel(root, text="Bu mening 1 chi ctk dasturim!")
matn.pack()

btn = CTkButton(root, text="Change", command=get_text, corner_radius=25)
btn.pack()


entry = CTkEntry(root, placeholder_text="CTkentry")
entry.pack()

root.mainloop()