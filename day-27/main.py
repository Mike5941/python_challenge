from tkinter import *
#
def button_clicked():
    miles = int(miles_value.get()) * 1.609
    km_value.config(text=str(miles))




window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(pady=30)

label = Label(text="is equal to ")
window.config(padx=30)
label.grid(column=0, row=1)

miles_value = Entry(width=10)
miles_value.insert(ANCHOR, string="0")
miles_value.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


























# Label

# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)
#
#
# # Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button", command=button_clicked)
# new_button.grid(column=2, row=0)
#
# # Entry
# input = Entry(width=10)
# input.grid(column=3, row=3)






window.mainloop()