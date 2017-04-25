import csv
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os
import sys

x_coords = []
y_coords = []

# visualize a dot operation
def visdot():
    return None

# visualize the elliptic curve used
def viscurve(a, b):
    Y, X = np.ogrid[-5:300:100j, -5:300:100j]
    plt.contour(X.ravel(), Y.ravel(), pow(Y,2) - pow(X,3) - X * a - b, [0])
    plt.grid()
    return None

def main():
    # exec ecc implementation to generate data
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            subprocess.call([sys.argv[1]])
        else:
            print("Please provide path to ECC executable.")
    else:
        print("Please provide path to ECC executable.")
        sys.exit()

    # set arguments
    if len(sys.argv) == 3:
        cfile = sys.argv[2]
    else:
        if os.path.isfile("coords.csv"):
            cfile = "coords.csv"
        else:
            print("Please provide a .csv file containing coords")
            sys.exit()

    if len(sys.argv) == 4:
        dfile = sys.argv[3]
    else:
        if os.path.isfile("data.csv"):
            dfile = "data.csv"
        else:
            print("Please provide a .csv file containing an elliptic curve function")
            sys.exit()

    # read in coords from csv file
    with open(cfile, 'r') as coords:
        creader = csv.reader(coords, delimiter=',')
        for row in coords:
            coord = row.split(',')
            # remove trailing newline
            coord[1] = coord[1][:-1]
            x_coords.append(coord[0])
            y_coords.append(coord[1])
    coords.close

    # read in other data from data csv
    with open(dfile, 'r') as data:
        dreader = csv.reader(data, delimiter=',')
        rownum = 0
        for row in data:
            # get curve function
            if rownum == 0:
                ab = row.split(',')
                a = int(ab[0])
                b = int(ab[1])

    data.close

    # plot points on elliptic curve
    plt.scatter(x_coords, y_coords)

    # does not work - output is weird
    # viscurve(a, b)

    # display output plot
    plt.show()

if __name__ == "__main__":
    main()
