## Data Structures

```
int main(void)
{
    int *x; // create a pointer x to an int
    int *y; // create a pointer y to an int

    x = malloc(sizeof(int)); // allocate memory for an integer for pointer x ; now pointer x has a POINTEE

    *x = 42; // go to the address of x and store 42
    // *y = 13; // bug -> no memory allocated

    y = x; // give y the same address as x
    *y = 13; // send 13 to y's address, this overwriting 42
}
```

**Data Structure** - a programming construct, in different programming languages, that allows the programmer to store information differently in the computer's memory.

---
Three important tools:

- struct - create custom structure / data type
- '.' (dot) - access a property of a structure
- '*' (star) - dereference operator - go to a chunk of memory by way of a pointer

---

- (arrays need to be reallocated if changed) - insertion is O(n) / search is O(log n)
- (arrays have random access - indexed)
- (sorted arrays work with binary search)


#### Linked lists

- allows to store a list of elements in a non-sequenatial manner
- each element stores 2 parts, the value, and a pointer to the next element - the last element points at NULL

```
typedef struct node // need to add 'node'
{
    int number;
    struct node *next; // need to add 'struct'
}
node;

node *list = NULL;

node *n = malloc(sizeof(node)); // allocate memoru for a node;

<!-- (*n).number = 2; // assign 2 for the node's number -->

if (n != NULL)
{
    n->number = 2; // syntactic sugar
    n->next = NULL;
}

list = n;

// move across the list
node *tmp = list;
while (tmp->next != NULL)
{
    tmp = tmp->next;
}

// add value 1 in, the list points at 2
n->next = list; // new node points at what list points at, i.e. 2
list = n; // the list points at n

```

- linked lists can allocate elements as they go and change where they point to -> a more dynamic insertion ability
- linked lists lose random access ability -> search is O(n) and also insertion is O(n)

---

#### Trees

##### Binary search tree

```
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;
```

- binary - each node has a max of 2 children
- the tree is recursively sorted -> the left node is smaller, the right node is greater
- binary search and recursion are doable / useful

```
// looking for 50
bool search(node *tree)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (50 < tree->number)
    {
        search(tree->left);
    }
    else if (50 > tree->unmber)
    {
        search(tree->right);
    }
    else
    {
        return true;
    }
}
```

- O(log n) -> search & insert

---

#### Hash table

- array + linked lists inside it
- each position in the array can contain a linked listed - e.g. an array for the alphabet and each letter is an index in the array, all names starting with that letter form a linked list in that 'bucket' / array position
- hash function -> a function / algorithm that decides where values go in the hash table
- e.g. 'Albus' -> hash function -> 0 - outputs index 0 for the first letter for 'A' etc.
- a collision is when two names start with the same letter - this is where the linked list inside the array comes in - in CS one must always think of all the extreme corner cases - e.g. all names start with the same one letter etc.
- one way to decrease collisions is to create more buckets by looking at the first two letters - e.g for 'H' - have 'Ha', 'He' etc. buckets ; or 3, or 4 etc. letters -> helps going towards search constant time O(1)
- tradeoff - still might get O(n) while also using a huge array taking a lot of memory
- ideal hash function - an algorithm that could assure 0 collisions and thus O(1) time
- most computer systems give you best effort - on average it's less than O(n) usually

---

#### Tries

- a trie sacrifices one resource to gain another
- takes up much more memory but does give O(1)
- it is a tree with arrays for nodes
- O(1) constant time - search and insertion

---

#### Abstract data structures

- using arrays, linked lists, trees and hash tables as building blocks to create other custom data structures for different problems

#### Queues

- FIFO - first in first out
- enqueue - get in line / dequeue - get out of line

#### Stacks

- LIFO - last in first out
- push - add to stack / pop - remove from stack

#### Dictionaries

- abstraction on top of a hash table
- key / value pairs

---
---

Data structures can boil down to 4 main basic ideas, four different ways to store sets of data
- arrays
- linked lists
- hash tables
- tries

#### Data structures summary

- arrays
    - insertion is bad - lots of shifting to fit an element in the middle
    - deletion is bad - lots of shifting after removing an element
    - lookup is great - random access, constant time
    - relatively easy to sort
    - relatively small size wise
    - stuck with a fixed size - no flexibility

- linked lists
    - insertion is easy - just tack onto the front
    - deletion is easy once you find the element
    - lookup is bad - have to rely on linear search
    - relatively difficuly to sort - unless you're willing to compromise on super-fast insertion and instead sort as you construct
    - relative small size-wise (not as small as arrays)

- hash tables
    - insertion is a two-step process - hash, then add
    - deletion is easy - once you find the element
    - lookup is on average better than with linked lists because you have the benefit of a real-world constant factor
    - not an ideal data structure if sorting is the goal - just use an array
    - can run the gamut of size

- tries
    - insertion is complex - a lot of dynamic memory allocation, but gets easier as you go
    - deletion is easy - just free a node
    - lookup is fast - not quite as fast as an array, but almost
    - already sorted - sorts as you build in almost all situations
    - rapidly becomes huge, even with very little data present, not great if space is at a premium

    ---
    ---

#### Singly-linked lists

- so far in the course, we've only had one kind of data structure for representing collections of like values
    - structs, recall, give us 'containers' for holding variables of different data types, typically
- arrays are great for element lookup, but unless we want to insert at the very end of the array, inserting elements is quite costly - remember insertion sort?
- arrays also suffer from a great inflexibility - what happens if we need a larger array than we thought?
- through clever use of pointers, dynamic memory allocation, and structs, we can put the pieces together to develop a new kind of data structure that gives us the ability to grow and shrink a collection of like values to fit our needs
- we call this combination of elements, when used in this way, a **linked list**
- a linked list **node** is a special kind of struct with two members:
    - data of some data type (int, char, float...)
    - a pointer to another node of the same type
- in this way, a set of nodes together can be thought of as forming a chain of elements that we can follow from beginning to end

```
typedef struct sllist
{
    VALUE val;
    struct sllist* next;
}
sllnode;
```

- in order to work with linked lists effectively, there are a number of operations that we need to understand:
    1. Create a linked list when it doesn't really exist
    2. Search through a linked list to find an element
    3. Insert a new node into the linked list
    4. Delete a single element from a linked list
    5. Delete an entire linked list

1. Create a linked list

```
sllnode* create(VALUE val);
```

- steps involved:
    1. Dynamycally allocate space for a new sllnode
    2. Check to make sure we didn't run out of memory
    3. Initialize the node's 'val' field
    4. Initialize the node's 'next' field
    5. Return a pointer to the newly created sllnode

2. Search through a linked list to find an element

```
bool find(sllnode* head, VALUE val);
```

- steps involved:
    1. Create a traversal pointer pointing to the list's head
    2. If the current node's 'val' field is what we're looking for, report success
    3. If not, set the traversal pointer to the next pointer in the list and to back to step b
    4. If you've reached the end of the list, report failure

3. Insert a new node into the linked list

```
sllnode* insert(sllnode* head, value val);
```

- steps involved:
    1. Dynamycally allocate space for a new sllnode
    2. Check to make sure we didn't run out of memory
    3. Populate and insert the node at the beginning of the linked list - always make sure to first connect the new node to the current head and then move the pointer to the head
    4. Return a pointer to the new head of the linked list

4. Delete an entire linked list

```
void destroy(sllnode* head);
```

- steps involved:
    1. If you've reached a null pointer, stop
    2. Delete the rest of the list
    3. Free the current node

---

#### Hash tables

- hash tables combine the random access of an array with the dynamism of a linked list
- this means (assuming we define our hash table well):
    - insertion can start to tend toward O(1)
    - deletion can start to tend toward O(1)
    - lookup can start to tend toward O(1)
- we're gaining the advantages of both types of data structure, while mitigating the disadvantages
- to get this performance upgrade, we create a new structure whereby when we insert data into the structure, the data itself gives us a clue about where we will find the data, should we need to later look it up
- the trade off is that hash tables are not great at ordering or soring data, but if we don't care about that, then we're good to go
