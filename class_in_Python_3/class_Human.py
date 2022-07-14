class Human:
    def __init__(self, name, ocupation):
        self.name = name
        self.ocupation = ocupation

    def do_work(self):
        if self.ocupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.ocupation == "actor":
            print(self.name, "shoots filme")

    def speaks(self):
        print(self.name, "says how are you?")

if __name__ == "__main__":
    tom = Human("tom Cruise", "actor")
    tom.do_work()
    tom.speaks()

    print("")
    print("Create another instance of this class: ")
    maria = Human("maria sharapova", "tennis player")
    maria.do_work()
    maria.speaks()





