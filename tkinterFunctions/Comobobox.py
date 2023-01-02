from tkinter import*
import tkinter.ttk as ttk

main = Tk()
main.title('Minji1201')
main.geometry('640x480+1000+400')
main.resizable(False, False)
#

values = [str(i) + "일" for i in range(1,32)]

# combobox.current(0) -> selects the first item in the combobox
combobox = ttk.Combobox(main, height=5, values=values, state='readonly')
combobox.pack()
combobox.set('Card Payment Date')


def btncmd():
    print(combobox.get())


btn = Button(main, text='Select', command=btncmd)
btn.pack()

main.mainloop()
