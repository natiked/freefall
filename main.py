import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from freefall import freefall

banner = '''
___________                       ___________      .__  .__   
\_   _____/______   ____   ____   \_   _____/____  |  | |  |  
 |    __) \_  __ \_/ __ \_/ __ \   |    __) \__  \ |  | |  |  
 |     \   |  | \/\  ___/\  ___/   |     \   / __ \|  |_|  |__
 \___  /   |__|    \___  >\___  >  \___  /  (____  /____/____/
     \/                \/     \/       \/        \/           

                                        Homework - 2
                                        Group 3
'''

print(banner)
choice = int(input("Select action: \n1. Free Fall Model(vpython)\t2. Plotting a graph :> "))

def simulate_free_fall(initial_height, initial_velocity, g=9.81, t_end=2):
    dt = 0.01
    #Array 
    #Creating a time array starting from 0 and moving up with interval of dt till t_end 
    t_data = np.arange(0, t_end+dt, dt)
    x_data = np.zeros(len(t_data))
    v_data = np.zeros(len(t_data))

    # Calculates x and v by iterating len(t)
    for i in range(len(t_data)-1):
        # x(ti+1) = x(ti) + v(ti) . t
        # v(ti+1) = v(ti) - g . t
        x_data[i+1] = x_data[i] + v_data[i]*dt
        v_data[i+1] = v_data[i] - g*dt

    return t_data, x_data, v_data

#Plotting the graph using t,x,v and h data
def plot_graphs(t_data, x_data, v_data, height_initial):
    plt.plot(t_data, x_data, label='Position (m)')
    plt.plot(t_data, v_data, label='Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.ylabel('v(t) & x(t)')
    plt.legend()
    plt.title(f"Free Fall Simulation (Initial Height: {height_initial} m)")
    plt.show()

#Animating and saving
def animate_and_save(t_data, x_data, v_data, height_initial):
    fig, ax = plt.subplots()
    t_line, = ax.plot([], [], label='Time (s)')
    x_line, = ax.plot([], [], label='Position (m)')
    v_line, = ax.plot([], [], label='Velocity (m/s)')

    ax.set_xlim(0, max(t_data))
    ax.set_ylim(-2 * height_initial, 2 * height_initial)

    #Updating the frame
    def update_frame(frame):
        t_line.set_data(t_data[:frame + 1], t_data[:frame + 1])
        x_line.set_data(t_data[:frame + 1], x_data[:frame + 1])
        v_line.set_data(t_data[:frame + 1], v_data[:frame + 1])
        return t_line, x_line, v_line

    ani = FuncAnimation(fig, update_frame, frames=len(t_data), interval=50, blit=True)

    # Save the animation as a GIF file
    ani.save(f'free_fall_animation_{height_initial}.gif', writer='pillow', fps=20)

def main():
    # Get user input
    height_initial = float(input("Enter the height from which the object was realesed from(m): "))
    velocity_initial = float(input("Enter the initial velocity (m/s): "))

    # Simulate free fall
    t_data, x_data, v_data = simulate_free_fall(height_initial, velocity_initial)

    # Plot graphs
    plot_graphs(t_data, x_data, v_data, height_initial)

    # Create and save animation
    animate_and_save(t_data, x_data, v_data, height_initial)

if choice == 1:
    freefall()
elif choice == 2:
    main()
else: 
    print("[-] Invalid input")

