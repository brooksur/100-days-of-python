import tkinter

# Setup screen
screen = tkinter.Tk()
screen.title('Miles to Kilometers')
screen.config(height=400, width=400)

# Miles Components
miles_entity = tkinter.Entry()
miles_entity.grid(row=0, column=1)
miles_label = tkinter.Label()
miles_label.config(text='Miles')
miles_label.grid(row=0, column=2)

# Kilometer Components
equal_to_label = tkinter.Label()
equal_to_label.config(text="is equal to")
equal_to_label.grid(row=1, column=0)
km_num_label = tkinter.Label()
km_num_label.config(text="0")
km_num_label.grid(row=1, column=1)
km_label = tkinter.Label()
km_label.config(text="Km")
km_label.grid(row=1, column=2)


# Button

def calculate():
    miles = float(miles_entity.get())
    kms = miles * 1.60934
    km_num_label.config(text=f'{kms}')


calculate_btn = tkinter.Button()
calculate_btn.config(text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)

screen.mainloop()