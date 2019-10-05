import matplotlib.pyplot as plt

input_values = range(1,5001)
cubes = [x**3 for x in input_values]

plt.style.use("seaborn")

fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.flag, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 5000, 0, 125_000_000_000])

plt.show()