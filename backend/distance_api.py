# https://www.johndcook.com/blog/2015/10/24/distance-to-mars/
from numpy import exp, pi, absolute


def earth(t):
    return exp(2 * pi * 1j * t)


def mars(t):
    r = 1.524  # semi-major axis of Mars orbit in AU
    return r * exp(2 * pi * 1j * (r ** -1.5 * t))


def distance(t):
    return absolute(earth(t) - mars(t))


def distance_km(t):
    return distance(t) * 1.496e+8
