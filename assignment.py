#Mod-env environment

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Hello, {self.name}! My name is {self.name}, nice to meet you')


greet = Person("James")

if __name__ == "__main__":
    print(greet.show_name())