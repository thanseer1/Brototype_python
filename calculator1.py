from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry( '400x600' )
window.resizable(0,0)
frame = LabelFrame(
    window,
    text='calculator',
    bg='#f0f0f0',
    font=(30)
)

T1=StringVar(window)
    
def clear_d():
    T.delete(0,END)

def calculus():
     v=T.get()
     cal=eval(v)
     T.delete(0,END)
     T.insert(0, cal)

def delete():
        a = T.get()
        T.delete(first=len(a)-1,last="end")    

equation = StringVar()
T = Entry(frame, width = 52,font=('Arial 30'),cursor="circle",textvariable=T1,)
T.pack(padx=10, pady=10)

clear = Button(frame, text = 'C',height = 2, width = 7, command=lambda:clear_d() )
clear.place(x = 30, y = 100)
div = Button(frame, text = '/',height = 2, width = 7,command=lambda: T.insert("end","/") )
div.place(x = 130, y = 100)
mul = Button(frame, text = 'X',height = 2, width = 7,command=lambda:T.insert("end","*"))
mul.place(x = 230, y = 100)
sub = Button(frame, text = '-',height = 2, width = 7,command=lambda: T.insert("end","-"))
sub.place(x = 330, y = 100)

btn7 = Button(frame, text = '7',height = 2, width = 7,command=lambda: T.insert("end","7"))
btn7.place(x = 30, y = 200)
btn8 = Button(frame, text = '8',height = 2, width = 7,command=lambda: T.insert("end","8"))
btn8.place(x = 130, y = 200)
btn9 = Button(frame, text = '9',height = 2, width = 7,command=lambda: T.insert("end","9"))
btn9.place(x = 230, y = 200)
add = Button(frame, text = '+',height = 9, width = 7,command=lambda: T.insert("end","+"))
add.place(x = 330, y = 200)

btn4 = Button(frame, text = '4',height = 2, width = 7,command=lambda: T.insert("end","4"))
btn4.place(x = 30, y = 300)
btn5 = Button(frame, text = '5',height = 2, width = 7,command=lambda: T.insert("end","5"))
btn5.place(x = 130, y = 300)
btn6 = Button(frame, text = '6',height = 2, width = 7,command=lambda: T.insert("end","6"))
btn6.place(x = 230, y = 300)

btn1 = Button(frame, text = '1',height = 2, width = 7,command=lambda: T.insert("end","1"))
btn1.place(x = 30, y = 400)
btn2 = Button(frame, text = '2',height = 2, width = 7,command=lambda: T.insert("end","2"))
btn2.place(x = 130, y = 400)
btn3 = Button(frame, text = '3',height = 2, width = 7,command=lambda: T.insert("end","3"))
btn3.place(x = 230, y = 400)
equal = Button(frame, text = '=',height = 9, width = 7,command=lambda: calculus())
equal.place(x = 330, y = 400)

zero = Button(frame, text = '0',height = 2, width = 7,command=lambda: T.insert("end","0"))
zero.place(x = 30, y = 500)
delete1 = Button(frame, text = 'Del',height = 2, width = 7,command=lambda: delete())
delete1.place(x = 130, y = 500)
point = Button(frame, text = '.',height = 2, width = 7,command=lambda: T.insert("end","."))
point.place(x = 230, y = 500)


frame.pack(expand=True, fill=BOTH)
T.pack()

window.mainloop()