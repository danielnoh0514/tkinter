from tkinter import *

main = Tk()
main.title("Coding")
main.geometry('640x480+1000+300')
main.resizable(False, False)

btn1 = Button(main, text="Button 1")
btn1.pack()

btn2 = Button(main, padx=5, pady=10, text="Button 2")
btn2.pack()

btn4 = Button(main, width=10, height=3, text="Button 4") # w,h is fixed
btn4.pack()

btn5 = Button(main, fg='red', bg='yellow', text="Button 5") # bg = background
btn5.pack()

photo = PhotoImage(file='check.png')
btn6 = Button(main, image=photo)
btn6.pack()

# Command Function
def btncmd():
    print('Button is Activated')

btn7 = Button(main, text="Button", command = btncmd)
btn7.pack()

main.mainloop()
