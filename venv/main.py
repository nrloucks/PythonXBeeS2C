import serial
import binascii
import tkinter as tk
from digi import *
import time


# variables ---

state = 0
is_tripped = 0


# setup gui elements ---------

window = tk.Tk(screenName="Test Name", baseName=None, className='Tk', useTk=1)
window.title("Motion Sensor Console")
motion_canvas = tk.Canvas(window, bg="green", width=50, height=50)
btn_ON_OFF = tk.Button(window,
                       activebackground="grey",
                       text="Off",
                       fg='white',
                       bg='red'
                       )
# window title banner
window_banner = tk.Label(window,
                         text="Motion Sensor Console",
                         fg='grey',
                         bg='black',
                         relief="solid",
                         font=("Arial", 30, "normal")
                         )


# function definitions -------


def set_disabled():
    window.config(motion_canvas, bg="grey")


def get_motion_status():
    data_raw = ''
    initial_red_time = 0
    # print("enter get motion status")
    ser1 = serial.Serial('COM3', 9600, timeout=1.75)
    # print("serial opened, waiting for data")
    data_raw = ser1.read(14)

    if data_raw == '':
        ser1.close()
        window.after(0, get_motion_status())
        window.update()
    else:
        try:
            data_hex = binascii.hexlify(data_raw).decode('utf-8')
            D2 = data_hex[22:26]  # extract desired bits
            base_ten_val =int(D2, 16)
            # print("this sample:")
            print(base_ten_val)  # view data

        except ValueError:
            # print("caught valueError")
            ser1.close()
            # print("re-paint")
            window.update()

        else:
            print("Data received")
            if base_ten_val == 4:
                print("set indicator: red")
                motion_canvas.config(bg="red")
                print("re-paint")
                #initial_red_time = time.now()
                window.update()
            elif base_ten_val == 0 or '':
                print("set indicator: green")
                motion_canvas.config(bg="green")
                print("re-paint")
                #initial_red_time = 0
                window.update()
        finally:
            ser1.close()
            # print("re-paint")
            window.update()
            # print("set window interrupt")
            window.after(0, get_motion_status())

# runs once -> calls recursive "get_motion_status"


btn_ON_OFF.pack()
window_banner.pack()
motion_canvas.pack()
print("re-paint")
window.update()
print("set window interrupt")
window.after(0, get_motion_status())

# delta_t = time.now() - initial_red_time
# threshold_time = time.time(0, 0, 10)    # threshold for missed low == 10 sec

# if delta_t - threshold_time < 0:
"""IF the time after a high signal is received
exceeds 10 seconds, reset to green. If a falling edge is  missed the program will remain high until the falling 
edge if the subsequent trigger. If no movement occurs after the missed falling edge the program would remain in 
the tripped state indefinitely. To avoid this this error catching code will reset it. If it was indeed tripped 
the value will return to tripped state on the next loop until 10 seconds have passed again. """

# print("set indicator: green")
# motion_canvas.config(bg="green")
# print("re-paint")
# initial_red_time = 0
# window.update()