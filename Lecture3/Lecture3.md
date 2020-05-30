## Algorithms

2 factors - correctness & design (is it efficient?)

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

### Big O notation ('on the order of')

(x = log<sub>2</sub>n <=> 2<sup>x</sup> = n)

Answers the question - what is the efficiency of your algorithm?

e.g.:

- O(n) - n steps for n elements - linear search
- O(n/2) - n/2 steps if checking 2 items at once -> still close to O(n)
- O(log<sub>2</sub>n) - binary search -> O(log n) ignoring base

The list:

- O(n<sup>2</sup>)
- O(n log n)
- O(n) - linear search
- O(log n) - binary search
- O(1)

---

### Ω - omega (opposite of big O)

O - upper bound of how much time an algorithm can take (worst case scenario)

Ω - best case scenario 

The list:

- Ω(n<sup>2</sup>)
- Ω(n log n)
- Ω(n)
- Ω(log n)
- Ω(1) - linear search, binary search