Software for visualization of Eliptic Curve Cryptography algorithms. Requires a CSV of points on an elliptic curve.
Project for my CS480 class, Computational Geomety.

Usage:
python vis.py path_to_ECC_executable [coords_csv] [data_csv]

coords_csv: a csv file of coordinate pairs where the first column is x values and second column is y values. A row is a pair.

data_csv: a csv file containing the elliptic curve a and b values, the base point on the curve, alice's public key, bob's public key, the unencrypted data point, and the encrypted data point.

Dependencies for vis.py: numpy, matplotlib
