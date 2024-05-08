'''Created on May 2 2018.

@author: Alex & Nadia
'''
#! /usr/bin/env python
#  -*- coding: utf-8 -*-
    
import fileinput
import time
import sys
from tkinter import Tk, PhotoImage, Frame, Text, Label, Entry, Button, Scrollbar, Menu, messagebox
from tkinter.constants import WORD, END, DISABLED, NORMAL, RIGHT, Y
from tkinter.filedialog import askopenfilename, asksaveasfilename
from bitstring import BitArray
import matplotlib.pyplot as plt

import Golomb
import About
import tkinter.ttk as ttk

ftype = [('Text files', '*.txt')]

z1 = []
z2 = []
k1 = []
k2 = []
m1 = []
m2 = []


def difficulty():
    global z1, z2, k1, k2, m1, m2

    f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='col', sharey='row')
    f.suptitle('Asymptotic Complexity')
    ax1.plot(z2, z1)
    ax2.plot(k2, k1)
    ax3.plot(m2, m1)
    ax1.set(title='First postulate')
    ax2.set(ylabel='time (s)', title='Second postulate')
    ax3.set(xlabel='number of elements', title='Third postulate')
    
    plt.show()


def _close(event):
    root.destroy()


def _help():
    About.show()


def _open():
    op = askopenfilename(filetypes=ftype)
    Entry1_1.delete(0, END)
    Entry2_1.delete(0, END)
    Entry3_1.delete(0, END)
    for l in fileinput.input(op):
        Entry1_1.insert(END, l)
        Entry2_1.insert(END, l)
        Entry3_1.insert(END, l)


def openAndProcess1(event):
    op = askopenfilename(filetypes=ftype)
    Entry1_1.delete(0, END)
    for l in fileinput.input(op):
        Entry1_1.insert(END, l)
    firstPostulate(event, Entry1_1.get())

    
def openAndProcess2(event):
    op = askopenfilename(filetypes=ftype)
    Entry2_1.delete(0, END)
    for l in fileinput.input(op):
        Entry2_1.insert(END, l)
    secondPostulate(event, Entry2_1.get())

    
def openAndProcess3(event):
    op = askopenfilename(filetypes=ftype)
    Entry3_1.delete(0, END)
    for l in fileinput.input(op):
        Entry3_1.insert(END, l)
    thirdPostulate(event, Entry3_1.get())


def openBinary():
    messagebox.showwarning('Attention!', 'Processing can take some time')
    s = ''
    
    Label4 = Label(root)
    Label4.place(x=root.winfo_width() / 2 - 100, y=root.winfo_height() / 2, height=50, width=200)
    Label4.configure(text='Work in progress...')
    
    btime = []
    bnumber = []
    st = ''
    s = ''
    x = 10
    op = askopenfilename()
    with open(op, "rb") as f:
        i = 0  
        for z in range(10):
            s = f.read(x)
            st = st + 'File read... \n'
            print('File read...')
            c = BitArray(s)
            st = st + 'Bit array formed... \n'
            print('Bit array formed...')
            t1 = time.time()
            st = st + 'Marked start time and started work... \n'
            print('Marked start time and started work...')
            mesneResults = Golomb.Golomb(c.bin)
            t2 = time.time()
            btime.append(t2 - t1)
            bnumber.append(len(s))
            x = x * 2
            st = st + 'Iteration No.' + str(i) + '\n'
            print('Iteration No.' + str(i))
            st = st + str(mesneResults) + '\n'
            print(mesneResults)
            i = i + 1
            s = ''
    st = st + str(bnumber) + '\n'
    print(bnumber)
    st = st + str(btime) + '\n'
    print(btime)
    
    f = open('test.txt', 'w')
    f.write(st)
    f.close()
    
    Label4.destroy()
    
    f, ax = plt.subplots()
    ax.plot(bnumber, btime)
    ax.set(title='Algorithm speed', ylabel='time (s)', xlabel='number of elements')
    ax.grid()
    
    plt.show()

def _save():
    sa = asksaveasfilename(filetypes=ftype)
    letter = Text1_2.get(1.0, END)
    letter1 = Text2_2.get(1.0, END)
    letter2 = Text3_2.get(1.0, END)
    f = open(sa, 'w')
    f.write('First postulate\n\n')
    f.write(letter)
    f.write('\n')
    f.write('Second postulate\n\n')
    f.write(letter1)
    f.write('\n')
    f.write('Third postulate\n\n')
    f.write(letter2)
    f.close()


def checkSequence(seq):
        if (seq.isdigit()):
            for i in seq:
                if ((int(i) > 1) | (int(i) < 0)):
                    return False
        else:
            return False


def firstPostulate(event, seq):
    flag = True
    
    Text1_2.configure(state=NORMAL)
    Text1_2.delete('1.0', END)

    if (len(seq) == 0):
        Text1_2.insert(END, 'Empty input')
        Text1_2.configure(state=DISABLED)
        return
    t1 = time.time()
    z = seq.count("0")
    o = seq.count("1")
    t2 = time.time()
    
    z1.append(t2 - t1)
    z2.append(len(seq))
    if (checkSequence(seq) == False):
        Text1_2.insert(END, 'Wrong sequence')
        Text1_2.configure(state=DISABLED)
        return
          
    if(abs(z - o) > 1):
        flag = False
    
    Text1_2.insert('1.0', 'Zeroes: ' + str(z) + '. Ones: ' + str(o) 
                    + '\nDifference: ' + str(abs(z - o)))
    if flag == True:
        Text1_2.insert(END, '\nPostulate satisfied.')
    else:
        Text1_2.insert(END, '\nPostulate not satisfied.') 
    Text1_2.configure(state=DISABLED)


def secondPostulate(event, seq):
    flag = True
    
    Text2_2.configure(state=NORMAL)
    Text2_2.delete('1.0', END)
    
    if (len(seq) == 0):
        Text2_2.insert(END, 'Empty input')
        Text2_2.configure(state=DISABLED)
        return
    
    if (checkSequence(seq) == False):
        Text2_2.insert(END, 'Wrong sequence')
        Text2_2.configure(state=DISABLED)
        return
    t1 = time.time()
    streaks = Golomb.Streaks(seq)
    strnum = list(streaks.keys())
    strnum.sort(key=None, reverse=False)
    
    Text2_2.insert(END, 'Sequence length: ' + str(len(seq)) + '\n')
    
    for i in range(1, len(strnum) + 1):
        Text2_2.insert(END, 'Number of series with lenght ' + str(i) + ': ' + str(len(streaks[i])) + '\n')
    
    if (streaks):
        for i in range(0, len(strnum) - 1):
            if(abs(strnum[i] - strnum[i + 1]) != 1):
                flag = False
                break
            if(len(streaks[strnum[i]]) != 2 * len(streaks[strnum[i + 1]])):
                if(len(streaks[strnum[i]]) != 1 and len(streaks[strnum[i + 1]]) != 1):
                    flag = False
                    break
    else:
        flag = False
    t2 = time.time()
    k1.append(t2 - t1)
    k2.append(len(seq))
    if flag == True:
        Text2_2.insert(END, '\nPostulate satisfied.')
    else:
        Text2_2.insert(END, '\Postulate not satisfied.') 
    Text2_2.configure(state=DISABLED)

def thirdPostulate(event, seq):
    flag = True
    
    Text3_2.configure(state=NORMAL)
    Text3_2.delete('1.0', END)
    
    if (len(seq) == 0):
        Text3_2.insert(END, 'Empty input')
        Text3_2.configure(state=DISABLED)
        return
    
    if (checkSequence(seq) == False):
        Text3_2.insert(END, 'Wrong sequence')
        Text3_2.configure(state=DISABLED)
        return
    
    if (len(seq) == 0):
        Text3_2.insert(END, 'Empty input')
        Text3_2.configure(state=DISABLED)
        return
    
    if (checkSequence(seq) == False):
        Text1_2.insert(END, 'Wrong sequence')
        Text1_2.configure(state=DISABLED)
        return
    t1 = time.time()
    # Выполняем сдвиг
    seq2 = seq[1:] + seq[:1]
    # Ищем расстояние Хэмминга
    ham = Golomb.Distance(seq, seq2)
    Text3_2.insert(END, 'Hamming distance of the sequence: ' + str(ham) + "\n") 
    for i in range(2, len(seq) - 1):
        # Сдвигаем последовательнось на i, после чего снова считаем сдвиг и сравниваем его
        seq2 = seq[i:] + seq[:i]
        Text3_2.insert(END, 'Shift by ' + str(i) + '\nDistance: ' + str(Golomb.Distance(seq, seq2))
                       + '\n')
        if(ham != Golomb.Distance(seq, seq2)):
            flag = False
    t2 = time.time()
    m1.append(t2 - t1)
    m2.append(len(seq))       
    if flag == True:
        Text3_2.insert(END, '\nPostulate satisfied.')
    else:
        Text3_2.insert(END, '\nnPostulate not satisfied.')
    Text3_2.configure(state=DISABLED)

# Инициализация интерфейса


root = Tk()


root.resizable(False, False)

main_menu = Menu()
    
file_menu = Menu(tearoff=0)
file_menu.add_command(label='Open...', command=_open)
file_menu.add_command(label='Test speed...', command=openBinary)
file_menu.add_command(label='Save as...', command=_save)
file_menu.add_command(label='Exit', command=root.destroy)

info_menu = Menu(tearoff=0)
info_menu.add_command(label='About', command=_help)
info_menu.add_cascade(label='Complexity', command=difficulty)
   
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Help', menu=info_menu)
    
root.config(menu=main_menu)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_compcolor = '#d9d9d9'
_ana1color = '#d9d9d9'
_ana2color = '#d9d9d9' 
font11 = '-family {Segoe UI} -size 11 -weight normal -slant '  \
    'roman -underline 0 -overstrike 0'
font12 = '-family {Segoe UI} -size 15 -weight normal -slant '  \
    'roman -underline 0 -overstrike 0'
style = ttk.Style()
if sys.platform == 'win32':
    style.theme_use('winnative')
style.configure('.', background=_bgcolor)
style.configure('.', foreground=_fgcolor)
style.configure('.', font='TkDefaultFont')
style.map('.', background=
    [('selected', _compcolor), ('active', _ana2color)])

root.geometry('722x487+473+135')
root.title('PyGolomb')
root.configure(background='#e6e6fa')

style.configure('TNotebook.Tab', background=_bgcolor)
style.configure('TNotebook.Tab', foreground=_fgcolor)
style.map('TNotebook.Tab', background=
    [('selected', _compcolor), ('active', _ana2color)])

TNotebook1 = ttk.Notebook(root)
TNotebook1.place(relx=0.01, rely=0.02, relheight=0.96
, relwidth=0.98)
TNotebook1.configure(width=704)
TNotebook1.configure(takefocus='')

TNotebook1_t0 = Frame(TNotebook1)
TNotebook1.add(TNotebook1_t0, padding=3)
TNotebook1.tab(0, text='Main', compound='left', underline='-1',)
TNotebook1_t0.configure(background='#e6e6fa')
TNotebook1_t0.configure(highlightbackground='#d9d9d9')
TNotebook1_t0.configure(highlightcolor='black')
bgimage = PhotoImage(file='bg.gif')
background_label = Label(TNotebook1_t0, image=bgimage)
background_label.place(x=0, y=0)

Label0_1 = Label(TNotebook1_t0, font='Helvetica 18 bold')
Label0_1.configure(text='Testing pseudorandom sequences for conformity with Golomb’s randomness postulates')
Label0_1.place(height=60, width=704)
Label0_1.configure(background='#e6e6fa')

TNotebook1_t1 = Frame(TNotebook1)
TNotebook1.add(TNotebook1_t1, padding=3)
TNotebook1.tab(1, text='First postulate', compound='left'
, underline='-1',)
TNotebook1_t1.configure(background='#e6e6fa')
TNotebook1_t1.configure(highlightbackground='#d9d9d9')
TNotebook1_t1.configure(highlightcolor='black')
TNotebook1_t1.configure(width=610)

TNotebook1_t2 = Frame(TNotebook1)
TNotebook1.add(TNotebook1_t2, padding=3)
TNotebook1.tab(2, text='Second postulate', compound='none'
, underline='-1',)
TNotebook1_t2.configure(background='#e6e6fa')
TNotebook1_t2.configure(highlightbackground='#d9d9d9')
TNotebook1_t2.configure(highlightcolor='black')

TNotebook1_t3 = Frame(TNotebook1)
TNotebook1.add(TNotebook1_t3, padding=3)
TNotebook1.tab(3, text='Third postulate', compound='none'
, underline='-1',)
TNotebook1_t3.configure(background='#e6e6fa')
TNotebook1_t3.configure(highlightbackground='#d9d9d9')
TNotebook1_t3.configure(highlightcolor='black')

Text1_1 = Text(TNotebook1_t1)
Text1_1.place(relx=0.01, rely=0.02, relheight=0.48
, relwidth=0.97)
Text1_1.configure(background='#ffffff')
Text1_1.configure(font=font12)
Text1_1.configure(foreground='black')
Text1_1.configure(highlightbackground='#d9d9d9')
Text1_1.configure(highlightcolor='black')
Text1_1.configure(insertbackground='black')
Text1_1.configure(selectbackground='#c4c4c4')
Text1_1.configure(selectforeground='black')
Text1_1.configure(width=680)
Text1_1.configure(wrap=WORD)
Text1_1.insert(END, 'How to use it: Enter the sequence in the field or use \"Open file\" button. \n\n' \
               'To check the first postulate we count ones and zeroes ' \
               'and compare their numbers. If the difference is 1, postulate is satisfied.')
Text1_1.configure(state=DISABLED)

Label1_1 = Label(TNotebook1_t1)
Label1_1.place(relx=0.01, rely=0.52, height=41, width=164)
Label1_1.configure(background='#e6e6fa')
Label1_1.configure(disabledforeground='#a3a3a3')
Label1_1.configure(font=font11)
Label1_1.configure(foreground='#000000')
Label1_1.configure(text='Sequence:')
Label1_1.configure(width=164)

Label1_2 = Label(TNotebook1_t1)
Label1_2.place(relx=0.01, rely=0.61, height=41, width=84)
Label1_2.configure(activebackground='#f9f9f9')
Label1_2.configure(activeforeground='black')
Label1_2.configure(background='#e6e6fa')
Label1_2.configure(disabledforeground='#a3a3a3')
Label1_2.configure(font=font11)
Label1_2.configure(foreground='#000000')
Label1_2.configure(highlightbackground='#d9d9d9')
Label1_2.configure(highlightcolor='black')
Label1_2.configure(text='Result:')
Label1_2.configure(width=84)

Entry1_1 = Entry(TNotebook1_t1)
Entry1_1.place(relx=0.24, rely=0.55, height=20, relwidth=0.72)
Entry1_1.configure(background='white')
Entry1_1.configure(disabledforeground='#a3a3a3')
Entry1_1.configure(font='TkFixedFont')
Entry1_1.configure(foreground='#000000')
Entry1_1.configure(insertbackground='black')
Entry1_1.configure(width=504)

Text1_2 = Text(TNotebook1_t1)
Text1_2.place(relx=0.24, rely=0.64, height=60, relwidth=0.72)
Text1_2.configure(background='white')
Text1_2.configure(font=font11)
Text1_2.configure(foreground='#000000')
Text1_2.configure(highlightbackground='#d9d9d9')
Text1_2.configure(highlightcolor='black')
Text1_2.configure(insertbackground='black')
Text1_2.configure(selectbackground='#c4c4c4')
Text1_2.configure(selectforeground='black')
Text1_2.configure(width=504)
Text1_2.configure(state=DISABLED)

Button1_1 = Button(TNotebook1_t1)
Button1_1.place(relx=0.03, rely=0.82, height=54, width=117)
Button1_1.configure(activebackground='#d9d9d9')
Button1_1.configure(activeforeground='#000000')
Button1_1.configure(background='#d9d9d9')
Button1_1.configure(disabledforeground='#a3a3a3')
Button1_1.configure(foreground='#000000')
Button1_1.configure(highlightbackground='#d9d9d9')
Button1_1.configure(highlightcolor='black')
Button1_1.configure(pady='0')
Button1_1.configure(text='Open file')
Button1_1.configure(width=117)
Button1_1.bind('<Button-1>', openAndProcess1)

Button1_2 = Button(TNotebook1_t1)
Button1_2.place(relx=0.43, rely=0.82, height=54, width=117)
Button1_2.configure(activebackground='#d9d9d9')
Button1_2.configure(activeforeground='#000000')
Button1_2.configure(background='#d9d9d9')
Button1_2.configure(disabledforeground='#a3a3a3')
Button1_2.configure(foreground='#000000')
Button1_2.configure(highlightbackground='#d9d9d9')
Button1_2.configure(highlightcolor='black')
Button1_2.configure(pady='0')
Button1_2.configure(text='Run algorithm')
Button1_2.configure(width=117)
Button1_2.bind('<Button-1>', lambda event : firstPostulate(event, Entry1_1.get()))

Button1_3 = Button(TNotebook1_t1)
Button1_3.place(relx=0.8, rely=0.82, height=54, width=117)
Button1_3.configure(activebackground='#d9d9d9')
Button1_3.configure(activeforeground='#000000')
Button1_3.configure(background='#d9d9d9')
Button1_3.configure(disabledforeground='#a3a3a3')
Button1_3.configure(foreground='#000000')
Button1_3.configure(highlightbackground='#d9d9d9')
Button1_3.configure(highlightcolor='black')
Button1_3.configure(pady='0')
Button1_3.configure(text='Exit')
Button1_3.configure(width=117)
Button1_3.bind('<Button-1>', _close)

Text2_1 = Text(TNotebook1_t2)
Text2_1.place(relx=0.01, rely=0.02, relheight=0.48
, relwidth=0.97)
Text2_1.configure(background='#ffffff')
Text2_1.configure(font=font12)
Text2_1.configure(foreground='black')
Text2_1.configure(highlightbackground='#d9d9d9')
Text2_1.configure(highlightcolor='black')
Text2_1.configure(insertbackground='black')
Text2_1.configure(selectbackground='#c4c4c4')
Text2_1.configure(selectforeground='black')
Text2_1.configure(width=680)
Text2_1.configure(wrap=WORD)
Text2_1.insert(END, 'How to use it: Enter the sequence in the field or use \"Open file\" button. \n\n' \
               'To check the second postulate we need to count series lenght. Half of the series should have lenght of 1, quarter - 2, one eighth - 3 and so on.')
Text2_1.configure(state=DISABLED)

Label2_1 = Label(TNotebook1_t2)
Label2_1.place(relx=0.01, rely=0.52, height=41, width=164)
Label2_1.configure(background='#e6e6fa')
Label2_1.configure(disabledforeground='#a3a3a3')
Label2_1.configure(font=font11)
Label2_1.configure(foreground='#000000')
Label2_1.configure(text='Sequence:')
Label2_1.configure(width=164)

Label2_2 = Label(TNotebook1_t2)
Label2_2.place(relx=0.01, rely=0.61, height=41, width=84)
Label2_2.configure(activebackground='#f9f9f9')
Label2_2.configure(activeforeground='black')
Label2_2.configure(background='#e6e6fa')
Label2_2.configure(disabledforeground='#a3a3a3')
Label2_2.configure(font=font11)
Label2_2.configure(foreground='#000000')
Label2_2.configure(highlightbackground='#d9d9d9')
Label2_2.configure(highlightcolor='black')
Label2_2.configure(text='Result:')
Label2_2.configure(width=84)

Entry2_1 = Entry(TNotebook1_t2)
Entry2_1.place(relx=0.24, rely=0.55, height=20, relwidth=0.72)
Entry2_1.configure(background='white')
Entry2_1.configure(disabledforeground='#a3a3a3')
Entry2_1.configure(font='TkFixedFont')
Entry2_1.configure(foreground='#000000')
Entry2_1.configure(insertbackground='black')
Entry2_1.configure(width=504)

scrollbar2_1 = Scrollbar(TNotebook1_t2)
scrollbar2_1.pack(side=RIGHT, fill=Y)

Text2_2 = Text(TNotebook1_t2, yscrollcommand=scrollbar2_1.set)
Text2_2.place(relx=0.24, rely=0.64, height=60, relwidth=0.72)
Text2_2.configure(background='white')
Text2_2.configure(font='TkFixedFont')
Text2_2.configure(foreground='#000000')
Text2_2.configure(highlightbackground='#d9d9d9')
Text2_2.configure(highlightcolor='black')
Text2_2.configure(insertbackground='black')
Text2_2.configure(selectbackground='#c4c4c4')
Text2_2.configure(selectforeground='black')
Text2_2.configure(width=504)
Text2_2.configure(state=DISABLED)

scrollbar2_1.config(command=Text2_2.yview)

Button2_1 = Button(TNotebook1_t2)
Button2_1.place(relx=0.03, rely=0.82, height=54, width=117)
Button2_1.configure(activebackground='#d9d9d9')
Button2_1.configure(activeforeground='#000000')
Button2_1.configure(background='#d9d9d9')
Button2_1.configure(disabledforeground='#a3a3a3')
Button2_1.configure(foreground='#000000')
Button2_1.configure(highlightbackground='#d9d9d9')
Button2_1.configure(highlightcolor='black')
Button2_1.configure(pady='0')
Button2_1.configure(text='Open file')
Button2_1.configure(width=117)
Button2_1.bind('<Button-1>', openAndProcess2)

Button2_2 = Button(TNotebook1_t2)
Button2_2.place(relx=0.43, rely=0.82, height=54, width=117)
Button2_2.configure(activebackground='#d9d9d9')
Button2_2.configure(activeforeground='#000000')
Button2_2.configure(background='#d9d9d9')
Button2_2.configure(disabledforeground='#a3a3a3')
Button2_2.configure(foreground='#000000')
Button2_2.configure(highlightbackground='#d9d9d9')
Button2_2.configure(highlightcolor='black')
Button2_2.configure(pady='0')
Button2_2.configure(text='Run algorithm')
Button2_2.configure(width=117)
Button2_2.bind('<Button-1>', lambda event : secondPostulate(event, Entry2_1.get()))

Button2_3 = Button(TNotebook1_t2)
Button2_3.place(relx=0.8, rely=0.82, height=54, width=117)
Button2_3.configure(activebackground='#d9d9d9')
Button2_3.configure(activeforeground='#000000')
Button2_3.configure(background='#d9d9d9')
Button2_3.configure(disabledforeground='#a3a3a3')
Button2_3.configure(foreground='#000000')
Button2_3.configure(highlightbackground='#d9d9d9')
Button2_3.configure(highlightcolor='black')
Button2_3.configure(pady='0')
Button2_3.configure(text='Exit')
Button2_3.configure(width=117)
Button2_3.bind('<Button-1>', _close)

Text3_1 = Text(TNotebook1_t3)
Text3_1.place(relx=0.01, rely=0.02, relheight=0.48
, relwidth=0.97)
Text3_1.configure(background='#ffffff')
Text3_1.configure(font=font12)
Text3_1.configure(foreground='black')
Text3_1.configure(highlightbackground='#d9d9d9')
Text3_1.configure(highlightcolor='black')
Text3_1.configure(insertbackground='black')
Text3_1.configure(selectbackground='#c4c4c4')
Text3_1.configure(selectforeground='black')
Text3_1.configure(width=680)
Text3_1.configure(wrap=WORD)
Text3_1.insert(END, 'How to use it: Enter the sequence in the field or use \"Open file\" button. \n\n' \
               'To check the third postulate we calculate the autocorrelation function of shifted functions with Hamming distance.  ' \
               'Postulate is satisfied if distance is always the same.')
Text3_1.configure(state=DISABLED)

Label3_1 = Label(TNotebook1_t3)
Label3_1.place(relx=0.01, rely=0.52, height=41, width=164)
Label3_1.configure(background='#e6e6fa')
Label3_1.configure(disabledforeground='#a3a3a3')
Label3_1.configure(font=font11)
Label3_1.configure(foreground='#000000')
Label3_1.configure(text='Sequence:')
Label3_1.configure(width=164)

Label3_2 = Label(TNotebook1_t3)
Label3_2.place(relx=0.01, rely=0.61, height=41, width=84)
Label3_2.configure(activebackground='#f9f9f9')
Label3_2.configure(activeforeground='black')
Label3_2.configure(background='#e6e6fa')
Label3_2.configure(disabledforeground='#a3a3a3')
Label3_2.configure(font=font11)
Label3_2.configure(foreground='#000000')
Label3_2.configure(highlightbackground='#d9d9d9')
Label3_2.configure(highlightcolor='black')
Label3_2.configure(text='Result:')
Label3_2.configure(width=84)

Entry3_1 = Entry(TNotebook1_t3)
Entry3_1.place(relx=0.24, rely=0.55, height=20, relwidth=0.72)
Entry3_1.configure(background='white')
Entry3_1.configure(disabledforeground='#a3a3a3')
Entry3_1.configure(font='TkFixedFont')
Entry3_1.configure(foreground='#000000')
Entry3_1.configure(insertbackground='black')
Entry3_1.configure(width=504)

scrollbar3_1 = Scrollbar(TNotebook1_t3)
scrollbar3_1.pack(side=RIGHT, fill=Y)

Text3_2 = Text(TNotebook1_t3, yscrollcommand=scrollbar3_1.set)
Text3_2.place(relx=0.24, rely=0.64, height=60, relwidth=0.72)
Text3_2.configure(background='white')
Text3_2.configure(font='TkFixedFont')
Text3_2.configure(foreground='#000000')
Text3_2.configure(highlightbackground='#d9d9d9')
Text3_2.configure(highlightcolor='black')
Text3_2.configure(insertbackground='black')
Text3_2.configure(selectbackground='#c4c4c4')
Text3_2.configure(selectforeground='black')
Text3_2.configure(width=504)
Text3_2.configure(state=DISABLED)

scrollbar3_1.config(command=Text3_2.yview)

Button3_1 = Button(TNotebook1_t3)
Button3_1.place(relx=0.03, rely=0.82, height=54, width=117)
Button3_1.configure(activebackground='#d9d9d9')
Button3_1.configure(activeforeground='#000000')
Button3_1.configure(background='#d9d9d9')
Button3_1.configure(disabledforeground='#a3a3a3')
Button3_1.configure(foreground='#000000')
Button3_1.configure(highlightbackground='#d9d9d9')
Button3_1.configure(highlightcolor='black')
Button3_1.configure(pady='0')
Button3_1.configure(text='Open file')
Button3_1.configure(width=117)
Button3_1.bind('<Button-1>', openAndProcess3)

Button3_2 = Button(TNotebook1_t3)
Button3_2.place(relx=0.43, rely=0.82, height=54, width=117)
Button3_2.configure(activebackground='#d9d9d9')
Button3_2.configure(activeforeground='#000000')
Button3_2.configure(background='#d9d9d9')
Button3_2.configure(disabledforeground='#a3a3a3')
Button3_2.configure(foreground='#000000')
Button3_2.configure(highlightbackground='#d9d9d9')
Button3_2.configure(highlightcolor='black')
Button3_2.configure(pady='0')
Button3_2.configure(text='Run algorithm')
Button3_2.configure(width=117)
Button3_2.bind('<Button-1>', lambda event : thirdPostulate(event, Entry3_1.get()))

Button3_3 = Button(TNotebook1_t3)
Button3_3.place(relx=0.8, rely=0.82, height=54, width=117)
Button3_3.configure(activebackground='#d9d9d9')
Button3_3.configure(activeforeground='#000000')
Button3_3.configure(background='#d9d9d9')
Button3_3.configure(disabledforeground='#a3a3a3')
Button3_3.configure(foreground='#000000')
Button3_3.configure(highlightbackground='#d9d9d9')
Button3_3.configure(highlightcolor='black')
Button3_3.configure(pady='0')
Button3_3.configure(text='Exit')
Button3_3.configure(width=117)
Button3_3.bind('<Button-1>', _close)

Label2 = Label(root)
Label2.place(relx=0.516, rely=0.02, height=21, width=344)
Label2.configure(background='#e6e6fa')
Label2.configure(disabledforeground='#a3a3a3')
Label2.configure(foreground='#000000')
Label2.configure(width=344)

root.mainloop()
