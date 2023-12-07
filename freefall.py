from vpython import *

def freefall():
    height_str = input("Enter the height from which the object was realesed from(m): ")
    initial_velocity = float(input("Enter the initial velocity(m/s): "))
    height = float(height_str)

    #To maximize the visibility of the ball we divide the height by 10*n, n depends on the digit fo height
    if height > 1:
        for i in range(len(height_str)):
            height = height / 10

    #To moving the object lower than the floor we subtract the radius of the object from y of the floor
    Radius_of_object = 0.01
    floor = box(pos = vector(0,-0.005-Radius_of_object,0),size = vector(0.5,0.01,0.2))

    #Constant
    gravity = 9.8
    x_initial = 0
    y_initial = height
    vx_initial = 0
    vy_initial = 0
    time = 0
    time_difference = 0.01

    #Creating the object 
    object = sphere(pos = vector(x_initial,y_initial,0), radius=Radius_of_object,color=color.blue)

    #Moving the object lower until it reaches y=0 
    while object.pos.y>=0:
        rate(50)
        x = x_initial + vx_initial * time
        y = y_initial + vy_initial * time - 0.5*gravity*time**2
        object.pos = vector(x,y,0)
        time = time + time_difference