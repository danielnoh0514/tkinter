from tkinter import *

main = Tk()
main.title("Minji1201")
main.geometry('640x480+1000+300')
main.resizable(False, False)
##############

label1 = Label(main, text='Hola')
label1.pack()

photo = PhotoImage(file = 'check.png')
label2 = Label(main, image=photo)
label2.pack()


def change():
    label1.config(text="안녕") # changes label1 text from Hola to 안녕
    global photo2 # use global for garbage collection
    photo2 = PhotoImage(file='wrong.png ')
    label2.config(image=photo2)

btn = Button(main, text="Click Me", command=change)
btn.pack()


main.mainloop()
