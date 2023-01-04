# Prime-Discriminator
### Problem
<img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" width="13pt"> [BaekJoon 15711 Fantastic Partner](https://www.acmicpc.net/problem/15711)

### Ranking

- 1st place in Python3 (2023.01.05)

![소수 rank](https://user-images.githubusercontent.com/62281102/210597807-f928a045-ce73-4460-b66b-da56f6b9e43e.png)


### Algorithm
- Sieve of Eratosthenes( $O(\sqrt{n})$ ) is not enough! (Time Exceed)
- [Miller-Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

  For a given odd integer n > 2 and integer a(called a base), n is said to be a **strong probable prime to base a** if one of these congruence relations holds:
  
  - $a^d \equiv 1 (mod\ n)$
  - $a^{2^r d} \equiv -1 (mod\ n)$ for some $0 \le r < s$ 
  
    (s is positive integer and d is an odd positive integer that meets $n-1 = 2^s d$ )
    
  For using given set of a, classification of numbers smaller than given n are guaranteed.
  
  - if n < 2,047, it is enough to test a = 2;
  - if n < 1,373,653, it is enough to test a = 2 and 3;
  - if n < 9,080,191, it is enough to test a = 31 and 73;
  - if n < 25,326,001, it is enough to test a = 2, 3, and 5;
  - if n < 3,215,031,751, it is enough to test a = 2, 3, 5, and 7;
  - if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
  - if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
  - if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
  - if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
  - if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.
  

- [Goldbach's Conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)
  
  Every even natural number greater than 2 is the sum of two prime numbers.
  
  The conjecture has been shown to hold for all integers less than $4 × 10^{18}$ but remains unproven despite considerable effort.
  
### Questions

- [ ] a = (2, 7, 61)에 대해서는 통과하는데 (2, 3, 5, 7, 11, 13, 17)에 대해서는 통과하지 않는 이유
