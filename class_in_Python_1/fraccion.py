from libFraccion import Fraccion
from libFracMix import FracMix

def main():
    a = Fraccion(2, 3)
    print(a)

    b = Fraccion(4, 3)
    print(b)
    print(a+b)

    c = FracMix(4, 8, 6)
    print(c)

    d = FracMix(3, 7, 4)
    print(d)

    print(c + d)


if __name__ == "__main__":
    main()

