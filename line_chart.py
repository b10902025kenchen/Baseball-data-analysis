import matplotlib.pyplot as plt

# Create lists for each line initialized with 0s
lines = [[0] * 16 for _ in range(3)]

# # -1
# lines[0] = [43,38,35,37,36,31,30,16]
# # 0
# lines[1] = [54,56,55,52,57,59,52,49]
# # +1
# lines[2] = [61,63,67,69,69,75,74,85]

lines[0] = [41.59, 40.09, 39.39, 36.83, 34.48, 30.36, 24.39, 14.93]
lines[1] = [53.34, 53.13, 52.68, 52.66, 52.47, 52.22, 52.47, 52.3]
lines[2] = [64.77, 65.94, 65.83, 67.82, 69.56, 73.11, 77.71, 86.62]

# Create x-axis values
x = list(range(1, 9))

# Create a figure and axis object
fig, ax = plt.subplots()

name = ["down by 1", "tie", "lead by 1"]
# Plot each line
for i in range(3):
    ax.plot(x, lines[i], label=name[i])

# Add labels and title
ax.set_xlabel('End of Inning')
ax.set_ylabel('WPCT(%)')
ax.set_title('MLB WPCT of home team')

# Add a legend
ax.legend()

# Display the plot
plt.show()
