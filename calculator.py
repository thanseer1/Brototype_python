from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry( '400x600' )
frame = LabelFrame(
    window,
    text='calculator',
    bg='#f0f0f0',
    font=(30)
)
expression = ""
def display(value):
    global expression
    expression = expression + str(value)
    equation.set(expression)
    
def clear_d():
    global expression
    expression=" "
    equation.set(" ")
    

def calculus():
    global expression
    total = str(eval(expression))
           
    equation.set(total)
    expression=total
    
def delete():
    global expression
    x=equation.get()[:-1]
    equation.set(equation.get()[:-1])
    expression=x
   
       


equation = StringVar()
T = Entry(frame, width = 52,textvariable=equation,font=('Arial 30'),state=DISABLED)
T.pack(padx=10, pady=10)

clear = Button(frame, text = 'C',height = 2, width = 7, command=lambda:clear_d())
clear.place(x = 30, y = 100)
div = Button(frame, text = '/',height = 2, width = 7,command=lambda: display("/"))
div.place(x = 130, y = 100)
mul = Button(frame, text = 'X',height = 2, width = 7,command=lambda: display("*"))
mul.place(x = 230, y = 100)
sub = Button(frame, text = '-',height = 2, width = 7,command=lambda: display("-"))
sub.place(x = 330, y = 100)

btn7 = Button(frame, text = '7',height = 2, width = 7,command=lambda: display("7"))
btn7.place(x = 30, y = 200)
btn8 = Button(frame, text = '8',height = 2, width = 7,command=lambda: display("8"))
btn8.place(x = 130, y = 200)
btn9 = Button(frame, text = '9',height = 2, width = 7,command=lambda: display("9"))
btn9.place(x = 230, y = 200)
add = Button(frame, text = '+',height = 9, width = 7,command=lambda: display("+"))
add.place(x = 330, y = 200)

btn4 = Button(frame, text = '4',height = 2, width = 7,command=lambda: display("4"))
btn4.place(x = 30, y = 300)
btn5 = Button(frame, text = '5',height = 2, width = 7,command=lambda: display("5"))
btn5.place(x = 130, y = 300)
btn6 = Button(frame, text = '6',height = 2, width = 7,command=lambda: display("6"))
btn6.place(x = 230, y = 300)

btn1 = Button(frame, text = '1',height = 2, width = 7,command=lambda: display("1"))
btn1.place(x = 30, y = 400)
btn2 = Button(frame, text = '2',height = 2, width = 7,command=lambda: display("2"))
btn2.place(x = 130, y = 400)
btn3 = Button(frame, text = '3',height = 2, width = 7,command=lambda: display("3"))
btn3.place(x = 230, y = 400)
equal = Button(frame, text = '=',height = 9, width = 7,command=lambda: calculus())
equal.place(x = 330, y = 400)

zero = Button(frame, text = '0',height = 2, width = 7,command=lambda: display("0"))
zero.place(x = 30, y = 500)
deel = Button(frame, text = 'Del',height = 2, width = 7,command=lambda: delete())
deel.place(x = 130, y = 500)
point = Button(frame, text = '.',height = 2, width = 7,command=lambda: display("."))
point.place(x =230, y = 500)

frame.pack(expand=True, fill=BOTH)
T.pack()

window.mainloop()