# Prime-Discriminator
### Problem
<img src="https://d2gd6pc034wcta.cloudfront.net/tier/13.svg" width="13pt"> [BaekJoon 15711 Fantastic Partner](https://www.acmicpc.net/problem/15711)

### Algorithm
- $O(\sqrt{n})$ is not enough! (Time Exceed)
- Miller-Rabin Primality Test

  For a given odd integer n > 2 and integer a(called a base), n is said to be a **strong probable prime to base a** if one of these congruence relations holds:
  
  - $a^d \equiv 1 (mod\ n)$
  - $a^{2^r d} \equiv -1 (mod\ n)$ for some $0 \le r < s$ 
  
    (s is positive integer and d is an odd positive integer that meets $n-1 = 2^s d$ )
