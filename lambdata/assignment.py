#Mod-env environment

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Hello, {self.name}! My name is {self.name}, nice to meet you')

class BasicMath:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   # Addition
   def add(self):
       return self.a + self.b

class Fibo:

    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def fib2(n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

greet = Person("James")
basicmath = BasicMath(1, 2)

def report():
   print(f'The sum of {basicmath.a} and {basicmath.b} is {basicmath.add()}')


if __name__ == "__main__":
    print(greet.show_name())
    print(report())
