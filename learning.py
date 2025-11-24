def outer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


class Numbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def even_odd(self, start, end):
        for i in range(start, end):
            if i%2==0:
                print("even")
            else:
                print("odd")

    def prime_numbers(self):
        for i in range(2, 50):
            for j in range(2, i):
                if i%j==0:
                    break
            else:
                print(i)


num = Numbers(10, 20)
num.even_odd(10, 20)
num.prime_numbers()

