#ex 16
#Generate all numbers of n digits with the property that 
#no number has two identical neighboring subsequences. 
#For example, for n=6, 121312 is correct, and 121313 and 
#132132 are not correct.

def print_it(sol, n):
    for i in range(1, n + 1):
        print sol[i],
    print
    return

def succesor(n, k, sol):
    if sol[k] < 9 :
        sol[k] = sol[k] + 1;
        return True
    return False

def is_valid(k, sol):
    if sol[1] == 0 : return False
    x = k / 2 + 1
    for j in range (1, x):
        y = k - j + 1
        for i in range (1, y):
            a = i
            b = i + j
            c = i + j
            d = i + j + j
            if sol[a:b] == sol[c:d] : return False
    return True

def is_solution(k, n):
    return (k == n + 1)

def bcktr(n, sol):
    k = 1
    sol[k] = -1
    while k > 0 :
        if succesor(n, k, sol):
            if is_valid(k, sol) :
                if k == n :
                    print_it(sol, n)
                else :
                    k += 1
                    sol[k] = -1
        else:
            k -= 1


def main():
    sol = []
    n = input('n=')
    for i in range(n + 1): sol.append(i);
    bcktr(n, sol)

main()
