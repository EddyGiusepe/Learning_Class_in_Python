'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
Link de estudo: https://en.wikibooks.org/wiki/A_Beginner's_Python_Tutorial/Classes#Creating_a_Class
'''

class Shape_rectangle():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.description = "This shape has not been describe yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area_rectangle(self):
        return self.a * self.b

    def perimeter_rectangle(self):
        return 2 * self.a + 2 * self.b

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.a = self.a * scale
        self.b = self.b * scale


if __name__ == "__main__":
    rectangle = Shape_rectangle(100, 45) # Está é a nossa classe

    area = rectangle.area_rectangle()
    print("The area of rentangle is: ", area)
    print("")

    perimeter = rectangle.perimeter_rectangle()
    print("Finding the perimeter of our rectangle: ", perimeter)
    print("")

    # Making the rectangle 50% smaller
    scale = rectangle.scaleSize(0.5)
    print("A  novas medidas são: ", scale)

    # Re-printing the new area of the rectangle
    new_area = rectangle.area_rectangle()
    print("The new area is: ", new_area)



