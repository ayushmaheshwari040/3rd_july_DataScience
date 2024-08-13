                                     ## 1.__________Fuctions in Python__________


##_____Brief explanation about function____

# Function is a block of code that performs a specified task.
# It takes input from the user , process and gives output.
# Function is a reusale code which can be used multiple times.

# Two types of Function
# 1. Predefined ( In-Built ) --> print(),len(),type(),max() etc.
# 2. User-Defined

# Function:-
# 1. Function Defination---->>>> def function_name():
# 2. Function body
# 3. Function Calling---->>>> function_name()
                                                              

##_____Program to Add two numbers using fuction_____ 


# # function defination with parameters 
# def add_two(num1, num2):                            
#     output = num1 + num2
#     return output 


# a = int(input('enter first number : '))
# b = int(input('enter second number : '))

# # function calling 
# output = add_two(num1=a,num2=b)
# output = add_two(a,b)  # positional arguments
# print("Your addition by method 1 is : ",output)
# print("Your addition by method 2 is : ",add_two(a,b))

##_____Function to count length of list without len()_____

# ls = [23,43,56,76,87,98,90,65,34,21,1,2,3,4,5]

# def my_len(ls):
#     count=0
#     for i in ls:
#         count+=1
#     print(count)

# my_len(ls)



##_____Function to count sum length of list without sum()_____

# ls = [1,2,3,4,5,6,7,8,9,10]

# def my_len(ls):
#     sum=0
#     for i in ls:
#         sum+=i
#     print("Sum : ",sum)
# my_len(ls)


##_____Average Finder_____

# ls = [1,2,3,4,5,6,7,8,9,10]

# def my_len(ls):
#     sum=0
#     count=0
#     for i in ls:
#         sum+=i
#         count+=1
#     print("average : ",sum/count)

# my_len(ls)

##_____Even Finder()_____

# ls=[1,2,3,4,5,6,7,8,9,10]
# def even_finder(ls):
#     ls1=[]
#     for i in ls:
#         if(i%2==0):
#             ls1.append(i)
#     print("Even Numbers in List : ",ls1)
# even_finder(ls)

##_____Average Finder Even()_____

# ls=[1,2,3,4,5,6,7,8,9,10]
# def even_finder(ls):
#     ls1=[]
#     count = 0
#     sum = 0
#     for i in ls:
#         if(i%2==0):
#             count+=1
#             sum+=i
#     print("Average of Even Numbers in List : ",sum/count)
# even_finder(ls)

##_____Min()_____

# ls=[2,3,4,5,6,7,1,8,9,10]
# def my_min(ls):
#     min = ls[0]
#     for i in ls:
#         if(i<min):
#             min = i
#     print("The Min : ",min)
# my_min(ls)


##_____Max()_____

# ls=[2,3,4,5,6,7,1,8,9,10]
# def my_max(ls):
#     max = ls[0]
#     for i in ls:
#         if(i>max):
#             max = i
#     print("The Max : ",max)
# my_max(ls)

##_____Module in python_____

# .py file is called a Module
# using the example of employe and manager
# using module we can use another file code



