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
    y, x = np.ogrid[-5:300:100j, -5:300:100j]
    # y^2 = x^3 + Ax + B ==> y^2 - x^3 - Ax - B
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    return None

def main():
    # the worst argument parsing of all time
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            if len(sys.argv) == 4:
                # execute ecc implementation with args
                subprocess.call([sys.argv[1], sys.argv[2], sys.argv[3]])

                # get coords file
                if len(sys.argv) == 5:
                    coord_file = sys.argv[4]
                else:
                    if os.path.isfile("coords.csv"):
                        coord_file = "coords.csv"
                    else:
                        print("Please provide a .csv file containing coords")
                        sys.exit()

                # get data file
                if len(sys.argv) == 6:
                    data_file = sys.argv[5]
                else:
                    if os.path.isfile("data.csv"):
                        data_file = "data.csv"
                    else:
                        print("Please provide a .csv file containing an elliptic curve function")
                        sys.exit()
            else:
                # execute ecc implementation without args
                # it is probably not safe to execute anything that gets passed
                subprocess.call([sys.argv[1]])

                # get coords file
                if len(sys.argv) == 3:
                    coord_file = sys.argv[2]
                else:
                    if os.path.isfile("coords.csv"):
                        coord_file = "coords.csv"
                    else:
                        print("Please provide a .csv file containing coords")
                        sys.exit()

                # get data file
                if len(sys.argv) == 4:
                    data_file = sys.argv[3]
                else:
                    if os.path.isfile("data.csv"):
                        data_file = "data.csv"
                    else:
                        print("Please provide a .csv file containing an elliptic curve function")
                        sys.exit()
        else:
            print("Please provide path to ECC executable.")
    else:
        print("Please provide path to ECC executable.")
        sys.exit()

    # read in coords from csv file
    with open(coord_file, 'r') as coords:
        coord_reader = csv.reader(coords, delimiter=',')
        for row in coord_reader:
            x_coords.append(int(row[0]))
            y_coords.append(int(row[1]))
    coords.close()

    # read in other data from data csv
    # data format: A, B, base point, alice pub key, bob pub key, data x, data y
    #               encrypted x, encrypted y
    with open(data_file, 'r') as data:
        data_reader = csv.reader(data, delimiter=',')

        # Get curve function a and b
        ab = next(data_reader)
        a = int(ab[0])
        b = int(ab[1])

        # Get base point of curve (important for keys)
        bp = next(data_reader)
        bpx = int(bp[0][1:])
        bpy = int(bp[1][1:-1])

        # Get Alice's public key
        ak = next(data_reader)
        akx = int(ak[0][1:])
        aky = int(ak[1][1:-1])

        # Get Bob's public key
        bk = next(data_reader)
        bkx = int(bk[0][1:])
        bky = int(bk[1][1:-1])

        # Get clear text data
        clt = next(data_reader)
        cltx = clt[0]
        clty = clt[1]

        # Get cypher text data
        cyt = next(data_reader)
        cytx = cyt[0]
        cyty = cyt[1]

    data.close()

    # plot points on elliptic curve
    plt.scatter(x_coords, y_coords)

    # plot some important points
    plt.scatter(bpx, bpy, label='base point', c='y')    # base point
    plt.scatter(akx, aky, label='alice pub key', c='g')    # alice's pub key
    plt.scatter(bkx, bky, label='bob pub key', c='c')    # bob's pub key
    plt.scatter(cltx, clty, label='unencrypted data', c='m')  # the unencrypted data
    plt.scatter(cytx, cyty, label='encrypted data', c='r')  # the encrypted data

    # legend code
    lgd = plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
    
    # does not work - output is weird
    # viscurve(a, b)

    # save visualization as image (properly displays legend)
    plt.savefig("curve.png", bbox_extra_artists=(lgd,), bbox_inches='tight')

    # display output plot
    plt.show()

if __name__ == "__main__":
    main()
