#example to apply condition for licence
"""
age=int(input("enter your age:"))

if(age >=18):
    print("can apply for licence")
else:
    print("you cant apply for licence")


#example of trafic lights

light=input("enter the signal you see:")

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")  
elif(light=="yellow"):
    print("wait")
else:
    print("you are fool")

    #example of giving vote

    age=17
    if(age>=18):
        print("i can give the vote")
    else:
        print("i cant give the vote")
        """
    #example of student marksheet
"""
mark=int(input("enter your mark:"))

if(mark>=90 and mark<100):
      grade="A"
elif(mark>=80 and mark<90):
      grade="B"
elif(mark>=70 and mark<80):
        grade="C"
elif(mark>60 and mark<70):
        grade="D"
elif(mark>=50 and mark<60):
        grade="E"      
else:
        grade="F" 
print("grade of the student is:",grade)  
"""

#list
list=[45,67,34,90,76,32]
print(list)
print(type(list))
print(list[0])#45
print(list[1])#67
print(list[2])#34
print(len(list))#6

"""
#list slicing
marks=[32,76,98,67,56,90]
print(marks[1:5])#[76,98,67,56]
print(marks[3:5])#[67,56]
print(marks[:5])#[32,76,98,67,56]
print(marks[3:])#[56,90]
"""

"""
list=[2,1,3]
list.append(5)
print(list) #[2,1,3,5]
list.sort()
print(list) #[1,2,3,5]
print(list.sort(reverse=True))
print(list) #[5,3,2,1]
list.reverse()
print(list) #[1,2,3,5]
list.insert(1,4)
print(list) #[1,4,2,3,5] 
list.pop(4)
print(list)#[1,4,2,3]
"""

#task->program-1
"""
number=int(input("enter a number:"))
if(number%2==0):
  print("enter number is even:")
else:
   print("enter number is odd:")

"""
#program-2
"""
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if(a>b and a>c):
   print("a is grater:")

elif(b>a and b>c ):
   print("b is greater:")
else:
   print("c is grater") 
   """ 

#program-3
"""
number=int(input("enter a number:"))
if(number%7==0):
    print("this number is multiple of 7:")
else:
    print("this number is not multiple of 7:")
    """    
 























































































