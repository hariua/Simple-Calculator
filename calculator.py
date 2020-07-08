from tkinter import *

window=Tk()
window.title("Simple Calculator")
window.configure(bg="violet")
value=""
txt=StringVar()


entry=Entry(window,textvariable=txt,bg="powderblue",bd=5).grid(columnspan=4,padx=15,pady=15)


btn7=Button(window,text="7",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("7")).grid(row=2,column=0)
btn8=Button(window,text="8",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("8")).grid(row=2,column=1)
btn9=Button(window,text="9",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("9")).grid(row=2,column=2)
btna=Button(window,text="+",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("+")).grid(row=2,column=3)


btn4=Button(window,text="4",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("4")).grid(row=3,column=0,pady=2)
btn5=Button(window,text="5",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("5")).grid(row=3,column=1)
btn6=Button(window,text="6",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("6")).grid(row=3,column=2)
btns=Button(window,text="-",padx=7,pady=3,font=("arial",10,"bold"),command=lambda :action_click("-")).grid(row=3,column=3)

btn1=Button(window,text="1",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("1")).grid(row=4,column=0)
btn2=Button(window,text="2",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("2")).grid(row=4,column=1)
btn3=Button(window,text="3",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("3")).grid(row=4,column=2)
btnm=Button(window,text="*",padx=6,pady=3,font=("arial",10,"bold"),command=lambda :action_click("*")).grid(row=4,column=3)


btnc=Button(window,text="C",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :clear("c")).grid(row=5,column=0,pady=2)
btn0=Button(window,text="0",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_click("0")).grid(row=5,column=1)
btne=Button(window,text="=",padx=5,pady=3,font=("arial",10,"bold"),command=lambda :action_result("=")).grid(row=5,column=2)
btnd=Button(window,text="/",padx=6,pady=3,font=("arial",10,"bold"),command=lambda :action_click("/")).grid(row=5,column=3)


window.mainloop()