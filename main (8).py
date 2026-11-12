# import tkinter as tk

# root = tk.Tk()
# matn1 = tk.Label(root, text="salom bu mening 1 tkinter dasturim!")
# matn1.pack()

# matn2 = tk.Label(root, text="Mening Ismmim Azizbek va man sensorika oquv markazida oqiyman")
# matn2.pack()

# matn3 = tk.Label(root, text="Man sensorika 1 oy oqiyman va python dasturlashni urgandim")
# matn3.pack()

# btn = tk.Button(root, text="stop")
# btn.pack()




# import tkinter as tk

# root = tk.Tk()

# tk.Label(root, text="First Name").grid(row=0, column=0)
# tk.Label(root, text="Last Name").grid(row=1, column=0)
# tk.Label(root, text="Age").grid(row=2, column=0)

# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)
# entry3 = tk.Entry(root)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# entry3.grid(row=2, column=1)

import tkinter as tk

def matn_chiqar(event):
    kiritilgan_matn = input1.get()
    text.config(text=f"Natija: {kiritilgan_matn}")

root = tk.Tk()
# geometry => ochiladigan oynaning width hamda height
root.geometry("400x500")

input1 = tk.Entry(root)
input1.pack(pady=25)

# <Return> => enter bosilganida
input1.bind('<Return>', matn_chiqar)

text = tk.Label(root, text="Natija bu yerda ko'rinadi")
text.pack(pady=5)



def calc(event):
    son_input = int(son.get())
    amal_input = amal.get().strip()
    raqam_input = int(raqam.get())

    result = 0

    if amal_input == "+":
        result = son_input + raqam_input
    elif amal_input == "-":
        result = son_input - raqam_input
    elif amal_input == "/":
        result = son_input // raqam_input
    elif amal_input == "*":
        result = son_input * raqam_input

    natija.config(text=f"Natija: {result}")

root = tk.Tk()
root.geometry('500x500')

son = tk.Entry(root, width=30, font=("Arial", 20))
son.pack(pady=10)

amal = tk.Entry(root, width=30, font=("Arial", 20))
amal.pack(pady=20)

raqam = tk.Entry(root, width=30, font=("Arial", 20))
raqam.pack(pady=10)

natija = tk.Label(root, text="Natija", font=("Arial", 24))
natija.pack(pady=10)

son.bind("<Return>", calc)
amal.bind("<Return>", calc)
raqam.bind("<Return>", calc)


root.mainloop()

