# Perfect Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A  **perfect number**  is a  **positive integer**  that is equal to the sum of its  **positive divisors**, excluding the number itself. A  **divisor**  of an integer `x` is an integer that can divide `x` evenly.

Given an integer `n`, return `true` *if* `n` *is a perfect number, otherwise return* `false`.

 

 **Example 1:** 

```
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

```

 **Example 2:** 

```
Input: num = 7
Output: false

```

 

 **Constraints:** 

- 1 <= num <= 108

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 63.26%)  
**Memory:** 19.1 MB (beats 82.01%)  
**Submitted:** 2026-11-01T17:00:17.627Z  

```py
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum+=i+num//i
                
        return num==sum
```

---

[View on LeetCode](https://leetcode.com/problems/perfect-number/)