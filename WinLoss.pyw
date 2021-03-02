# Win/Loss counter that auto updates .txt file
from tkinter import *


def write_to_file():
    with open(filename, 'w') as fp:
        fp.write(recordText.get())


def reset():
    global win, loss
    win = 0
    loss = 0
    recordText.set(f"Record: {win} - {loss}")
    write_to_file()


def add_win():
    global win
    win += 1
    recordText.set(f"Record: {win} - {loss}")
    write_to_file()


def add_loss():
    global loss
    loss += 1
    recordText.set(f"Record: {win} - {loss}")
    write_to_file()


filename = 'record.txt'
win = 0
loss = 0



# GUI LAYOUT
window = Tk()
window.geometry('400x200')
window.config(bg='black')
window.title("Chrono's W/L Recorder")

recordText = StringVar()
recordText.set(f"Record: {win} - {loss}")
display = Label(window, textvariable=recordText, height=7, bg='black', fg='white', font=100)
display.pack(fill=X)

winButton = Button(window, text='WIN', command=add_win, height=5, width=17, bg='green', font=20)
winButton.pack(side=LEFT)
lossButton = Button(window, text='LOSS', command=add_loss, height=5, width=17, bg='red', font=20)
lossButton.pack(side=RIGHT)
resetButton = Button(window, text='RESET', bg='blue', command=reset, height=5, font=20)
resetButton.pack(side=BOTTOM, fill=X)





window.mainloop()