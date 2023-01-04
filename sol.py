import sys
from math import sqrt, floor

def input_single(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

def isprime(n):
    '''
    prime discriminator based on Miller-Rabin primality test
    it can discriminate primes with confidence below 4,759,123,141 when a = (2, 7, 61).
    (Actually, this set of a is not enough for the range suggested in the problem(4x10^12), however, 
     it still passes while a = (2, 3, 5, 7, 11, 13, 17) doesn't.
     This remains unresolved question: https://www.acmicpc.net/board/view/95065)
    for more details: https://ko.wikipedia.org/wiki/%EB%B0%80%EB%9F%AC-%EB%9D%BC%EB%B9%88_%EC%86%8C%EC%88%98%ED%8C%90%EB%B3%84%EB%B2%95
    '''
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d >> 1
        s += 1

    for a in [2, 7, 61]:
        prime = False
        v = pow(a, d, n)
        if v == 1:
            prime = True
            continue

        for r in range(s):
            if v == n - 1:
                prime = True
                continue
            v = pow(v, 2, n)
        
        if prime == False:
            return False
        
    return prime

T = input_single()
for _ in range(T):
    A, B = input_list()
    if (A + B) < 4:
        print("NO")
    elif (A + B) % 2 == 0:
        print("YES")        ## Goldbach's Conjecture
    elif isprime(A + B - 2):
        print("YES")
    else:
        print("NO")
