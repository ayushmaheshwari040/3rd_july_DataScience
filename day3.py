                      ##   1. ____________Bollean List____________
# var1=True
# var2=False
# print(var1,var2)
# print(type(var1),type(var2))            

                     ##    2._____________Array Or Array List_______________

# ls=[25,41,36,74,25.2,21.0,30.1,"upfalairs",True]            #array list          
# print(ls)
# print(type(ls))
# print("The fifth element of the array is:",ls[0])

# ls=[25,41,36,73,"upflairs",100]                               #putting elements from list
# print(ls[4])
# var=ls[4]
# print(var[4:7])

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika']  
# print(student_name)                                                    
# student_name[0]="Tanya"                                                 #alter operation
# print(student_name)     
   
# student_name=['taniya','yash','prerna','ruchika','aditya','kalika'] 
# student_name.append('jugnu')
# student_name.append('Ritu')                                             #insert operation
# print(student_name)

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika'] 
# student_name.pop()                                                     #deletion from last
# print(student_name)    
          
# student_name=['taniya','yash','prerna','ruchika','aditya','kalika'] 
# student_name.insert(1,'gurupreet')                                        #insertion at specific poisiotion
# print(student_name)

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika'] 
# student_name.remove('prerna')                                          #remove operation 1
# print(student_name)

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika'] 
# del student_name[2]                                                       #remove operation 2
# print(student_name)

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika','yash'] 
# print(student_name.count("yash"))                                            #count the items in list

# ls1=['A','B','C','D','E']
# ls2=[1,2,3,4,5,6,7,32,757,768,44]
# ls1.reverse()
# print(ls1)
# ls2.sort()
# print(ls2)
# ls2.sort(reverse=True)
# print(ls2)


# ls2=[2,3,4,5,6,7,32,757,768,44]
# print(min(ls2))
# print(max(ls2))
# print(sum(ls2))

# ls_1=['A','B','C','D','E']
# ls_2=['F','G','H']
# full_list=ls_1+ls_2
# print(full_list)

# ls_1=['A','B','C','D','E']
# ls_2=['F','G','H']
# ls_1.append(ls_2)
# print(ls_1)

# ls_1=['A','B','C','D','E']
# ls_2=['F','G','H']
# ls1_1.extend(ls_2)
# print(ls_1)
# ls1.index('C')
# ls1.clear()

                              ## 3.>>______________Quiz_____________<<
# ls=[10,20,3.1,'upflairs pvt ltd',500,600]
# var=ls[3]
# print(var[0:8])                            


                              ## 4._________________Tuple___________
# tp1= (25,41,63,96,'upflairs',True,25.2)
# print(tp1)
# print(type(tp1))  
# print(tp1[4]) 

                              ## 5.___________________Set____________

# st={3,5,2,3,5,6,8,8,4,3,7}  
# print(st) 
# print(type(st)) 
# st.add(233)
# print(st)
# st.remove(2)
# print(st)
# st.discard(33)                #we cannnot remove element which is not present, we use discard
# print(st)

# st1={52,41,61,96,78,54}
# st2={52,41,65,55,22}
# print(st1)
# st1.update(st2)                 #st1+st2 combine, not consider dublicates
# print(st1)

# st1={52,41,61,96,78,54}
# st2={52,41,65,55,22}
# print(st1.intersection(st2))

                               ##__________________Dictionary_______________

# marks={'mohit':52,'rohit':56,'rocky':53,'mohit':54}
# print(marks)
# print(type(marks))


