import csv
from datetime import datetime

from matplotlib import pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index,
        low_index):
    """Get the highs and lows from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                high = (high-32) * (5/9)

                low = int(row[low_index])
                low = (low-32) * (5/9)
            except ValueError:
                print(f"Missing data for {row[1]}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
#San Francisco
filename = '/home/mengeroshi/Escritorio/Python-Crash-Course-exercises/16-Downloading_data/data/san_francisco_2018.csv'
highs, lows, dates = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=3, low_index=4)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Death Valley
filename = '/home/mengeroshi/Escritorio/Python-Crash-Course-exercises/16-Downloading_data/data/death_valley_2018_simple.csv'
highs, lows, dates = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=4, low_index=5)

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Sitka vs San Francisco high and low temperatures - 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()