import tkinter

main_win = tkinter.Tk()

main_win.title("Pack geometry manager")
main_win.geometry('800x600+30+300')

#help(tkinter)


label = tkinter.Label(main_win, text="hello world")
label.pack(side='top')

leftFrame = tkinter.Frame(main_win)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(main_win)
rightFrame.pack(side='right', anchor='n', expand=True)


button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
main_win.mainloop()
