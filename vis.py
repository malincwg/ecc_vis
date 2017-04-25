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
    # this is very, very, very not safe - executes anything you pass it
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
            # remove trailing character if it exits
            if coord[1][-1].isdigit():
                coord[1] = coord[1][:-1]
            x_coords.append(coord[0])
            y_coords.append(coord[1])
    coords.close

    # read in other data from data csv
    # data format: A, B, base point, alice pub key, bob pub key, data x, data y
    #               encrypted x, encrypted y
    with open(dfile, 'r') as data:
        dreader = csv.reader(data, delimiter=',')

        ab= next(dreader)
        bp = next(dreader)
        ak = next(dreader)
        bk = next(dreader)
        clt = next(dreader)
        cyt = next(dreader)

        # Get curve function a and b
        a = int(ab[0])
        b = int(ab[1])

        # Get base point of curve (important for keys)
        bpx = int(bp[0][1:])
        bpy = int(bp[1][1:-1])

        # Get Alice's public key
        akx = int(ak[0][1:])
        aky = int(ak[1][1:-1])

        # Get Bob's public key
        bkx = int(bk[0][1:])
        bky = int(bk[1][1:-1])

        # Get cleartext data
        cltx = clt[0]
        clty = clt[1]

        # Get cyphertext data
        cytx = cyt[0]
        cyty = cyt[1]

    data.close

    # plot points on elliptic curve
    plt.scatter(x_coords, y_coords)

    # plot some important points
    plt.scatter(bpx, bpy, c='k') # base point
    plt.scatter(akx, aky, c='g') # alice's pub key
    plt.scatter(bkx, bky, c='c') # bob's pub key
    plt.scatter(cltx, clty, c='m') # the unencrypted data
    plt.scatter(cytx, cyty, c='r') # the encrypted data

    print("KEY:")
    print("Black - The base point on the curve (used to generate keys)")
    print("Green - Alice's public key")
    print("Cyan - Bob's public key")
    print("Magenta - Unencrypted data")
    print("Red - Encrypted data")

    # does not work - output is weird
    # viscurve(a, b)

    # display output plot
    plt.show()

if __name__ == "__main__":
    main()
