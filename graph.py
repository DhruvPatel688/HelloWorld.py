import matplotlib.pyplot as plt
import numpy as np

# Create data
index = int(input("How many x values do you have? "))
x =[]
while index > 0:
    a = float(input("What is one of the x values? "))
    x.append(a)
    index -= 1
index = int(input("How many y values do you have? "))
y =[]
while index > 0:
    b = float(input("What is one of the y values? "))
    y.append(b)
    index -= 1


# Create a line plot
plt.plot(x, y, color = 'purple')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple graph')

# Add legend
plt.legend()

# Show the plot
plt.show()
