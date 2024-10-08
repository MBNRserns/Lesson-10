from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Multiplication")

title=Label(root, text = "Mathematical Table")
title.grid(row=0, column=0, columnspan=3, pady=25)

caption=Label(root, text= "Number and Range")
caption.grid(row=1, column=0, padx=10)

theNum = IntVar()
numbers=Combobox(root,textvariable= theNum,width=5)
numbers['values'] = tuple(range(101))
numbers.grid(row=1,column=1)

endVal = IntVar()
r10=Radiobutton(root,text="10",variable=endVal,value=10)
r10.grid(row=1,column=2)
r20=Radiobutton(root,text="20",variable=endVal,value=20)
r20.grid(row=2,column=2)
r30=Radiobutton(root,text="30",variable=endVal,value=30)
r30.grid(row=3,column=2)
endVal.set(10)

def genTable():
    tabels=""
    for i in range(endVal.get()+1):
        tabels += str(theNum.get())+"    X    "+str(i)+"    =    "+str(theNum.get()*i)+"\n"
    table.configure(text=tabels)
        

btn=Button(root, text="Calculate", command=genTable)
btn.grid(row=4, column=1)

table=Label(root, anchor="center")
table.grid(row=5,column=1,pady=25)

root.mainloop()