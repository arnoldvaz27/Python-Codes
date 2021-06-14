import random
import collections


a = [1,2,3,4,5,6]
b = [1,2,33,4,5,6]
#----------------------------------------------------------------------------------
print(max(a)) #max value in list
print(min(a)) #min value in list
print(sum(a))  #sum value of list
print(sorted(a)) #sorted list
a[3] = 10
print(1 not in a) #checking
print(1 in a)
print(1 in [1,2,3,4,5,6])
del(a[3]) #deleting value from list by index
print(a)
del (a[1:4]) #deleting value by slicing
print(a)
print(a[1:3])
print(a+[23,34,34]) #concat
#----------------------------------------------------------------------------------
b.append(23) #appending
print(b)
b.remove(23) #removing the element
print(b)
b.pop() #poping the value from last
print(b)
b.pop(2) #poping the specified value mentioned by using index
print(b)
b.insert(2,42) #inserting the specified value mentioned by using index 
print(b)
b.reverse() #reversing
print(b)
b.sort() #sorting list
print(b)
c = b.count(2) #counting times of emenent occured
print(c)
d = b.index(4) #returning index vaue
print(d)
#----------------------------------------------------------------------------------
e = [2,3,4,5,6,7,]
f = [1,2,3,4,5,6,e]
print(f)
g = [1,2,3,4,5,6,*e]
print(g)
k = g
print(k)
#----------------------------------------------------------------------------------
i = [1,2,3,4,5,6,7]
j = [11,22,33,44,55,66,77,88]
l = [i,j]
print(l[1][0])
#----------------------------------------------------------------------------------
z = len(a)
print(z)

print(a[:z-3])
print(a[z-2:z])
#----------------------------------------------------------------------------------

y = [random.randint(10,100) for n in range(20)]
print(y)
w = [num for num in y if num>20 and num<50]
print(w)
a = sorted(w)
print(a)
k = [(x,x**2,x**3) for x in range(10)]
print(k)
k[:] #deleting all element from list
#----------------------------------------------------------------------------------
ar = [(i,j,k) for i in [1,2,3,4] for j in [1,2,3,4] for k in [1,2,3,4] if i!=j if j!=k if k!=i]
print(ar)
#----------------------------------------------------------------------------------
s = [] #stack
s.append(10) #appending
s.append(20)
s.append(30)
s.pop()   #poping the element
print(s)
#----------------------------------------------------------------------------------
q = collections.deque()
q.append(10)
q.append(20)
q.append(30)
q.popleft() #poping from left
print(q)
#----------------------------------------------------------------------------------
birds = ["Pegion","Crow","Sparrow","Eagle"]
b = birds
birds[0] = "Owl"
print("birds: ",birds)
print("b: ",b)
#----------------------------------------------------------------------------------

