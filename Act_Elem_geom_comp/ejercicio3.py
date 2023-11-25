from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Define the points
points = [(9, 7), (1, 3), (7, 2), (1, 9), (5, 4)]

# Create a Voronoi diagram
vor = Voronoi(points)

# Plot the Voronoi diagram
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax)

# Plot the points
ax.plot(*zip(*points), marker='o', color='red', ls='')

plt.title('Voronoi Diagram')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
