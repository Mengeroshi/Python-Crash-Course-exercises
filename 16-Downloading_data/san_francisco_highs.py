import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = '/home/mengeroshi/Escritorio/Python-Crash-Course-exercises/16-Downloading_data/data/san_francisco_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_index = header_row.index('DATE') #prints the number on csv
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[high_index])
        high = (high-32) * (5/9)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()