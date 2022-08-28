'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''

from math import exp


def barometric(h, T):
    g = 9.81     # m/(s*s)
    R = 8.314    # J/(K*mol)
    M = 0.02896  # kg/mol
    p0 = 100.0  # kPa

    return p0*exp(-M*g*h/(R*T))


print("The first solution: ")
print(barometric(2469, 245))

# Another solution would be to have h as the only argument, and T as a
# global variable:
T = 245.0


def barometric(h):
    g = 9.81  # m/(s*s)
    R = 8.314  # J/(K*mol)
    M = 0.02896  # kg/mol
    p0 = 100.0  # kPa

    return p0*exp(-M*g*h/(R*T))


print("The second solution: ")
print(barometric(2469))


print("===========================")
print("Class to barometric formula")
print("===========================")


class Barometric:
    def __init__(self, T):
        self.T = T             # K
        self.g = 9.81          # m/(s*s)
        self.R = 8.314         # J/(K*mol)
        self.M = 0.02896       # kg/mol
        self.p0 = 100.0        # kPa

    def value(self, h):
        return self.p0 * exp(-self.M*self.g*h/(self.R*self.T))


b1 = Barometric(T=245)   # Create instance (object)
p1 = b1.value(2469)      # Compute function value
print(p1)

b2 = Barometric(T=273)
p2 = b2.value(2469)
print(p2)


class Barometric1:
    def __init__(self, T):
        self.T = T    # K

    def value(self, h):
        g = 9.81
        R = 8.314
        M = 0.02896
        p0 = 100.0

        return p0 * exp(-M*g*h/(R*self.T))


b3 = Barometric1(T=273)
p3 = b3.value(2469)
print(p3)


class Barometric2:
    def __init__(self, T):

        g = 9.81                # m/(s*s)
        R = 8.314               # J/(K*mol)
        M = 0.02896             # kg/mol

        self.h0 = R*T/(M*g)
        self.p0 = 100.0  # kPa

    def value(self, h):
        return self.p0 * exp(-h/self.h0)


b4 = Barometric2(T=273)
p4 = b4.value(2469)
print(p4)
