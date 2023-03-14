from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
GUI =Tk() #คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #คือชื่อโปรแกรม
GUI.geometry( '500x400' ) #คือขนาดโปรแกรม
L1 = Label (GUI,text='โปรแกรมบันทึกทรัพย์สิน',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

#########
def Button2 () :
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place (x=200,y=200)
B2 = ttk.Button (FB1,text= 'มีเงินอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=20)
B2.pack(ipadx=20,ipady=20,padx=40,pady=35)

def Button3 () :
    text = 'ตอนนี้มีเงินในหุ้นอยู่ 30,000 บาท'
    messagebox.showinfo('เงินในหุ้น',text)

FB2 = LabelFrame(GUI,text='หุ้น') #คล้ายกระดาน
FB2.place (x=200,y=400)
B3 = ttk.Button (FB2,text= 'มีเงินอยู่ในหุ้นกี่บาท',command=Button3)
#B3.pack(ipadx=20,ipady=20)
B3.pack(ipadx=30,ipady=30,padx=40,pady=35)

def Button4 () :
    text = 'ตอนนี้มีเงินในกองทุนอยู่ 300,000 บาท'
    messagebox.showinfo('เงินในกองทุน',text)

FB3 = LabelFrame(GUI,text='กองทุน') #คล้ายกระดาน
FB3.place (x=400,y=400)
B4 = ttk.Button (FB3,text= 'มีเงินอยู่ในกองทุนกี่บาท',command=Button4)
#B4.pack(ipadx=20,ipady=20)
B4.pack(ipadx=30,ipady=30,padx=40,pady=35)


GUI.mainloop()
