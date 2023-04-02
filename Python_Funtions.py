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
