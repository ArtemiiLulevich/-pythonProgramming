try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
# mian window setup
calcWindow = tkinter.Tk()

calcWindow.title('Calculator')
calcWindow.geometry('480x320+20+300')

# main window column configeration
calcWindow.columnconfigure(0, weight=3)
calcWindow.columnconfigure(1, weight=3)
calcWindow.columnconfigure(2, weight=3)
calcWindow.columnconfigure(3, weight=3)

# main window row configeration
calcWindow.rowconfigure(0, weight=3)
calcWindow.rowconfigure(1, weight=3)
calcWindow.rowconfigure(2, weight=3)
calcWindow.rowconfigure(3, weight=3)
calcWindow.rowconfigure(4, weight=3)
calcWindow.rowconfigure(5, weight=3)

# Create Entery
enterString = tkinter.Entry(calcWindow)
enterString.grid(row=0, column=0, columnspan=4, rowspan=2, sticky='news')

calcWindow.mainloop()
