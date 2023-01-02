from tkinter import*
import tkinter.ttk as ttk
import time

main = Tk()
main.title('Minji1201')
main.geometry('640x480+1000+400')
main.resizable(False, False)
#

# progressbar = ttk.Progressbar(main, maximum=100, mode='indeterminate')
# progressbar = ttk.Progressbar(main, maximum=100, mode='determinate')
# progressbar.start(5)
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()

def btncmd():
    for i in range(101):
        time.sleep(0.01)
        var2.set(i)
        progressbar2.update()


var2 = DoubleVar()
progressbar2 = ttk.Progressbar(main, maximum=100, mode='indeterminate', length=150, variable=var2)
progressbar2.pack()

btn = Button(main, text='Start', command=btncmd)
btn.pack()

main.mainloop()
