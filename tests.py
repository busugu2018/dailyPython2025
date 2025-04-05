# import os

# os.mkdir('thumbnails')
# os.chdir('thumbnails')

# sizes = ['small', 'medium', 'large']

# for size in sizes:
#     os.mkdir(size)

# print(os.listdir())


# def fun(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s


# for x in fun(2):
#     print(x, end='');




# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# # Insert line of code here.
# print(foo)


# my_list = [1, 2, 3]
# # Insert line of code here.
# print(foo)

# try:
#    # Code that may raise an exception
#    risky_call()
# except ValueError:
#    print("Caught ValueError")
# except TypeError:
#    print("Caught TypeError")
# except Exception:
#    print("Caught a different exception")



# #q8
# try:
#     raise Exception("An error occurred")
# except ValueError as ve:
#     print("ValueError:", str(ve))
# except BaseException as be:
#     print("BaseException:", str(be))
# except:
#     print("Caught some other exception")




# def generate_pattern(n):
#     def create_pattern():
#         return '**' * n

#     return create_pattern

# pattern1 = generate_pattern(1)
# pattern2 = generate_pattern(2)
# print(pattern1() + pattern2())

import os

os.mkdir('pictures')
os.chdir('pictures')

print(os.getcwd())







