from tkinter import *

main = Tk()
main.title("Minji1201")
main.geometry('640x480+1000+300')
main.resizable(False, False)
##############

chkvar = IntVar()
checkbox = Checkbutton(main, text="Do not show until tomorrow", variable=chkvar)
checkbox.select() # checkbox is selected
checkbox.deselect() # checkbox is deselected
checkbox.pack()

def btncmd():
    print(chkvar.get())

btn = Button(main, text="Button", command=btncmd)
btn.pack()

main.mainloop()
