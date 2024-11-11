from tkinter import *
from tkinter import Tk
from googletrans import Translator, LANGUAGES
root= tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('logo simpli.ico')
root['bg']='black'

root.title('language translator by SImplilearn')
label(root, text = "language Translator" , font = "arial 20 bold").pack()
label(root,text="Enter Text",font ='arial 13 bold',bg = 'white smoke').place(x=165, y=90)
Input_text=Entry(root,width=60)
Input_text.place(x=30,y=130)
Input_text.get()

label(root,text="output",font = 'arial 13 bold', bg='white smoke').place(x=789,y=95)
Output_text=Text(root , font='arial 10',height=11,wrap=WORD,padx=5,width=50)
Output.text.place(x= 600, y=180)
language = list(LANGUAGES.values())

dest_lang=ttk.combobox(root , values =language, width = 22)
dest_lang.place(x=130, y=180)
dest_lang.set('choose language')

def Translate():
    translator= translator()
    translated= translator. translate(text=Input_text.get(), dest= dest_lang.get())
    Out_text.delete(1.0, END) 
    Output_text.insert(END, translated.text)


trans_btn=Button(root, text='Translate', font='arial 12 bold', pady = 5,command= Translate, bg= 'orange', activebackground='green')
trans_btn.place(x=445 ,y=180)

root.mainloop()
