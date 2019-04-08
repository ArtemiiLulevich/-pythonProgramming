import tkinter

main_win = tkinter.Tk()

main_win.title('Hello world!:)')
main_win.geometry('800x600+480+270')

label = tkinter.Label(main_win, text="Hello World", bg='lightgreen')
label.pack(side='top', fill=tkinter.X)

canvas = tkinter.Canvas(main_win, relief='raised', borderwidth=1)
canvas.pack(side='left')

# canvas.create_line(10, 10, 150, 150)
# canvas.create_line(10, 20, 150, 200)
leftFrame = tkinter.Frame(main_win)
leftFrame.pack(side='left', expand=False, anchor='s')

button1 = tkinter.Button(leftFrame, text='Button1')
button2= tkinter.Button(leftFrame, text='Button2')
button3 = tkinter.Button(leftFrame, text='Button3')

button1.pack(anchor='n')
button2.pack(anchor='e')
button3.pack(anchor='s')

main_win.mainloop()