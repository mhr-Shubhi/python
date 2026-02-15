import math
import random

input = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

output=[0,1,1,0]
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

w1= random.random()
w2= random.random()
w3= random.random()
w4= random.random()
w5= random.random()
w6= random.random()

b1= random.random()
b2= random.random()
b3= random.random()

x1=0
x2=1

h1= sigmoid(x1*w1+x2*w2+b1)
h2= sigmoid(x1*w3+x2*w4+b2)

output= sigmoid(h1*w5+h2*w6+b3)

print(output)

target= 1

error= target-output
print("Error",error)

