import tkinter
from functools import partial

# Window
window = tkinter.Tk()
window.title('My First GUI')
window.minsize(width=500, height=300)
window.config(padx=25, pady=50)

# Label
my_label = tkinter.Label(text="Tkinter", font=("sans-serif", 24, 'bold'))
my_label.grid(column=0, row=0)
my_label['text'] = 'New Label Text'

# Entry
entry = tkinter.Entry(width=15)
entry.grid(column=1, row=1)


# Button
def change_text(prefix=''):
    label_text = entry.get()
    my_label.config(text=prefix+label_text)


button = tkinter.Button(text='Click me', command=change_text)
button.grid(column=2, row=2)

button2 = tkinter.Button(text='Click me 2', command=partial(change_text, '2'))
button2.grid(column=2, row=0)

# Mainloop
window.mainloop()
