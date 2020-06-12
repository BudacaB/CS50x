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
- O(n log n) - merge sort
- O(n) - linear search
- O(log n) - binary search
- O(1)

---

### Ω - omega (opposite of big O)

O - upper bound of how much time an algorithm can take (worst case scenario)

Ω - best case scenario

The list:

- Ω(n<sup>2</sup>) - <em>bubble sort</em>, selection sort
- Ω(n log n) - merge sort
- Ω(n) - (bubble sort - after tweak)
- Ω(log n)
- Ω(1) - linear search, binary search

---

### Θ - theta

- If O and Ω are identical

The list:

- Θ(n<sup>2</sup>) - selection sort
- Θ(n log n) - merge sort
- Θ(n)
- Θ(log n)
- Θ(1)

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

#### Merge sort

```
if only one item
    return
else
    sort left half of items
    sort right half of items
    merge sorted halves
```

O(n log n)

---

---

### Recursion

- Code that calls itself
- A function 'search' - is recursive if it calls itself

---

### Call stack

- When you call a function, the system sets aside space in memory for that function to do its necessary work.

  - We frequently call such chunks of memory <strong>stack frames</strong> or <strong>function frames</strong>

- More than one function's stack frame may exist in momery at a given time. If main() calls move(), which then calls direction(), all three functions have open frames (but only one is active).

- When a function finishes its work, its frame is <strong>popped</strong> off of the stack, and the frame immediately and the frame immediately below it becomes the new, active, function on top of the stack. This function picks up immediately where it left off.

---

---

---

### Shorts

#### Linear search

- The idea of the algo is to iterate across the array from left to right, searching for the specified element

Pseudocode:

- repeat starting at the first element:
  - if the first element is what you're looking for (the targer), stop
  - otherwise, move to the next element

O(n) - go through all n elements

Ω(1) - find the target on the 1st element

---

#### Binary search

- The idea of the algo is to divide and conquer, reducing the search area by half each time, trying to find the target
  - in order for this to work, our array must be sorted, else we can't make assumptions about the array's contents.

Pseudocode:

- repeat until the (sub)array is of size 0:
  - calculate the middle point of the current (sub)array
  - if the target is at the middle, stop
  - otherwise, if the target is less than what's at the middle, repeat, changing the end point to be just to the left side of the middle
  - otherwise, if the target is greater than what's at the middle, repeat, changing the start point to be just to the right of the middle
