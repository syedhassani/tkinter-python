from tkinter import *
window=Tk()
window.title("coding")
window.geometry("400x400")
lable=Label(text=" welcome to coding",fg="green" , bg="red")
lable.pack()

button=Button (text=" click me to see more codes",fg="red" , bg="yellow")
button.pack()


entry=Entry(fg="red" , bg="yellow")
entry.pack()

window.mainloop()