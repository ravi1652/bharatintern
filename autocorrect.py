from textblob import TextBlob
from tkinter import *



def Auto_correct():
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i).correct())
    Output_text.delete(1.0, END)
    for i in corrected_words:
        Output_text.insert(END, i + " ")

def Clear():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)


    
    
mainwin = Tk()

mainwin.geometry('1500x700')

mainwin.resizable(False, False)

mainwin.title("Auto Correct")

mainwin.config(bg='#c09999')

Label(mainwin, text="Auto Correction Tool", font='arial 25 bold', bg= '#c09999').place(x=540, y=30)

Label(mainwin, text="Please Enter your Text here", font='arial 18 bold', bg= '#c09999').place(x=280, y=90)

Input_text = Text(mainwin, font='arial 13', bg='white', height=13, wrap=WORD, padx=5, pady=5, width=60, insertbackground='black')

Input_text.place(x=80, y=130)

Label(mainwin, text="Corrected Text", font='arial 18 bold', bg= '#c09999').place(x=980, y=90)

Output_text = Text(mainwin, font='arial 13', bg='white', height=13, wrap=WORD, padx=5, pady=5, width=60, insertbackground='black')

Output_text.place(x=770, y=130)

auto_correct_btn = Button(mainwin, text="Correct", bg='lavender blush', width=30, font='arial 18 bold', pady=3, command=Auto_correct)

auto_correct_btn.place(x=240, y=420)

c1 = Button(mainwin, text="Clear", width=30, pady=3, bg='lavender blush', font='arial 18 bold', command=Clear)

c1.place(x=710, y=419)

mainwin.mainloop()