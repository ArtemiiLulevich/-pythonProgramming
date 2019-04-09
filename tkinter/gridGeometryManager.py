import tkinter

main_win = tkinter.Tk()

main_win.title("Pack geometry manager")
main_win.geometry('800x600-8-200')

#help(tkinter)


label = tkinter.Label(main_win, text="hello world")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(main_win)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1,column=0)

rightFrame = tkinter.Frame(main_win)
rightFrame.grid(row=1, column=2, sticky='n')


button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)


#cinfig the columns
main_win.columnconfigure(0, weight=1)
main_win.columnconfigure(1, weight=1)
main_win.grid_columnconfigure(2, weight=1)


leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

main_win.mainloop()
