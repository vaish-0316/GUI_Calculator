#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
expression=""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
       
   
def clear():
    global expression
    expression = ""
    equation.set("")
   
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)
   
window = Tk()

window.configure(background="brown")
window.title("CALCULATOR")
window.geometry("408x316")
window.iconbitmap("Calculator_image.ico")

heading = Label(window,text = "CALCULATOR",background="brown",foreground="pink",font=('Times New Roman','11','italic',
                                                                                      'bold','underline'))
heading.grid(row=0,pady=10)

equation = StringVar()
expression_field = Entry(window, textvariable=equation,font='4')
expression_field.grid(columnspan=4)


btn_clear = Button(window,text="AC",bg="red",command=clear,height=1, width=7,font='4')
btn_clear.grid(row=2,pady=10)

btn_backspace = Button(window, text = "DEL", width= 7, height = 1, bg="red",command=backspace)
btn_backspace.grid(row = 2, column = 3)

btn_7 = Button(window,text="7",bg="pink",command=lambda: press(7),height=2, width=11,font='4')
btn_7.grid(row=3)

btn_8 = Button(window,text="8",bg="pink",command=lambda: press(8),height=2, width=10,font='4')
btn_8.grid(row=3,column=1)

btn_9 = Button(window,text="9",bg="pink",command=lambda: press(9),height=2, width=10,font='4')
btn_9.grid(row=3,column=2)

btn_divide = Button(window,text="/",bg="orange",command=lambda: press('/'),height=2, width=10,font='4')
btn_divide.grid(row=3,column=3)

btn_4 = Button(window,text="4",bg="pink",command=lambda: press(4),height=2, width=11,font='4')
btn_4.grid(row=4)

btn_5 = Button(window,text="5",bg="pink",command=lambda: press(5),height=2, width=10,font='4')
btn_5.grid(row=4,column=1)

btn_6 = Button(window,text="6",bg="pink",command=lambda: press(6),height=2, width=10,font='4')
btn_6.grid(row=4,column=2)

btn_multiply = Button(window,text="*",bg="orange",command=lambda: press('*'),height=2, width=10,font='4')
btn_multiply.grid(row=4,column=3)

btn_1 = Button(window,text="1",bg="pink",command=lambda: press(1),height=2, width=11,font='4')
btn_1.grid(row=5)

btn_2 = Button(window,text="2",bg="pink",command=lambda: press(2),height=2, width=10,font='4')
btn_2.grid(row=5,column=1)

btn_3 = Button(window,text="3",bg="pink",command=lambda: press(3),height=2, width=10,font='4')
btn_3.grid(row=5,column=2)

btn_plus = Button(window,text="+",bg="orange",command=lambda: press('+'),height=2, width=10,font='4')
btn_plus.grid(row=5,column=3)

btn_0 = Button(window,text="0",bg="light pink",command=lambda:press(0),height=2, width=11,font='4')
btn_0.grid(row=6)

btn_point = Button(window,text=".",bg="pink",command=lambda: press('.'),height=2, width=10,font='10')
btn_point.grid(row=6,column=1)

btn_equal = Button(window,text="=",bg="light green",command=equalpress,font='10',height=2, width=10)
btn_equal.grid(row=6,column=2)

btn_minus = Button(window,text="-",bg="orange",command=lambda: press('-'),height=2, width=10,font='4')
btn_minus.grid(row=6,column=3)


window.mainloop()


# In[ ]:




