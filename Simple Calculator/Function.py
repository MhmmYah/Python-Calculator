dotcounter = 0
mem1 = float()
mem2 = float()
functions = enumerate(["+","-","/","X"])
fchoice = 0

def saveval(input, display):
    global dotcounter
    global mem1
    global mem2
    global fchoice
    

    if (dotcounter): 
        for i in range(0,dotcounter):
            input = input / 10.0
        dotcounter +=  1

    else:
        mem1 = mem1 * 10

    mem1 = mem1 + input
    display['text'] = mem1

def setdot():
    global dotcounter
    dotcounter = 1

def clear(display):
    global dotcounter
    global mem1
    global mem2
    global fchoice
    dotcounter = 0
    mem1 = 0
    mem2 = 0
    fchoice = 0
    display['text'] = mem1

def operate(input, display):
    global fchoice
    global mem2
    global mem1

    if (fchoice):
        calculate(display)
        mem2 = mem1
        fchoice = 0

    fchoice = input
    mem2 = mem1
    mem1 = 0
    display['text'] = mem1

def calculate(display):
    global mem1
    global mem2
    global fchoice
    if(fchoice == 1):
        mem1 = mem1 + mem2
    elif(fchoice == 2):
        mem1 = mem2 - mem1
    elif(fchoice == 3):
        mem1 = float(mem2) / mem1
    elif(fchoice == 4):
        mem1 = mem1 * mem2
    else:
        display["text"] = "Not yet implemented"
        return
    mem2 = 0
    fchoice = 0
    display["text"] = mem1