import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import pathlib

filepath = pathlib.Path(__file__).with_name("cleaned_data.csv")

data = []
try:
    with filepath.open("r") as measurement:
        reader = csv.reader(measurement, delimiter=';')
        for row in reader:
            data.append(row)

except FileNotFoundError:
    print("File not found")

print(f"Data loaded: {data[0:5]}\n")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for row in data:
    x = float(row[0])
    y = float(row[1])
    z = float(row[2])
    ax.scatter(x, y, z, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()