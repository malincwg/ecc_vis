import csv
import matplotlib.pyplot as plt

x_coords = []
y_coords = []

#read in coords from csv file
with open('coords.csv', 'r') as coords:
    creader = csv.reader(coords, delimiter=',')
    for row in coords:
        coord = row.split(',')
        #remove trailing newline
        coord[1] = coord[1][:-1]
        x_coords.append(coord[0])
        y_coords.append(coord[1])
coords.close

plt.scatter(x_coords, y_coords)
plt.show()
