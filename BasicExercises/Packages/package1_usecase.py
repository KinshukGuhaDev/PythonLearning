from package1 import Module1, Module2

def main():
    module1 = Module1()
    module2 = Module2()
    print(module1.greet())
    print("Concatenate 'Hello' and 'World':", module1.concatenate("Hello", "World"))
    print("String multiply 'Hi' 3 times:", module1.string_multiply("Hi", 3))
    print("Cube of 3:", module2.cube(3))
    print("Divide of 10 and 2:", module2.devide(10, 2))

if __name__ == "__main__":
    main()  