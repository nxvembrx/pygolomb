from tkinter import Tk, Message

def show():
    root = Tk()
    
    _bgcolor = '#d9d9d9'
    _fgcolor = '#000000'
    _compcolor = '#d9d9d9'
    _ana1color = '#d9d9d9' 
    _ana2color = '#d9d9d9' 
    font9 = '-family {Segoe UI} -size 14 -weight normal -slant '  \
        'roman -underline 0 -overstrike 0'

    root.geometry('492x249+487+174')
    root.title('About')
    root.configure(background='#d9d9d9')
    root.configure(highlightbackground='#d9d9d9')
    root.configure(highlightcolor='black')

    Message1 = Message(root)
    Message1.place(relx=0.02, rely=-1.16, relheight=3.29, relwidth=0.94)

    Message1.configure(background='#d9d9d9')
    Message1.configure(font=font9)
    Message1.configure(foreground='#000000')
    Message1.configure(highlightbackground='#d9d9d9')
    Message1.configure(highlightcolor='black')
    Message1.configure(text='Welcome to the program for verifying binary sequences for conformity with Golomb’s randomness postulates! Each tab has a short information about each of three postulates. Also there\'s an ability to enter the sequence yourself or load it from a file. You can store resulting information in a file to show it to the professor or save for later use.')
    Message1.configure(width=463)

    root.mainloop()
