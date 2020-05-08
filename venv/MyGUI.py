import Tkinter as tk
from Tkinter import *

btn_height = 2
btn_width = 12

# define GUI elements/properties and styling
# Create new window "m" with given parameters using the Tkinter library
m = tk.Tk(screenName="Test Name", baseName=None, className='Tk', useTk=1)

# define buttons
btn_ON_OFF = tk.Button(m,
                       activebackground="light-grey",
                       text="Off",
                       fg='white',
                       bg='red'
                       )
btn_ALARM_ON_OFF = tk.Button(m, text="Alarm", fg='red', bg='brown', relief=RAISED, font=("arial", 14, "bold"))
btn_VIEW_CAMERA = tk.Button(m, text="View Cam", fg='red', bg='brown', relief=RAISED, font=("arial", 14, "bold"))
btn_ON_OFF.config(height=btn_height, width=btn_width)
btn_ALARM_ON_OFF.config(height=btn_height, width=btn_width)
btn_VIEW_CAMERA.config(height=btn_height, width=btn_width)

# window title banner (for now)
window_banner = tk.Label(m, text="HOME AUTOMATION", fg='grey', bg='black', relief="solid", font=("stencil", 30, "bold"))

# Create Canvas
# canvas = tk.Canvas(m, width=1280, height=720)


def make():

    btn_ON_OFF.place(x=100, y=90)
    btn_ALARM_ON_OFF.place(x=300, y=90)
    btn_VIEW_CAMERA.place(x=100, y=165)
    window_banner.place(x=640, y=22)
    # canvas.pack()
