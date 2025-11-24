# if 10%2==0:
#     print("even")

#-------------------------------------------
#
# num = int(input("Enter the number : "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# #-------------------------------------------
#
# for num in range(1, 10):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")

# #-------------------------------------------
#
# def even_odd():
#     for num in range(1, 10):
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")

#-------------------------------------------

# class Numbers:
#
#     def even_odd(self, start, end):
#         for num in range(start, end):
#             if num%2==0:
#                 print("even")
#             else:
#                 print("odd")

for i in range(2, 50):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)




































