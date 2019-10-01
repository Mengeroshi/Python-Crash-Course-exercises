import matplotlib.pyplot as plt

input_values = range(1,5000)
cubes = [x**3 for x in input_values]

plt.style.use("seaborn")

fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)

ax.axis([0, 5000, 0, 125_000_000_000])

plt.show()