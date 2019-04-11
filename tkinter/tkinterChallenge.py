try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
# mian window setup
calcWindow = tkinter.Tk()

calcWindow.title('Calculator')
calcWindow.geometry('320x500-20-300')

# main window column configuration
calcWindow.columnconfigure(0, weight=15, minsize=15)
calcWindow.columnconfigure(1, weight=25, minsize=15)
calcWindow.columnconfigure(2, weight=25, minsize=15)
calcWindow.columnconfigure(3, weight=25, minsize=15)
calcWindow.columnconfigure(4, weight=25, minsize=15)
calcWindow.columnconfigure(5, weight=15, minsize=15)

# main window row configuration
calcWindow.rowconfigure(0, weight=15, minsize=15)
calcWindow.rowconfigure(1, weight=15, minsize=15)
calcWindow.rowconfigure(2, weight=15, minsize=15)
calcWindow.rowconfigure(3, weight=15, minsize=15)
calcWindow.rowconfigure(4, weight=15, minsize=15)
calcWindow.rowconfigure(5, weight=15, minsize=15)
calcWindow.rowconfigure(6, weight=100, minsize=15)
# Create Entery
enterString = tkinter.Entry(calcWindow, relief='groove')
enterString.grid(row=0, column=1, columnspan=4, sticky='news')

# Func frame
# funcButtonFrame = tkinter.Frame(calcWindow, width=3, height=3)
# funcButtonFrame.grid(row=1, column=1,  sticky='news')

# Function numbers
buttonCancel = tkinter.Button(calcWindow, text='C')
buttonCE = tkinter.Button(calcWindow, text='CE')

# Func button positioning
buttonCancel.grid(row=1, column=1, sticky='news')
buttonCE.grid(row=1, column=2, sticky='news')

# Create buttons Frame
# buttonFrame = tkinter.Frame(calcWindow)
# buttonFrame.grid(row=3, column=1, columnspan=3, sticky='news')

# Create number buttons
button0 = tkinter.Button(calcWindow, text='0')
button1 = tkinter.Button(calcWindow, text='1')
button2 = tkinter.Button(calcWindow, text='2')
button3 = tkinter.Button(calcWindow, text='3')
button4 = tkinter.Button(calcWindow, text='4')
button5 = tkinter.Button(calcWindow, text='5')
button6 = tkinter.Button(calcWindow, text='6')
button7 = tkinter.Button(calcWindow, text='7')
button8 = tkinter.Button(calcWindow, text='8')
button9 = tkinter.Button(calcWindow, text='9')

# Create Character buttons
buttonPlus = tkinter.Button(calcWindow, text='+')
buttonMinus = tkinter.Button(calcWindow, text='-')
buttonMult = tkinter.Button(calcWindow, text='*')
buttonDiv = tkinter.Button(calcWindow, text='/')
buttonEq = tkinter.Button(calcWindow, text='=')

# Button positioning
button7.grid(row=2, column=1, sticky=tkinter.E + tkinter.W)
button8.grid(row=2, column=2, sticky='news')
button9.grid(row=2, column=3, sticky='news')
buttonPlus.grid(row=2, column=4, sticky='news')

button4.grid(row=3, column=1, sticky='news')
button5.grid(row=3, column=2, sticky='news')
button6.grid(row=3, column=3, sticky='news')
buttonMinus.grid(row=3, column=4, sticky='news')

button1.grid(row=4, column=1, sticky='news')
button2.grid(row=4, column=2, sticky='news')
button3.grid(row=4, column=3, sticky='news')
buttonMult.grid(row=4, column=4, sticky='news')

button0.grid(row=4, column=1, sticky='news')
buttonEq.grid(row=4, column=2, columnspan=2, sticky='news')
buttonDiv.grid(row=4, column=4, sticky='news')


calcWindow.mainloop()
