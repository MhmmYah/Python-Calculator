#!/usr/bin/env python
# Setting up dependencies
import Tkinter as tk 
import Function as fu

# Setting up frames
root = tk.Tk()
root.geometry("150x160")
root.title("Calculator")
answerframe = tk.Frame(root)
answerframe.pack(fill= tk.X, side = tk.TOP, expand = 1)
numberframe = tk.Frame(root)
numberframe.pack(fill=tk.Y, side = tk.LEFT, expand = 1)
functionframe = tk.Frame(root)
functionframe.pack(fill=tk.Y, side = tk.RIGHT, expand = 1)

# Setting up answerframe
display = tk.Label(answerframe, text = fu.mem1)
display.pack(fill = tk.X, side = tk.TOP, expand = 1)
tk.Button(answerframe, text ="Clear", command= lambda: fu.clear(display)).pack(fill = tk.NONE, side = tk.RIGHT, anchor = tk.SW)

# Setting up numberframe
for i in range(1,10):
    b = tk.Button(numberframe, text = i, command= lambda i=i: fu.saveval(i, display))
    b.grid(row=(9-i)/3, column=(i-1)%3, sticky="nsew")
tk.Button(numberframe, text ="0", command= lambda: fu.saveval(0, display)).grid(row=3, column=0, sticky="nsew")
tk.Button(numberframe, text =".", command= lambda: fu.setdot()).grid(row=3, column=1, sticky="nsew")
tk.Button(numberframe, text = "=", command = lambda: fu.calculate(display)).grid(row=3, column=2, sticky="nsew")


# Setting up functionframe

for i, sign in fu.functions:
    b = tk.Button(functionframe, text = sign, command= lambda i=i: fu.operate(i+1, display))
    b.grid(column = i/4 ,row = i%4, sticky = "nsew")

# Run till exit
root.mainloop()