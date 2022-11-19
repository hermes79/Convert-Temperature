from tkinter import *
from tkinter.font import Font

#Define window + 'logo'
root = Tk()
#root.iconbitmap('python_ico.ico') use to replace logo of tkinter with one of your choice
root.geometry('300x300')


#Define fonts
my_font = Font(
    family='helvetica',
    slant= 'roman',
    weight= 'bold')

#Define Buttons Functions
         
def F():
    c = int(my_entry.get())
    cel = ((c * 9)/(5)) + 32
    convert_label2.config(text=cel)
                  

def clear():
    my_entry.delete(0,END)


#Define labels
main_label = Label(root, text='Convert Temperature', font=my_font, fg='blue')
main_label.pack(side=TOP)
convert_label2 = Label(root, text='', font=my_font)  
convert_label2.pack(side=BOTTOM, pady=20)


#Define entry
my_entry = Entry(root)
my_entry.pack()           
var = StringVar()


#Define buttons
clear_button = Button(root, text='CLEAR', command=clear, bg='red', fg='white', padx=20, pady=5)
clear_button.pack(padx=20, pady=10, side=LEFT, anchor=NW)
f_but = Button(root, text='C to  F', command=F, bg='black', fg='yellow', padx=20, pady=5)
f_but.pack(padx=20, pady=10, side=LEFT, anchor=NW)



root.mainloop()