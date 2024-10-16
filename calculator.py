import tkinter
from tkinter import *


#intializing the main window and setting the title , size and color of the window
window = Tk()
window.title("Calculator")
window.geometry("570x600")
window.configure(bg = "#030001")

#creating a string variable to hold the entered expression
equation_text =""

#creating a string variable to hold the text for label 
equation_label = StringVar()

#creating a label  to display the expression
label = Label(window, textvariable= equation_label,height = 2,width= 25,bg ="white",fg = "black",font = ("arial",20))
label.pack()

# function to update the expression in the label 
def button_click(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


#function to evaluate the final expression
def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total


    except SyntaxError:   

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""


#function to clear the input
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""



#buttons for calculator
clear_button = Button(window,text = "C" , width=5,height=1,font = ("arial",30,"bold"),fg= "white",bg="orange",command=clear).place(x= 10,y =100)
power      = Button(window,text="x^2",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click("**")).place(x=150,y=100)
percentage = Button(window,text="%",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('%')).place(x=290,y=100)
div        = Button(window,text="/",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('/')).place(x=430,y=100)

button_7 = Button(window,text="7",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(7)).place(x=10,y=200)
button_8 = Button(window,text="8",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(8)).place(x=150,y=200)
button_9 = Button(window,text="9",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(9)).place(x=290,y=200)
mul      = Button(window,text="*",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('*')).place(x=430,y=200)

button_4 = Button(window,text="4",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(4)).place(x=10,y=300)
button_5 = Button(window,text="5",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(5)).place(x=150,y=300)
button_6 = Button(window,text="6",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(6)).place(x=290,y=300)
sub      = Button(window,text="-",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('-')).place(x=430,y=300)

button_1 = Button(window,text="1",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(1)).place(x=10,y=400)
button_2 = Button(window,text="2",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(2)).place(x=150,y=400)
button_3 = Button(window,text="3",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(3)).place(x=290,y=400)
add      = Button(window,text="+",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('+')).place(x=430,y=400)


decimal  = Button(window,text=".",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click('.')).place(x=10,y=500)
button_0 = Button(window,text="0",width=5,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=lambda:button_click(0)).place(x=150,y=500)
equal    = Button(window,text="=",width=10,height=1,font=("arial",30,"bold"),fg="white",bg="#444444",command=equals).place(x=300,y=500)


window.mainloop()
