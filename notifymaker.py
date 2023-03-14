from tkinter import *
import customtkinter
from plyer import notification


window = customtkinter.CTk()
window.geometry("350x200")
window.title("Notification Maker")
window.resizable(False, False)

a = customtkinter.CTkLabel(window, text="Notification Maker")
a.grid(row=0,column=0)

b = customtkinter.CTkLabel(window, text="Notification Title:")
b.grid(row=3,column=0)

c = customtkinter.CTkLabel(window, text="Notification Message:")
c.grid(row=4, column=0)

e = customtkinter.CTkLabel(window, text="Seconds for which it appears:")
e.grid(row=5, column=0)

e1 = customtkinter.CTkEntry(window)
e1.grid(row=3, column=1)

e2 = customtkinter.CTkEntry(window)
e2.grid(row=4, column=1)

e3 = customtkinter.CTkEntry(window)
e3.grid(row=5, column=1)

def start():
    x = int(e3.get())
    notification.notify(
    title = e1.get(),
    message = e2.get(),
    timeout = x  
)


button = customtkinter.CTkButton(window, text="Make Notification", command=start)
button.grid(row=6, column=0)
window.mainloop()