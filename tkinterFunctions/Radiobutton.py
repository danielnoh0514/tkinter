from tkinter import*

main = Tk()
main.title('Minji1201')
main.geometry('640x480+1000+400')
main.resizable(False, False)
#

Label(main, text="Choose Your Food").pack()

food_var = IntVar()
btn1 = Radiobutton(main, text="Hamburger", value=1, variable=food_var)
btn1.select()
btn2 = Radiobutton(main, text="Spaghetti", value=2, variable=food_var)
btn3 = Radiobutton(main, text="Pizza", value=3, variable=food_var)

btn1.pack()
btn2.pack()
btn3.pack()

Label(main, text="Choose Your Drink").pack()
drink_var = StringVar()
btn_drink_1 = Radiobutton(main, text='Coke', value='Coke', variable=drink_var)
btn_drink_1.select()
btn_drink_2 = Radiobutton(main, text='Fanta', value='Fanta', variable=drink_var)

btn_drink_1.pack()
btn_drink_2.pack()

def btncmd():
    print(food_var.get())
    print(drink_var.get())


btn = Button(main, text='Order', command=btncmd)
btn.pack()

main.mainloop()
