"""
 Shellsort is one of the oldest sorting algorithms, named after its inventor D.L. Shell (1959) [She 59].
 It is fast, easy to understand and easy to implement.
 The idea of Shellsort is the following:
   1. arrange the data sequence in a two-dimensional array
   2. sort the columns of the array
 The effect is that the data sequence is partially sorted.
 The process above is repeated, but each time with a narrower array, i.e. with a smaller number of columns.
 In the last step, the array consists of only one column. In each step, the sortedness of the sequence is increased,
 until in the last step it is completely sorted.
 Example:
   3 10 34 9 0 2 78

   3 10 34              3 0 2
   9 0 2      -->       9 10 34
   78                   78

   3 0                 2 0
   2 9       -->       3 9
   10 34               10 34
   78                  78

   2                 0
   0                 2
   3                 3
   9         -->     9
   10                10
   34                34
   78                78
   An in-place algorithm is an algorithm which transforms input using a data structure
   with a small, constant amount of extra storage space.
   Shell sort is an in-place algorithm.
"""
def shellSort(l):
    inc = len(l) // 2
    while inc:
        for i, el in enumerate(l):
            while i >= inc and l[i - inc] > el:
                l[i] = l[i - inc]
                i -= inc
            l[i] = el
        #inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        inc-=1

list = [ 3, 10, 34, 9, 0, 2, 78]
shellSort(list)
print list # [-5, 2, 4, 7, 8, 22]