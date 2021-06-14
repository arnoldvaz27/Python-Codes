n = input("Enter the number: ")
sum1 = 0
k = 0
for i in n:
   for j in i:
      j = 1
      a = i[:j]
      b = int(a)
      c = b*b*b
      sum1 = sum1 + c
      k = sum1
      j = j + 1
print(k)
