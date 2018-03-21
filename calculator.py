from tkinter import *


def  btclick(numbers):
    global operator
    operator=operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator=" "
    txt_input.set("")

def eq():
    global operator
    sumup=str(eval(operator))
    txt_input.set(sumup)
    operator=" "



cal =Tk()
cal.title("Calculator")
operator=" "
txt_input=StringVar()

txtdisplay = Entry(cal , font=("arial" , 20  ) , fg='green',textvariable=txt_input, bd=30, insertwidth=4,bg = "black" , justify='right').grid(columnspan=4)
#=======================================================================================================


menu = Menu(cal)
cal.config(menu=menu)

submenu=Menu(menu)
menu.add_cascade(label="Adv")
menu.add_cascade(label=".")
menu.add_cascade(label="This is a basic Calculator ~ ~ by Suyash ")


#=========================================================================================
b7=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='7',bg='black'  ,  command=lambda : btclick(7)).grid(row=1 , column=0)
b8=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='8',bg='black' ,  command=lambda : btclick(8)).grid(row=1 , column=1)
b9=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='9',bg='black' ,  command=lambda : btclick(9)).grid(row=1 , column=2)
badd=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='+',bg='black' ,  command=lambda : btclick('+')).grid(row=1 , column=3)
#=====================================================================================
#=========================================================================================
b4=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='4',bg='black' ,  command=lambda : btclick(4)).grid(row=2 , column=0)
b5=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='5',bg='black' ,  command=lambda : btclick(5)).grid(row=2 , column=1)
b6=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='6',bg='black' ,  command=lambda : btclick(6)).grid(row=2, column=2)
bsub=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='-',bg='black' ,  command=lambda : btclick('-')).grid(row=2 , column=3)
#=====================================================================================
#=========================================================================================
b1=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='1',bg='black' ,  command=lambda : btclick(1)).grid(row=3 , column=0)
b2=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='2',bg='black' ,  command=lambda : btclick(2)).grid(row=3 , column=1)
b3=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='3',bg='black' ,  command=lambda : btclick(3)).grid(row=3, column=2)
bmul=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='*',bg='black' ,  command=lambda : btclick('*')).grid(row=3 , column=3)
#=====================================================================================

#=========================================================================================
b0=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='0',bg='black' ,  command=lambda : btclick(0)).grid(row=4 , column=0)
bdiv=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='/',bg='black' ,  command=lambda : btclick('/')).grid(row=4 , column=1)
bcl=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='C',bg='black' ,command=clear ).grid(row=4, column=2)
beq=Button(cal , padx=16 , bd=8, fg ='green',  font=("arial" , 20 , "bold" ), text='=',bg='black'  ,command=eq ).grid(row=4 , column=3)
#=====================================================================================
cal.mainloop()
