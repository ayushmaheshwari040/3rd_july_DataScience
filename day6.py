                                     ##1.__________Loop__________
##I._____for loop______

# for i in range(10):                  #by default 0 starting point and 10 ending point 
#     print(i,": Hello World")

# for i in range(0,10):                #with 0 starting and 10 ending point
#     print(i,": Hello World 1")

# for i in range(1,10):                #with 1 starting and 10 ending point
#     print(i,": Hello World 2")    
                                  

##II._____while loop______

# i=0
# while(i<=10):
#     print(i,": Hello World")
#     i+=1

# for i in range(100):                 # fixed range known by us
#     print("Welcome")

# condition = True                     # not fixed range,not known by us,infinite loop
# while condition:
#     print("Welcome")

# condition = True                     # condition based
# while condition:
#     user_input=input("Do you want to quit  this program press Y/N:")
#     if(user_input=='Y' or user_input=='y'):
#         condition=False
#     print("Welcome to you in upflairs")  

# for i in range(10):                     #with break keyword(stop the iteration)
#     print(i)
#     if(i==5):
#         break

# for i in range(10):                     #with continue keyword(ignoring the current  iteration)
#     if(i==5):
#         continue
#     print(i)

# count=0
# for i in range(10):
#     count+=1                     
#     continue
#     print("Hello")
# print(count)    

# count=0
# for i in range(10):
#     count+=1                     
#     break
#     print("Hello")
# print(count)

# ls=[52,41,63,96,85,7,45,86,6,9,12,36,72,11,22,33]
# #is 85 present in ls, if it is present than tell me the poisition on which, 85 is present
# count=0
# for item in ls:
#     if(item==85):
#         print("Present at poistion:",count)
#         break
#     count+=1

# print("Final count:",count)  
  

                                            ##2.___________QUIZ___________
#  1. find min and max element in list ,without using in builtin function(min(),max())
#  2. *
#     **
#     ***
#     ****
#     *****
#     ******
#  3. 1
#     12
#     123
#     1234
#     12345   
     