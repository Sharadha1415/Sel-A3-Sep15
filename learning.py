class Numbers:

    def even_odd(self, start, end):
        for i in range(start, end):
            if i%2==0:
                print("even")
            else:
                print("odd")
    
num = Numbers()
num.even_odd(10, 20)