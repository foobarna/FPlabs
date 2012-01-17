#Given a sort algorithm (let us denote it by SA) that was already discussed at the class, you are
#required to write a generic SA sorting function. Your generic sorting function should take two
#parameters, a list of elements and a function to compare elements (comparison function). This
#comparison function has to be supplied when the sorting function is called.
#You are required to test your generic sorting function using TWO different comparison functions.

def bubbleSort(A,comp):
 global s
 while s:
       s =False
       for i in range(1,len(A)-1):
                if compFunc(A[i],A[i+1])>0:
                                    aux=A[i]
                                    A[i]= A[i+1]
                                    A[i+1]=aux
                                    s = True
 return A

def compFunc(a,b):
   if (a < b):
        return -1
   elif (a > b):
        return 1
   else:
        return 0

def compD(a,b):
    if a>b :
        return False
    else :
        return True
def compC(a,b):
    if a>b:
        return True
    else:
        return False
def bubble_Sort(l,com):
    global i
    global j
    if not com:
        aux=l[i]
        l[i]=l[j]
        l[j]=aux
    if j==len(l)-1:
        j=-1
        i=i+1
    if i==len(l):
        return l
    j=j+1
    return bubble_Sort(l,compD(l[i],l[j]))

com=True
i=0
j=1
list=[1,4,1,89, 5 ,0,6, 8,90, 111]
print bubble_Sort(list,compD(list[0],list[1]))
