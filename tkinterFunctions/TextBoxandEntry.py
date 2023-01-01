from tkinter import *

main = Tk()
main.title("Minji1201")
main.geometry('640x480+1000+300')
main.resizable(False, False)
##############

txt = Text(main, width=30, height=5) # creating textbox
txt.pack()
txt.insert(END, 'Insert Username') # inserting text in the textbox END=0

e = Entry(main, width=35) # entry can't make a new line by pressing enter
e.pack()

def btncmd():
    print(txt.get('1.0', END)) # 1:First Line 0:first column
    print(e.get())
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(main, text="Button", command=btncmd)
btn.pack()

main.mainloop()
