# Right-Angled Number Triangle Pattern

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**. The task is to print Right-Angled Number Triangle with n lines.

 **Note:**  There is a space between two adjacent number in the pattern.

 **Examples:** 

```
Input: n = 4
Output:
1
1 2  
1 2 3
1 2 3 4
Explanation: For n = 4 there are 4 rows in the output and the number of elements increases with an increase in the row.
```

```
Input: n = 5 
Output:
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
Explanation: For n = 5 there are 5 rows in the output and the number of elements increases with an increase in the row.
```

 **Constraints:** 
1 ≤ n ≤ 20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T17:58:51.535Z  

```py
n = int(input())

# code here
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/right-angled-number-triangle/1)