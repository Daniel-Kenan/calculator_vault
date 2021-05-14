from tkinter import * 
import user, sys, fm
# from tkinter.font import Font
import re , os
from math import sqrt 
from user import check
window = Tk()
window.geometry("310x350")
window.title("CALCULATOR")
window.iconbitmap(sys.path[0] + "\\vault.ico")


def btn(row, column ,text , command = None, columnspan  = 1 ):
   if command == None:
       Button(window , text = text , command = lambda:screen.insert(END , text) , width=5 , height=3 , borderwidth=0 , border = 0 , ).grid(row = row , column = column )
   else :
       Button(window , text = text , command = command , width=5 , height=3 , borderwidth=0 , border = 0 , ).grid(row = row , column = column )
   Grid.rowconfigure(window, row , weight = 1)
   Grid.columnconfigure(window, column , weight = 1)


def equal_to(expression):
    e = expression
    e  = e.replace('x','*')
    e = e.replace('÷','/')
    e = e.replace('%','/100')
    # e = e.replace('√' , "sqrt")
    screen.delete(0,END)
    screen.insert(END,str(eval(e)))
    return eval(e) 

if check():
  screen = Entry(window , width= 50  )
  screen.grid(columnspan = 4 , ipady =15 , pady=5)

  btn(3 , 0 , "%" ,)
  btn(3 , 1 , "√" , lambda:root())

  def root():
    if open('vault.txt ').readlines()[0] !=  screen.get():
      x = equal_to(screen.get())
      screen.delete(0,END)
      equal_to(str(sqrt(x)))
    else: 
      for widget in window.winfo_children():
          widget.destroy()
      Button(window , text="RETRIEVE FILES " , command=fm.retrieve , borderwidth=2).grid(row=0 , column =1 )
      Button(window , text = "HIDE FILES" ,command=fm.classify , borderwidth=2 ).grid(row=1 , column=1)
      
      

  btn(3 , 2 , "x^2" , lambda:square())
  
  def square():
    x = equal_to(screen.get())
    screen.delete(0,END)
    screen.insert(END,x*x)


    # numbers
  btn(4,0,1,)
  btn(4,1,2)
  btn(4,2,3)
  btn(5,0,4)
  btn(5,1,5)
  btn(5,2,6)
  btn(6,0,7)
  btn(6,1,8)
  btn(6,2,9)

  # operators
  btn(3,3,"÷")
  btn(4,3,"x")
  btn(5,3,"+")
  btn(6,3,"-") 
  btn(7,3,"=" ,lambda:equal_to(screen.get())) 

# continuos
  btn(7,0,"clear" ,lambda:clear())

  def clear():
    screen.delete(0, END)

  btn(7,1,"0")
  btn(7,2,".")

else:
    Label(window , text ="CREATE NEW PINCODE").pack(pady = 5)
    pin = Entry(window)
    pin.pack()
    # pin.insert(END , '')
    def submit():
        global pin
       
        if not re.search(r'[A-z]',pin.get()):
           pin = pin.get() 
           with open('vault.txt','w') as authority:
             authority.write(pin)
             os.system(f'cd {fm.EXECUTION_PATH} && attrib +s +h vault.txt')
             Label(window, 
             text="now you can type your pincode on the calculator and press √ . restart the application").pack()
        else:
            pin.delete(0,END)
            pin.insert(END,"numbers only")

    Button(window , text = "submit" , command=submit).pack()
    
      
window.mainloop()