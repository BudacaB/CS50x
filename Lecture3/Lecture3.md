## Algorithms

https://cs50.harvard.edu/x/2021/notes/3/ 

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

- When a function finishes its work, its frame is <strong>popped</strong> off of the stack,  and the frame immediately below it becomes the new, active, function on top of the stack. This function picks up immediately where it left off.

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

Worst-case scenario: We have to divide a list of n elements in half repeatedly to find the target element, either because the target element will be found at the end of the last division or doesn't exist in the array at all.

Best-case scenario: The target element is at the midpoint of the full array, and so we can stop looking immediately after we start.

O(log n)

Ω(1)

---

#### Bubble sort

- The idea of the algo is to move higher valued elements generally towards the right and lower value elements generally towards the left

Pseudocode:

- set swap counter to a non-zero value
- repeat until the swap counter is 0:
    - look at each adjacent pair
        - if two adjacent elements are not in order, swap them and add one to the swap counter

Worst-case scenario: The array is in reverse order; we have to 'bubble' each of the n elements all the way across the array, and since we can only fully bubble one element into position per pass, we must do this n times.

Best-case scenario: The array is already perfetly sorted, and we make no swaps on the first pass.

O(n<sup>2</sup>)

Ω(n)

---

#### Selection sort

- The idea of the algo is to find the smallest unsorted element and add it to the end of the sorted list

Pseudocode:

- repeat until no unsorted elements remain:
    - search the unsorted part of the data to find the smallest value
    - swap the smallest found value with the first element of the unsorted part

Worst-case scenario: we have to iterate over each of the n elements of the array (to find the smallest unsorted element) and we must repeat this process n times since only one element gets sorted on each pass.

Best-case scenario: Exactly the same! There's no way to guarantee the array is sorted until we go through this process for all elements.

O(n<sup>2</sup>)

Ω(n<sup>2</sup>)

---

#### Insertion sort

- The idea of the algo is to build your sorted array in place, shifting elements out of the way if necessary to make room as you go.

Pseudocode:

- call the first element of the array 'sorted'
- repeat until all elements are sorted:
    - look at the next unsorted element. Insert into the 'sorted' portion by shifting the requisite number of elements

Worst-case scenario: The array is in reverse order; we have to shift each of the n elements n positions each time we make an insertion.

Best-case scenario: The array is already perfectly sorted, and we simply keep moving the line between 'unsorted' and 'sorted' as we examine each element.

O(n<sup>2</sup>)

Ω(n)

---

#### Recursion

- We might describe an implementation of an algo as being particularly 'elegant' if it solves a problem in a way that is both interesting and easy to visualize.
- The technique of <strong>recursion</strong> is a very common way to implement such an 'elegant' solution.
- The definition of a recursive function is one that, as part of its execution, invokes itself.

E.g.:
- the factorial function (n!) is defined over all positive integers
- n! equals all of the positive integers less than or equal to n, multiplied together
- thinking in terms of programming, we'll define the mathematical function n! as fact(n)

- fact(1) = 1
- fact(2) = 2 * 1
- fact(3) = 3 * 2 * 1 ...

or

- fact(1) = 1
- fact(2) = 2 * fact(1)
- fact(3) = 3 * fact(2) ...

fact(n) = n * fact(n-1)

- This forms the basis for a <strong>recursive definition</strong> of the factorial function
- Every recursive function has two cases that could apply, given any input
    - the <em>base case</em>, which when triggered will terminate the recursive process
    - the <em>recursive case</em>, which is where the recursion will actually occur

```
int fact(int n)
{
    // base case
    if (n == 1)
        return 1;

    // recursive case
    else
        return n * fact(n - 1);
}
```

- In general, but not always, recursive functions replace loops in non-recursive functions

```
int fact2(int n)
{
    int product = 1;
    while(n > 0)
    {
        product *= n;
        n--;
    }
    return product;
}
```

- It is possible to have more than one base or recursive case, if the program might recurse or terminate in different ways, depending on the input being passed in.

- <strong>Multiple base cases</strong>: The Fibonacci number sequence is defined as follows:
    - the first element is 0
    - the second element is 1
    - the n<sup>th</sup> element is the sum of the (n-1)<sup>th</sup> and (n-2)<sup>th</sup> elements

- <strong>Multiple recursive cases</strong>: The Collatz conjecture.

- The Collatz conjecture applies to positive integers and speculates that it is always possible to get 'back to 1' if you follow these steps:
    - if n is 1, stop
    - otherwise, if n is even, repeat the this process on n/2
    - otherwise, if n is odd , repeat this process on 3n + 1

- Write a recursive function collatz(n) that calculates how many steps it takes to get to 1 if you start from n and recurse as indicated above.

```
int collatz(int n)
{
    // base case
    if (n == 1)
        return 0;
    // even numbers
    else if (n % 2 == 0)
        return 1 + collatz (n/2);
    // odd numbers
    else
        return 1 + collatz (3 * n + 1);
}
```
---

#### Merge sort

- The idea of the algo is to sort smaller arrays and then combine those arrays together (merge them) in sorted order
- Merge sort leverages something called <strong>recursion</strong>

Pseudocode:

- sort the left half of the array (assuming n > 1)
- sort the right half of the array (assuming n > 1)
- merge the two halves together

Worst-case scenario: We have to split n elements up and then recombine them, effectively doubling the sorted subarrays as we build them up. (combining sorted 1-element arrays into 2-element arrays, combining 2-element arrays into 4-element arrays...)

Best-case scenario: The array is already perfectly sorted. But we still have to split and recombine it back together with this algo.

O(n log n)

Ω(n log n)

---

#### Summary

- Selection sort
    - find the <strong>smallest</strong> unsorted element in the array and swap it with the <strong>first</strong> unsorted element of the array
    - O(n<sup>2</sup>) ; Ω(n<sup>2</sup>)

- Bubble sort
    - swap <strong>adjacent pairs</strong> of elements if they are out of order, effectively 'bubbling' larger elements to the right and smaller ones to the left
    - O(n<sup>2</sup>) ; Ω(n)

- Insertion sort
    - proceed once through the array from left to right, <strong>shifting</strong> elements as necessary to insert each element into its correct place
    - O(n<sup>2</sup>) ; Ω(n)

- Merge sort
    - <strong>split</strong> the full array into subarrays, then <strong>merge</strong> those subarrays back together in the correct order
    - O(n log n) ; Ω(n log n)

- Linear search
    - <strong>iterate</strong> across the array from left to right, trying to find the target element
    - O(n) ; Ω(1)

- Binary search
    - given a <ins>sorted</ins> array, <strong>divide and conquer</strong> by systematically eliminating half of the remaining elements in the search for the target element
    - O(log n) ; Ω(1)