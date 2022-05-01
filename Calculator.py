from tkinter import *
import re

show_text = ""

def set_ex(exp):
    global show_text
       
    show_text = show_text + str(exp)
    expression.set(show_text)
    

def show_res():
    
    try:
        global show_text
        result = re.sub('^0*|(?<=[-\+\*/])0*', '', entry_field.get())
        result = eval(result)
        #result = eval(entry_field.get())
        expression.set(result)
        show_text = str(result)
    except:
        expression.set("Syntax Error !")
        show_text = ""

def clear_all():
    global show_text
    expression.set('')
    show_text = ""

def delete():
    global show_text
    length = len(show_text)
    st = show_text[0:length-1]
    show_text = st
    expression.set(show_text)
    

if __name__=="__main__":
    main = Tk()

    main.title('Calculator')
    main.configure(bg='#fff')
    main.geometry('264x248')
    main.iconbitmap("C:\\Users\\Abhishek\\Desktop\\python\\Exercise\\Calculator\\cal.ico")
    main.resizable(0,0)
    main.overrideredirect(0)

    #.....creating widgets........
    expression = StringVar()
    entry_field = Entry(main, textvariable = expression)
    entry_field.grid(columnspan=4,row=0,ipady=12,ipadx=70)

    b_1 = Button(main,text = '1',command =lambda: set_ex('1'),height=2, width=8)
    b_1.grid(column=0,row=1)

    b_2 = Button(main,text = '2',command =lambda: set_ex('2'),height=2, width=8)
    b_2.grid(column=1,row=1)

    b_3 = Button(main,text = '3',command =lambda: set_ex('3'),height=2, width=8)
    b_3.grid(column=2,row=1)

    b_4 = Button(main,text = '4',command =lambda: set_ex('4'),height=2, width=8)
    b_4.grid(column=0,row=2)

    b_5 = Button(main,text = '5',command =lambda: set_ex('5'),height=2, width=8)
    b_5.grid(column=1,row=2)

    b_6 = Button(main,text = '6',command =lambda: set_ex('6'),height=2, width=8)
    b_6.grid(column=2,row=2)

    b_7 = Button(main,text = '7',command =lambda: set_ex('7'),height=2, width=8)
    b_7.grid(column=0,row=3)

    b_8 = Button(main,text = '8',command =lambda: set_ex('8'),height=2, width=8)
    b_8.grid(column=1,row=3)

    b_9 = Button(main,text = '9',command =lambda: set_ex('9'),height=2, width=8)
    b_9.grid(column=2,row=3)

    b_0 = Button(main,text = '0',command =lambda: set_ex('0'),height=2, width=8)
    b_0.grid(column=1,row=4)

    b_plus = Button(main,text = '+',command =lambda: set_ex('+'),height=2, width=8)
    b_plus.grid(column=3,row=1)

    b_minus = Button(main,text = '-',command =lambda: set_ex('-'),height=2, width=8)
    b_minus.grid(column=3,row=2)

    b_mul = Button(main,text = 'x',command =lambda: set_ex('*'),height=2, width=8)
    b_mul.grid(column=3,row=3)

    b_div = Button(main,text = '/',command =lambda: set_ex('/'),height=2, width=8)
    b_div.grid(column=3,row=4)

    b_dec = Button(main,text = '.',command =lambda: set_ex('.'),height=2, width=8)
    b_dec.grid(column=0,row=4)

    b_res = Button(main,text = 'Result',command =lambda: show_res(),height=2, width=27)
    b_res.grid(columnspan=3,row=5)

    b_ac = Button(main,text = 'AC',command =lambda: clear_all(),height=2, width=8)
    b_ac.grid(column=2,row=4)

    b_del = Button(main,text = 'DEL',command =lambda: delete(),height=2, width=8)
    b_del.grid(column=3,row=5)


    main.mainloop()
