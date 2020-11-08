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