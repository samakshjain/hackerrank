from math import atan, degrees, ceil, sqrt

AB = int(raw_input())
BC = int(raw_input())


theta = int(round( degrees( atan(float(AB)/BC))))

print str(theta) + "°"