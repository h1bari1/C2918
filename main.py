class Hello:
    def __init__(self):
        print("Hello")


class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World!")


hello_world = HelloWorld()


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128


class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"

    def test(self):
        print('test')


class SmartPhone(Display, Computer):
    def print_info(self):
        super().test()   
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone()
iphone.print_info()
