#ex 16

def print_it(sol, n):
    for i in range(1, n + 1):
        print sol[i],
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

def bcktr(n, k, sol):
    if is_solution(k, n):
        print_it(sol, n)
        print '\n'
    else :
        sol[k] = -1
        while succesor(n, k, sol) :
            if is_valid(k, sol) : bcktr(n, k + 1, sol)

def main():
    sol = []
    n = input('n=')
    for i in range(n + 1): sol.append(i);
    bcktr(n, 1, sol)

main()
