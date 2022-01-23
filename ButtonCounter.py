#Program updates simple UI everytime the button is clicked
#Written by Ishaan Bahl/Illusion
#Uses the python tkinter and PIL modules

from tkinter import *
from PIL import Image, ImageTk

global number
number = 0

#Main
window = Tk()
window.title("Button Clicker")
window.configure(background="#262626")
window.geometry("500x500")

def Counter():
    global number
    number += 1  

    number_label.config(text=number)

#image for button
image = Image.open("PracticeProjects/Images/blue-button.png")
resize_image = image.resize((500, 500))
img = ImageTk.PhotoImage(resize_image)

#Number Display
number_label = Label(window, text='0', font=('Tahoma', 44))
number_label.pack(pady=10)

#Button
button = Button(window, text='Click me!', image = img)
button.config(command=Counter, bg="#262626")
button.pack()

#Runs Window
window.mainloop()