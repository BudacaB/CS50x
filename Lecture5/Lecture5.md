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