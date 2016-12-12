#Basic Calculator with GUI
#Shoie Somanath

import simplegui
from math import factorial

#global variables
s = ""
data = []

# Array of permitted operations
op_arr = ['/', '*', '+', '-', '!']

def draw_handler(canvas):
    #Horizontal lines
    canvas.draw_line([0, 110], [300, 110], 2, 'Black')
    canvas.draw_line([0, 170], [300, 170], 2, 'Black')
    canvas.draw_line([0, 230], [300, 230], 2, 'Black')
    canvas.draw_line([0, 290], [240, 290], 2, 'Black')
    
    #Vertical lines
    canvas.draw_line([60, 110], [60, 290], 2, 'Black')
    canvas.draw_line([120, 110], [120, 350], 2, 'Black')
    canvas.draw_line([180, 110], [180, 350], 2, 'Black')
    canvas.draw_line([240, 110], [240, 350], 2, 'Black')
    
    #Drawing text
    canvas.draw_text('9', (20, 150), 30, 'Black', 'serif')
    canvas.draw_text('8', (80, 150), 30, 'Black', 'serif')
    canvas.draw_text('7', (140, 150), 30, 'Black', 'serif')
    
    canvas.draw_text('6', (20, 210), 30, 'Black', 'serif')
    canvas.draw_text('5', (80, 210), 30, 'Black', 'serif')
    canvas.draw_text('4', (140, 210), 30, 'Black', 'serif')
    
    canvas.draw_text('3', (20, 270), 30, 'Black', 'serif')
    canvas.draw_text('2', (80, 270), 30, 'Black', 'serif')
    canvas.draw_text('1', (140, 270), 30, 'Black', 'serif')
    
    canvas.draw_text('0', (50, 330), 30, 'Black', 'serif')
    canvas.draw_text('.', (145, 330), 50, 'Black', 'serif')
    
    canvas.draw_text('+', (200, 150), 30, 'Black', 'serif')
    canvas.draw_text('-', (200, 210), 40, 'Black', 'serif')
    canvas.draw_text('*', (200, 270), 30, 'Black', 'serif')
    canvas.draw_text('C', (200, 330), 30, 'Black', 'serif')
    
    canvas.draw_text('/', (265, 150), 30, 'Black', 'serif')
    canvas.draw_text('n!', (260, 210), 30, 'Black', 'serif')
    canvas.draw_text('=', (260, 300), 30, 'Black', 'serif')
    
    canvas.draw_text(s, [30,60], 32, "Red")
        
# Formatting of input string into a list of numbers and operations between them
# For Example: For input - '23+2*2-54/27', this function will return 
['23', '+', '2', '*', '2', '-', '54', '/', '27']
def format_input():
    global s, data, op_arr
    count = 0
    for i in range(len(s)):
        if s[i] in op_arr:
            data.append(s[count:i])
            data.append(s[i])
            count = i+1
        if i == len(s)-1:
            data.append(s[count:])        
    return data        

#For performing one Factorial operation
def CalculateFact(data):
    fac_pos = data.index('!')
    fac_res = factorial(int(data[fac_pos-1]))
    data[fac_pos] = str(fac_res)
    data.pop(fac_pos-1)
    return data

# For performing one division operation
def divide(data):
    div_pos = data.index('/')
    div_res = float(data[div_pos-1]) / float(data[div_pos+1])
    data[div_pos] = str(div_res)
    data.pop(div_pos-1)
    data.pop(div_pos)
    return data

# For performing one multiplication operation
def multiply(data):
    mul_pos = data.index('*')
    mul_res = float(data[mul_pos-1]) * float(data[mul_pos+1])
    data[mul_pos] = str(mul_res)
    data.pop(mul_pos-1)
    data.pop(mul_pos)
    return data

# For performing one addition operation
def add(data):
    add_pos = data.index('+')
    add_res = float(data[add_pos-1]) + float(data[add_pos+1])
    data[add_pos] = str(add_res)
    data.pop(add_pos-1)
    data.pop(add_pos)
    return data

# For performing one subtraction operation
def subtract(data):
    sub_pos = data.index('-')
    sub_res = float(data[sub_pos-1]) - float(data[sub_pos+1])
    data[sub_pos] = str(sub_res)
    data.pop(sub_pos-1)
    data.pop(sub_pos)
    return data

def evaluate(data):
    global s
    # Perform 'factorial' operation for every '!' in the input
    while '!' in data:
        data = CalculateFact(data)
        
    # Perform 'divide' operation for every '/' in the input
    while '/' in data:
        data = divide(data)

    # Perform 'multiply' operation for every '*' in the input
    while '*' in data:
        data = multiply(data)

    # Perform 'add' operation for every '+' in the input
    while '+' in data:
        data = add(data)

    # Perform 'subtract' operation for every '-' in the input
    while '-' in data:
        data = subtract(data)
        
    print data[0]
    
    s = ""
    s = s + str(data[0]) 

def reset():
    global data, s
    data = []
    s = ""
    
def click(pos):
    global data, s
    if pos[0]in range(0,59) and pos[1] in range(111,169):
        #character :9
        s = s + str(9)
    elif pos[0]in range(61,119) and pos[1] in range(111,169):
        #character :8
        s = s + str(8)
    elif pos[0]in range(121,179) and pos[1] in range(111,169):
        #character :7
        s = s + str(7)
    elif pos[0]in range(0,59) and pos[1] in range(171,229):
        #character :6
        s = s + str(6)
    elif pos[0]in range(61,119) and pos[1] in range(171,229):
        #character :5
        s = s + str(5)
    elif pos[0]in range(121,179) and pos[1] in range(171,229):
        #character :4
        s = s + str(4)
    elif pos[0]in range(0,59) and pos[1] in range(231,289):
        #character :3
        s = s + str(3)
    elif pos[0]in range(61,119) and pos[1] in range(231,289):
        #character :2 
        s = s + str(2)
    elif pos[0]in range(121,179) and pos[1] in range(231,289):
        #character :1
        s = s + str(1)
    elif pos[0]in range(1,119) and pos[1] in range(291,349):
        #character :0
        s = s + str(0)
    elif pos[0]in range(121,179) and pos[1] in range(291,349):
        #character :'.'
        s = s + str('.')
    elif pos[0]in range(181,239) and pos[1] in range(111,169):
        #character :'+'
        s = s + str('+')
    elif pos[0]in range(181,239) and pos[1] in range(171,229):
        #character :'-'
        s = s + str('-')
    elif pos[0]in range(181,239) and pos[1] in range(231,289):
        #character :'*'
        s = s + str('*')
    elif pos[0]in range(181,239) and pos[1] in range(291,349):
        #character :'C'
        reset()
    elif pos[0]in range(241,299) and pos[1] in range(111,169):
        #character :'/'
        s = s + str('/')
    elif pos[0]in range(241,299) and pos[1] in range(171,229):
        #character :'n!'
        s = s + str('!')
    elif pos[0]in range(241,299) and pos[1] in range(231,349):
        #character :'='
        data = format_input()
        evaluate(data)
        
    
frame = simplegui.create_frame('BASIC CALCULATOR', 300, 350)
frame.set_canvas_background("Pink")
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()