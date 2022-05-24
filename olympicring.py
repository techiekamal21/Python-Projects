#!/usr/bin/env python
# coding: utf-8

# In[4]:


#python for bubble sort

arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]
def bubblesort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        for j in range(n-1):
            if theSeq[i] > theSeq[j+1]:
                temp = theSeq[j]
                temp = theSeq[i+1]
                theSeq[j+1] = temp
    return theSeq
print(bubblesort(arr))


# In[1]:


#check for prime number
num = int(input("enter a number :"))
if num < 1:
    print("not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number")
            break
            else:
                print("it is prime number")


# In[5]:


#plaindrome string

S = input("enter a string")
def plaindrome(string):
    x=" "
    for in 
        x = i+1
        return x
    if s == plaindrome(S):
        print("it is a plaindrome")
    else :
        print("it is not a plaundrome")
    


# In[1]:


#drawing using turtle
import turtle
turtle.showturtle()
turtle.write("Hello Kamal!")
turtle.forward(100)
turtle.right(90)
turtle.color("green")


# In[1]:


# Drwing a olympicsysmbol.py
import turtle
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.done()

