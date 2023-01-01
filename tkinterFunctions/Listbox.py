  from tkinter import *

main = Tk()
main.title("Minji1201")
main.geometry('640x480+1000+300')
main.resizable(False, False)
##############

# selectmode = 'extended'
# height=0 -> shows all components in the listbox

listbox = Listbox(main, selectmode='single', height=0)
listbox.insert(0,'Strawberry')
listbox.insert(1,'Apple')
listbox.insert(2,'Grape')
listbox.insert(3,'Banana')
listbox.pack()

def btncmd():
    # Deletion
    # END -> delete from the end    0-> delete from the beginning
    # listbox.delete(END)

    # Amount Check
    # print(f'리스트에는 {listbox.size()} 개가 있어요')

    # Item Check
    # print(f'1-3 Items {listbox.get(0,2)}')

    # Currently Selected Item
    print(f'Currently Selected Item is {listbox.curselection()}')
    
btn = Button(main, text="Button", command=btncmd)
btn.pack()

main.mainloop()
