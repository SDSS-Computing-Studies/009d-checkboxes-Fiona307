#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    decimal = binary[0]*128+binary[1]*64+binary[2]*32+binary[3]*16+binary[4]*8+binary[5]*4+binary[6]*2+binary[7]
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    answer = []
    if decimal >= 128:
        answer.append(1)
        #21
        if decimal-128 >= 64:
            answer.append(1)
            #31
            if decimal-128-64 >= 32:
                answer.append(1)
                #41
                if decimal-128-64-32 >= 16:
                    answer.append(1)
                    #51
                    if decimal-128-64-32-16 >= 8:
                        answer.append(1)
                        #61
                        if decimal-128-64-32-16-8 >= 4:
                            answer.append(1)
                            #71
                            if decimal-128-64-32-16-8-4 >= 2:
                                answer.append(1)
                                #81
                                if decimal-128-64-32-16-8-4-2 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                            #70
                            else:
                                answer.append(0)
                                #81
                                if decimal-128-64-32-16-8-4 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                        #60
                        else:
                            answer.append(0)
                            #71
                            if decimal-128-64-32-16-8 >= 2:
                                answer.append(1)
                                #81
                                if decimal-128-64-32-16-8-2 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                            #70
                            else:
                                answer.append(0)
                                #81
                                if decimal-128-64-32-16-8 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                    #50
                    else:
                        answer.append(0)
                        #61
                        if decimal-128-64-32-16 >= 4:
                            answer.append(1)
                            #71
                            if decimal-128-64-32-16-4 >= 2:
                                answer.append(1)
                                #81
                                if decimal-128-64-32-16-4-2 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                            #70
                            else:
                                answer.append(0)
                                #81
                                if decimal-128-64-32-16-4 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                        #60
                        else:
                            answer.append(0)
                            #71
                            if decimal-128-64-32-16 >= 2:
                                answer.append(1)
                                #81
                                if decimal-128-64-32-16-2 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                            #70
                            else:
                                answer.append(0)
                                #81
                                if decimal-128-64-32-16 >= 1:
                                    answer.append(1)
                                #80
                                else:
                                    answer.append(0)
                else:
                    answer.append(0)
                    if decimal-128-64-32 >= 8:
                        answer.append(1)
                    else:
                        answer.append(0)
                        if decimal-128-64-32 >= 4:
                            answer.append(1)
                        else:
                            answer.append(0)
                            if decimal-128-64-32 >= 2:
                                answer.append(1)
                            else:
                                answer.append(0)
                                if decimal-128-64-32 >= 1:
                                    answer.append(1)
                                else:
                                    answer.append(0)
            else:
                answer.append(0)
        else:
            answer.append(0)

    else:
        answer.append(0)
    binary = (answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7])
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = e1.get()
    binary = binary_to_decimal(decimal)
    state1.set(binary[0])
    state2.set(binary[1])
    state3.set(binary[2])
    state4.set(binary[3])
    state5.set(binary[4])
    state6.set(binary[5])
    state7.set(binary[6])
    state8.set(binary[7])

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    binary.append(state1.get())
    binary.append(state2.get())
    binary.append(state3.get())
    binary.append(state4.get())
    binary.append(state5.get())
    binary.append(state6.get())
    binary.append(state7.get())
    binary.append(state8.get())
    decimal = binary_to_decimal(binary)
    e1.insert(0,str(decimal))

win = tk.Tk()



b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)

l1 = tk.Label(win, text="Binary/Decimal Converter!")
e1 = tk.Entry(win)

state1 = tk.IntVar()
cb1 = tk.Checkbutton(win, variable=state1)
state2 = tk.IntVar()
cb2 = tk.Checkbutton(win, variable=state2)
state3 = tk.IntVar()
cb3 = tk.Checkbutton(win, variable=state3)
state4 = tk.IntVar()
cb4 = tk.Checkbutton(win, variable=state4)
state5 = tk.IntVar()
cb5 = tk.Checkbutton(win, variable=state5)
state6 = tk.IntVar()
cb6 = tk.Checkbutton(win, variable=state6)
state7 = tk.IntVar()
cb7 = tk.Checkbutton(win, variable=state7)
state8 = tk.IntVar()
cb8 = tk.Checkbutton(win, variable=state8)

l1.grid(row=1, column=1, columnspan=8)
cb1.grid(row=2, column=1)
cb2.grid(row=2, column=2)
cb3.grid(row=2, column=3)
cb4.grid(row=2, column=4)
cb5.grid(row=2, column=5)
cb6.grid(row=2, column=6)
cb7.grid(row=2, column=7)
cb8.grid(row=2, column=8)
b1.grid(row=3, column=1, columnspan=4)
b2.grid(row=3, column=5, columnspan=4)
e1.grid(row=4, column=1, columnspan=8)

win.mainloop()