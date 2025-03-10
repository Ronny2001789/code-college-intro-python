import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Using plot() instead of scatter()
    ax.plot(rw.x_values, rw.y_values, linewidth=1, color="blue")  # Line plot

    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.plot(0, 0, 'go', markersize=10)  # Green start point
    ax.plot(rw.x_values[-1], rw.y_values[-1], 'ro', markersize=10)  # Red end point

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Ask the user if they want another walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':  
        break  # Exit the loop
