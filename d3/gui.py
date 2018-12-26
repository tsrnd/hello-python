import tkinter

window = tkinter.Tk()

# define eventlistener
def uocCaiGi():
    lb.configure(text=":)")

window.title('Turn down for what???')
lb = tkinter.Label(window, text='what', font=("monaco", 69))
lb.grid(column=0, row=0)
btn = tkinter.Button(window, text='click de co them 1 dieu uoc', command=uocCaiGi)
btn.grid(column=0, row=10)


window.geometry('320x240')
window.mainloop()