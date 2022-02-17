import math

# synatx errors

# info = {"name" : "Vinay"; "job" : "SE"}
# print(info)

# indentation error

# if 10 > 5:
# print("okay")

# name errors
# print(c)

# index errors
# a = [1 , 3 , 5]
# print(a[4])

# type erros
# math.sqrt("d")

# value errors
# x = int(input("Enter the number"))
# print(x)

# attribute error
# x = (1,2,3,4)
# x.append(5)

# a = 10
# b = 0
# print(a/b)

x = 0
try:
    x = int(input("Enter the number"))
    print("Hello " + str(x))
    if x > 10:
        raise ValueError("The value is greater than 10")
    print("Inside try block " + str(x))
except TypeError as ex:
    print(ex)
    print("Inside TypeError except block")
    print("Opps! I made a mistake")
except ValueError as ex:
    print(ex)
    print("Inside ValueError except block")
    print("Opps! I made a mistake")
except Exception as ex:
    print(ex)
    print("Inside Generic exception except block")
    print("Unexpected exception occured")
else:
    print("Inside the else block")
finally:
    print("Inside finally block" + str(x))

print("Finished")
