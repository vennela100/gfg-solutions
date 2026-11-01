# Count Primes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer `n`, return  *the number of prime numbers that are strictly less than*  `n`.

 

 **Example 1:** 

```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

```

 **Example 2:** 

```
Input: n = 0
Output: 0

```

 **Example 3:** 

```
Input: n = 1
Output: 0

```

 

 **Constraints:** 

- 0 <= n <= 5 * 106

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 18.9 MB  
**Submitted:** 2026-11-01T17:54:46.287Z  

```py
class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        if n<=2:
            return 0
        for i in range(2,n):
                for j in range(2,int(i**0.5)+1):
                    if i%j==0:
                        return False
                count+=1
        return count
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-primes/)