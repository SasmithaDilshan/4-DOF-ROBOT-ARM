import serial
from tkinter import *
import tkinter as tk
from math import *


# ser = serial.Serial('COM6', 9600,timeout = 1)
a = ""
state = False
def update_InvKinVal(event=None):
    global state
    global val1,val2,val3,val4,val5
    global x,y,z
    label9.config(text=f"EE_pose: {val5.get()}")
    
    x_ = x.get()
    y_ = y.get()
    z_ = z.get()
    theta_1= atan2(y_,x_)
    p2_x = x_-12.5*cos(radians(val5.get()))*cos(theta_1)
    p2_y = y_-12.5*cos(radians(val5.get()))*sin(theta_1)
    p2_z = z_-12.5*sin(radians(val5.get()))
    print(p2_x,p2_y,p2_z)
    r = sqrt(p2_x**2+p2_y**2)-1.3
    s = p2_z-9.5
    q =(r**2+s**2-2*(12**2))/(2*12*12)
    if(-1<=q<=1):
        theta_3 = -acos(q)
        theta_2 = atan2(s,r)-atan2(12*sin(theta_3),(12+12*cos(theta_3)))
        print("a",val5.get())
        theta_4=radians(val5.get())-theta_2-theta_3
        if (0<=int(degrees(theta_4)+90)<=180):
            print(degrees(theta_1),degrees(theta_2),degrees(theta_3),degrees(theta_4))
            theta[0]=int(degrees(theta_1))
            theta[1]=int(degrees(theta_2))
            theta[2]=int(-degrees(theta_3))
            theta[3]=int(degrees(theta_4)+90)
            val1.set(int(degrees(theta_1)))
            val2.set(int(degrees(theta_2)))
            val3.set(int(degrees(theta_3)))
            val4.set(int(degrees(theta_4)))
            z.set(9.5+12*sin(radians(val2.get()))+12*sin(radians(val2.get()+val3.get()))+12.5*sin(radians(val2.get()+val3.get()+val4.get())))
        else:
            state=True
            theta[0]=int(degrees(theta_1))
            theta[1]=int(degrees(theta_2))
            theta[2]=int(-degrees(theta_3))
            theta[3]=int(90)
            val1.set(int(degrees(theta_1)))
            val2.set(int(degrees(theta_2)))
            val3.set(int(degrees(theta_3)))
            val4.set(int(90))
            z.set(9.5+12*sin(radians(val2.get()))+12*sin(radians(val2.get()+val3.get()))+12.5*sin(radians(val2.get()+val3.get()+val4.get())))
    else:
        state = True
        val1.set(90)
        val2.set(90)
        val3.set(90)
        val4.set(90)
    if (not(state)):
        indicator_canvas.itemconfig(circle, fill='green') 
        indicator_canvas.itemconfig(text, text='Solution Exist', fill='white') 

        
    else:
        indicator_canvas.itemconfig(circle, fill='red')  
        indicator_canvas.itemconfig(text, text='No Solution', fill='black')
        state = False
   

def update_values(event=None):
    global val1,val2,val3,val4,val5
    global x,y,z
    theta[0]=slider1.get()
    theta[1]=-slider2.get()
    theta[2]=slider3.get()
    theta[3]=-slider4.get()+90
    theta[4] = slider9.get()
    label1.config(text=f"theta 1: {val1.get()}")
    label2.config(text=f"theta 2: {val2.get()}")
    label3.config(text=f"theta 3: {val3.get()}")
    label4.config(text=f"theta 4: {val4.get()}")
    x.set(12*cos(radians(val1.get()))*(0.10833+cos(radians(val2.get()))+cos(radians(val2.get()+val3.get()))+1.04167*cos(radians(val2.get()+val3.get()+val4.get()))))
    y.set(12*sin(radians(val1.get()))*(0.10833+cos(radians(val2.get()))+cos(radians(val2.get()+val3.get()))+1.04167*cos(radians(val2.get()+val3.get()+val4.get()))))
    z.set(9.5+12*sin(radians(val2.get()))+12*sin(radians(val2.get()+val3.get()))+12.5*sin(radians(val2.get()+val3.get()+val4.get())))

    
def on_button_click():
    global a
    global theta
    for i in range(0,len(theta)-1):
        a+=str(theta[i])+","
    a= a[:-1]+"\n"
    print(a)
    # ser.write(a.encode())
    a=""
    
# Create the main window
root = tk.Tk()
root.title("ARM GUI")
root.geometry("800x800")
x = tk.IntVar()
y = tk.IntVar()
z = tk.IntVar()
val1 = tk.DoubleVar()
val2 = tk.DoubleVar()
val3 = tk.DoubleVar()
val4 = tk.DoubleVar()
val5 = tk.DoubleVar()
print(val1.get())
# Create sliders with labels

frame1 = tk.Frame(root)
frame1.pack()
theta = [0,0,0,0,0]
label1 = tk.Label(frame1, text="theta 1: 0")
label1.pack(side=tk.LEFT)
slider1 = tk.Scale(frame1, from_=-180, to=180,length=200, orient=tk.HORIZONTAL, command=update_values,variable=val1)
slider1.pack(side=tk.LEFT)

frame2 = tk.Frame(root)
frame2.pack()
label2 = tk.Label(frame2, text="theta 2: 0")
label2.pack(side=tk.LEFT)
slider2 = tk.Scale(frame2, from_=-180, to=180,length=200, orient=tk.HORIZONTAL, command=update_values,variable=val2)
slider2.pack(side=tk.LEFT)

frame3 = tk.Frame(root)
frame3.pack()
label3 = tk.Label(frame3, text="theta 3: 0")
label3.pack(side=tk.LEFT)
slider3 = tk.Scale(frame3, from_=-180, to=180, length=200,orient=tk.HORIZONTAL, command=update_values,variable=val3)
slider3.pack(side=tk.LEFT)

frame4 = tk.Frame(root)
frame4.pack()
label4 = tk.Label(frame4, text="theta 4: 0")
label4.pack(side=tk.LEFT)
slider4 = tk.Scale(frame4, from_=-180, to=180,length=200, orient=tk.HORIZONTAL, command=update_values,variable=val4)
slider4.pack(side=tk.LEFT)
frame5 = tk.Frame(root)
frame5.pack()

button = tk.Button(frame5, text="Move Arm", command=on_button_click,bg="white")
button.pack(side=tk.LEFT, padx=5)
button_1 = tk.Button(frame5, text="Grab", command=on_button_click,bg="yellow")
button_1.pack(side=tk.LEFT, padx=5)
button_2 = tk.Button(frame5, text="release", command=on_button_click,bg="blue")
button_2.pack(side=tk.LEFT, padx=5)

print(val1,val2)
#inverse kinamatics calculations
frame6 = tk.Frame(root)
frame6.pack()
t1=tk.Label(frame6, text="X coordinate:")
t1.pack(side=tk.LEFT)
l1=tk.Scale(frame6, from_=-40, to=40,length=200, orient=tk.HORIZONTAL, command=update_InvKinVal,variable=x)
l1.pack(side=tk.LEFT)
frame7 = tk.Frame(root)
frame7.pack()
t2=tk.Label(frame7, text="Y coordinate:")
t2.pack(side=tk.LEFT)
l2 =tk.Scale(frame7, from_=-40, to=40,length=200, orient=tk.HORIZONTAL, command=update_InvKinVal,variable=y)
l2.pack(side=tk.LEFT)
frame8 = tk.Frame(root)
frame8.pack()
t3=tk.Label(frame8, text="Z coordinate:")
t3.pack(side=tk.LEFT)
l3 =tk.Scale(frame8, from_=0, to=50,length=200, orient=tk.HORIZONTAL, command=update_InvKinVal,variable=z)
l3.pack(side=tk.LEFT)
frame9 = tk.Frame(root)
frame9.pack()
label9 = tk.Label(frame9, text="EE_Pose: 0")
label9.pack(side=tk.LEFT)
slider9 = tk.Scale(frame9, from_=-180, to=180,length=200, orient=tk.HORIZONTAL, command=update_InvKinVal,variable=val5)
slider9.pack(side=tk.LEFT)

frame10 = tk.Frame(root)
frame10.pack()
indicator_canvas = tk.Canvas(frame10, width=200, height=50, bg='white')
indicator_canvas.pack(pady=20)
circle = indicator_canvas.create_rectangle(10, 15, 170, 40, outline='black', fill='red')
text = indicator_canvas.create_text(90, 25, text='No', fill='black')
# Start the main loop
root.mainloop()