# Print Solid Square

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n**, print a solid square pattern of size n × n using "  * " (a star followed by exactly one space).

 **Examples:** 

```
Input: n = 5
Output:
 **   **  *
 **   **  *
 **   **  *
 **   **  *
 **   **  *
Explanation: A solid square of size 5 × 5, with each row containing 5 stars followed by a single space.
```

```
Input:  n = 4
Output:
 **   **  
 **   **  
 **   **  
 **   **  
Explanation: A solid square of size 4 × 4, with each row containing 4 stars followed by a single space.

```

**Constraints:
**1 ≤ n ≤ 10

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T17:23:11.854Z  

```py
n = int(input())

# code here
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-square-wall-1605682270/1)