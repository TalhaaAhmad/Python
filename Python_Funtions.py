# Fuctions In Python
# What About len()

# Example Of Some Inbuilt Fuctions
# list1 = [1,2,3,4,5,6,7]
# print("Maximum Number : ",max(list1))
# print("Minimum Number : ",min(list1))
# print("Sum Of List : ",sum(list1))

# How do Functions Works?
# They may or may not accepts input parameter
# They may or may not return output

# Example Of A Function Which Doesn't Execpt Any Parameter
# and doesn't return Anything
def welcome_message():
    print("Welcome to iNeuron Batch-2 !!!")
welcome_message()

# Example Of A Function Which Doesn't Execpt Any Parameter
# and does return something
def bot_message():
    return "Message from bot !!"
print( bot_message() )
result = bot_message()
print("Output From Bot_message : ", result )

# Example Of A Function Which  Excepts Some Parameter
# and does return output values
def avg_of_two_nums( a, b ):
    print("First Value : ", a)
    print("Last Value : ", b)
    avg_result = (a + b) / 2
    return avg_result

num1 = 10
num2 = 15
output = avg_of_two_nums( num1 , num2 )
print("Result Of avg_of_two_nums : ", output)


# Write A Function To Calculate The Factorial Of Given Number?
def fact(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for num in range(1 , n+1):
        result = result * num
    return result

x = 5
ans = fact(x)
print("Factorial Of ", x , " : ", ans)

x = 0
ans = fact(x)
print("Factorial Of ", x , " : ", ans)


# How to return multiple values from a function
a,b,c = 1,2,3
print("Value of A ", a)
print("Value of B ", b)
print("Value of C ", c)

def sqr_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

num = 3
sqr_ans,cube_ans = sqr_and_cube(num)
print("Square Of ",num," : ",sqr_ans)
print("Cube Of ",num," : ",cube_ans)  

# How to create optional arguments in python
