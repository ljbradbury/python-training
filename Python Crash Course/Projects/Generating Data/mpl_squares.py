import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]

squares = [1, 4, 9, 16, 25]

plt.plot(input_values,squares, linewidth=3)

# Set chart title and label axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# Set the size of the tick labels
plt.tick_params(axis="both", labelsize=10)

plt.show()
