# TASK5. HOMEWORK-----------ATABEK ARAPOV
# 1)
# def rec(x):
#     if x == 0:
#         return []
#     else:
#         return rec(x - 1) + [x]
# print(rec(13))

# 2)
# def factori(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num + factori(num - 1)
# print(factori(10))

# 3)
# def reverse(number):
#     if number < 10:
#         return number
#     return int(str(number % 10) + str(reverse(number // 10)))
# print(reverse(4747))
    
# 4)
# def fibonacci(number):
#     if number <= 1:
#         return number
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)
# print(fibonacci(10))

# 5)
# basket = dict()
# def stepPerms(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     if n not in basket:
#         basket[n] = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
#     return[n]











