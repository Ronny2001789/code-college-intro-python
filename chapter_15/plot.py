# import matplotlib.pyplot as plt 


# squares = [1,4,9,16,25]

# fig, ax = plt.subplots()
# ax.plot(squares,linewidth= 14 )
# # Set chart title and label axes.
# ax.set_title("squares numbers",fontsize = 24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("square of value", fontsize = 14)
# ax.tick_params(labelsize=14)

# # Set size of tick labels.
# plt.show()

# import matplotlib.pyplot as plt

# # list 
# names = ["Ethan", "Ronny", "Pierre", "Marvelous"]
# # Sample values (e.g., scores, ages, or any data)
# values = [10, 15, 7, 12]  

# # Create a bar chart
# fig, ax = plt.subplots()
# fig.set_facecolor("green")
# ax.bar(names, values, color=['blue', 'red', 'green', 'purple'])

# # Set chart title and labels
# ax.set_title("SAMPLE BAR CHART", fontsize=20 )
# ax.set_xlabel("NAMES", fontsize=14)
# ax.set_ylabel("VALUES", fontsize=14)
# # ax.set_title("Custom Background Color")
# # Show the plot
# plt.show()

import matplotlib.pyplot as plt

# First 5 cubic numbers
x_small = [1, 2, 3, 4, 5]
y_small = [x**3 for x in x_small]

# First 5,000 cubic numbers
x_large = list(range(1, 5001))
y_large = [x**3 for x in x_large]

# Plot for first 5 numbers
fig, ax = plt.subplots()
ax.plot(x_small, y_small, marker='*', linestyle='-', color='b', linewidth=2)
ax.set_title("First 5 Cubic Numbers")
ax.set_xlabel("Number")
ax.set_ylabel("Cube of Number")
plt.show()

# Plot for first 5000 numbers
# fig, ax = plt.subplots()
# ax.plot(x_large, y_large, color='r', linewidth=1)
# ax.set_title("First 5000 Cubic Numbers")
# ax.set_xlabel("Number")
# ax.set_ylabel("Cube of Number")
# plt.show()









