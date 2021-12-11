# list = [10, 20, 30 , 40, 50]
# print(list[::-1])
# list.reverse()
# print(list)

# -------------------------------------

# new_list = []
# for num in list[::-1]:
#     new_list.append(num)

# print(new_list)

# nums = [10,20,30,40,50,60,70,80,90]

# def myFilter(func, list, targetNumber):
#     filtired_nums = []
#     for num in list:
#         result = func(num, targetNumber)
#         if result:
#             filtired_nums.append(num)
#     return filtired_nums


# def less(num, target):
#     return num < target

# def greater(num, target):
#     return num > target


# print(myFilter(less, [10,20,30,40,50,60,70,80,90], 50))
# print(myFilter(greater,[10,20,30,40,50,60,70,80,90], 30))


# def calculator(func, a, b):
#     return func(a,b)
        

# def add(a,b):
#     return a + b

# def divide(a,b):
#     return a / b

# def subtract(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# print(calculator(add,2,3))
# print(calculator(divide,10 ,2))
# print(calculator(subtract,10 ,2))
# print(calculator(multiply,10, 2))


# def sum_numbers(text:str):
#     acc = 0
#     list = text.split(' ')
#     for word in list:
#         if word.isdigit():
#             acc += int(word)
#     return acc

# print(sum_numbers('hi'))
# print(sum_numbers('11'))


# def chekio(array):
#     sum=0
#     for i in range(0, len(array), 2):
#         sum += array[i]
#     return sum * array[-1] if array else 0

# print(chekio([0,1,2,3,4,5,]))
# print(chekio([1,3,5]))
# print(chekio([6]))
# print(chekio([]))