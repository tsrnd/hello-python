import tkinter as tk
from tkinter import Menu
from tkinter import ttk
        
#======================
# functions
#======================
# Exit GUI cleanly
def _quit():
    win.quit()      # win will exist when this function is called
    win.destroy()
    exit() 

#======================
# procedural code
#======================
# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python Projects")
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Creating a Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)   # command callback
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------

# We are creating a container frame to hold all other widgets
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')
# using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

# ---------------------------------------------------------------
# but frame won't be visible until we add widgets to it...
# Adding a Label
ttk.Label(weather_conditions_frame, text="Location:").grid(column=0, row=0, sticky='W')

# ---------------------------------------------------------------
city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)             # highlight first city
        
# ---------------------------------------------------------------
# increase combobox width to longest city
max_width  = max([len(x) for x in citySelected['values']])
new_width = max_width
new_width = max_width - 5           # adjust per taste of extra spacing
citySelected.config(width = new_width)
         
#======================
# Start GUI
#======================
win.mainloop()
