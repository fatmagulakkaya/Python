

a=[1,2,2.5,"merhaba"]
b=[4,5,6,7]
#a*b  #hatalı

type(a)

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

ab

import numpy as np
print(np.__version__)

aa=np.array([1,2,3,4])
bb=np.array([5,6,7,8])

aa*bb

type(aa)

c=np.array([1,2.5,3,6.5])
c

c=np.array([1,2.5,3,6.5],dtype="int")
c

#Sıfırdan array olusturma

np.zeros(4)
np.zeros((2,3))
np.zeros((3,3),dtype="int")

np.ones((2,2))
np.ones((4,2),dtype="int")

np.full((3,3),5)

np.arange(0,21,2)

np.linspace(0,1,9)

np.random.randint(1,100,(4,5))

np.random.normal(10,5,(4,5))

#Matrisin özelliklerini okuma

m=np.random.randint(1,100,(4,5))

m.ndim # boyutunu verir

m.shape #satır,sutun bilgilerini verir

m.size # veri sayısını verir

m.dtype # turunu verir

# Reshapping

n=np.arange(1,10)
n
n.size
n.ndim

n.reshape((3,3))
n
k=n.reshape((3,3))
k

#Array Birleştirme

x=np.array([1,2,3])
y=np.array([4,5,6])

np.concatenate([x,y])
np.concatenate([x,y],axis=0)
np.concatenate([x,y],axis=1) # hatalı / cok boyutlu dızılerde calısır

a=np.array([[1,2,3],[4,5,6]])
a
a.shape

a1=np.concatenate([a,a]) #satır bazında birleştirme
a1

a1=np.concatenate([a,a],axis=0) #satır bazında birleştirme
a1
a1.shape

a1=np.concatenate([a,a],axis=1) #sutun bazında bırlestırme
a1
a1.shape

#İki boyutlu arrayleri ayırma

l=np.arange(16).reshape(4,4)
l

np.vsplit(l,2)
l
ust,alt=np.vsplit(l,2)
ust
alt

np.hsplit(l,2)
sol,sag=np.hsplit(l,2)
sol
sag


