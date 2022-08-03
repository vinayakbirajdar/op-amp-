from tkinter import*
root=Tk()
root.geometry("780x500")
root.minsize(500,500)
#FUNCTIONS
def hello():
    vb_1=Label(f0,text=("This is an closed loop inverting op amp with negative feedback"),
               font=("comicsansms","30"),fg="white",bg="black")
    vb_1.pack()
def he():
    vb_2=Label(f0,text=("Formula FOR GAIN : -RF\R1 \nFormula for total output :V0=G(vid),"
                        "[Here vid = v1-v2] so as v2 is connected \nto ground therefore"
                        "V0=G(-V1)"),
               font=("comicsansms","20"),fg="white",bg="black")
    vb_2.pack()
def rf():
    get_1=ent.get()
    vb_4 =Label(f1,text=("The given feedback resistance is  :",(get_1)))                  
    vb_4.pack()
def r_1():
    get_2=ent_1.get()
    vb_5 =Label(f1,text=("The given R1 resistance is  :",(get_2)))         
    vb_5.pack()
def cal():
    t_1=int(ent.get())
    t_2=int(ent_1.get())

    vb_6 =Label(f1,text=("the output is :" ,(t_1/t_2)*(-1)),font=("comicsansms","30")
                ,bg="white",fg="black")
    vb_6.pack()
   
photo=photo = PhotoImage(file = '//Users//vinayakbirajdar//Desktop//image//opamp.png')
p_1 = Label(image=photo)
p_1.pack()
ent=Entry()
ent.config(font=("ink free",30))
ent.pack(side=BOTTOM)
#TEXT
us_1=Label(text="$RF$",font=("comicsansms","40"))
us_1.pack(side=BOTTOM)
#ENTRY
ent_1=Entry()
ent_1.config(font=("ink free",30))
ent_1.pack(side=BOTTOM)
#TEXT
us_1=Label(text="$R1$",font=("comicsansms","40"))
us_1.pack(side=BOTTOM)
#FRAME
f2 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f2.pack(fill="y",side="left")
f1 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f1.pack(fill="y",side="right")
f0 = Frame(root,borderwidth=3,bg="gray",relief="groove",height='100')
f0.pack(fill="x",side="top")
f3 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='100')
f3.pack(fill="x",side="bottom")
vb_3=Label(f3,text=("As this is an inverting op apm let us calculate the gain of op amp"
                "to calculate teh gain \nof op amp we need R1 and R2 so kindly put the value"
                "of R1 and R2 below the entry widget"),font=("comicsansms","20"),fg="white",
                 bg="black")
vb_3.pack()
#BUTTON
b1=Button(f2,fg='green',text="#INFO#",font=("comicsansms","30"),relief = GROOVE,command=hello)
b1.pack()

b2=Button(f2,fg='green',text="#HINT#",font=("comicsansms","30"),relief = GROOVE,command=he)
b2.pack()
b3=Button(f2,fg='green',text="#R1 SUBMIT#",font=("comicsansms","30"),relief = GROOVE,
          command=r_1)
b3.pack()

b4=Button(f2,fg='green',text="#RF SUBMIT#",font=("comicsansms","30"),relief = GROOVE,
          command=rf)
b4.pack()

b5=Button(f2,fg='green',text="opamp.GAIN#",font=("comicsansms","30"),relief = GROOVE,
          command=cal)
b5.pack()
b_1=Label(text="CREATED BY suryakant birajdar ROLL NO=03 [ELN S.Y]",font=("comicsansms","30"))
b_1.pack()
root.mainloop()

