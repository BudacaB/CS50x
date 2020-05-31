## Algorithms

2 factors - correctness & design (is it efficient?)

### Searching

#### Linear search
- unsorted array - from start to finish (in a line)

```
for i from 0 to n - 1
    if i'th element is 50
        return true
return false
```
---

#### Binary search (divide & conquer)
- sorted array - split in 2 each time and decide on direction

```
if no items
    return false
if middle item is 50
    return true
else if 50 < middle item
    search left half
else if 50 > middle item
    search right half
```
---
---

### Big O notation ('on the order of')

(x = log<sub>2</sub>n <=> 2<sup>x</sup> = n)

Answers the question - what is the efficiency of your algorithm?

e.g.:

- O(n) - n steps for n elements - linear search
- O(n/2) - n/2 steps if checking 2 items at once -> still close to O(n)
- O(log<sub>2</sub>n) - binary search -> O(log n) ignoring base

The list:

- O(n<sup>2</sup>) - bubble sort, selection sort
- O(n log n)
- O(n) - linear search
- O(log n) - binary search
- O(1)

---

### Ω - omega (opposite of big O)

O - upper bound of how much time an algorithm can take (worst case scenario)

Ω - best case scenario 

The list:

- Ω(n<sup>2</sup>) - <em>bubble sort</em>, selection sort
- Ω(n log n)
- Ω(n) - (bubble sort - after tweak)
- Ω(log n)
- Ω(1) - linear search, binary search
---
---

### Sorting

#### Bubble sort

n - 1 passes required


(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2

n(n - 1) / 2 - total number of comparisons

```
repeat n-1 times
(repeat until no swaps) - improvement
    for i from 0 to n-2
        if i'th and i+1'th elements are out of  order
            swap them
```
O((n-1) x (n-2)) => O(n<sup>2</sup> -3n + 2) => O(n<sup>2</sup>) 

Ω(n<sup>2</sup>) - it will carry out the steps regardless

---

#### Selection sort

```
for i from 0 to n-1
    find smallest item between i'th item and last item
    swap the smallest item with the i'th item
```
n + (n - 1) + (n - 2) + ... + 1 = n(n + 1) / 2 => (n<sup>2</sup> + n) / 2 => O (n<sup>2</sup>)

Ω(n<sup>2</sup>)

---
---

### Recursion

- Code that calls itself
- A function 'search' - is recursive if it calls itself

