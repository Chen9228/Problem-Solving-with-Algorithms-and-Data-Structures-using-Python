### Notes for [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/runestone/static/pythonds/index.html#problem-solving-with-algorithms-and-data-structures-using-python)

#### Lists Operation Efficiency Table

| Operation        | Big-O Efficiency |
| ---------------- | ---------------- |
| index []         | $O(1)$           |
| index assignment | $O(1)$           |
| append           | $O(1)$           |
| pop()            | $O(1)$           |
| pop(i)           | $O(n)$           |
| insert(i,item)   | $O(n)$           |
| del operator     | $O(n)$           |
| iteration        | $O(n)$           |
| contains (in)    | $O(n)$           |
| get slice [x:y]  | $O(k)$           |
| del slice        | $O(n)$           |
| set slice        | $O(n+k)$         |
| reverse          | $O(n)$           |
| concatenate      | $O(k)$           |
| sort             | $O(nlogn)$       |
| multiply         | $O(nk)$          |

#### Dictionary  Operations Efficiency Table

| operation     | Big-O Efficiency |
| ------------- | ---------------- |
| copy          | $O(n)$           |
| get item      | $O(1)$           |
| set item      | $O(1)$           |
| delete item   | $O(1)$           |
| contains (in) | $O(1)$           |
| iteration     | $O(n)$           |

#### Linear structures

1. **Stack **

   **an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end ;This end is commonly referred to as the “top.” The end opposite the top is known as the “base.” **

   **LIFO**:**last-in first-out**

   **Reverse order**

   - `Stack()` creates a new stack that is empty. It needs no parameters and returns an empty stack.

   - `push(item)` adds a new item to the top of the stack. It needs the item and returns nothing.

   - `pop()` removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

   - `peek()` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

   - `isEmpty()` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

   - `size()` returns the number of items on the stack. It needs no parameters and returns an integer.

     ##### Infix Prefix Postfix

     | **Infix Expression** | **Prefix Expression** | **Postfix Expression** |
     | -------------------- | --------------------- | ---------------------- |
     | A + B                | + A B                 | A B +                  |
     | A + B * C            | + A * B C             | A B C * +              |
     | (A + B) * C          | * + A B C             | A B + C *              |
     | A + B * C + D        | + + A * B C D         | A B C * + D +          |
     | (A + B) * (C + D)    | * + A B + C D         | A B + C D + *          |
     | A * B + C * D        | + * A B * C D         | A B * C D * +          |
     | A + B + C + D        | + + + A B C D         | A B + C + D +          |

   2. Queue

      **ordered;new items happens at rear ; removal of existing items  happened at  front**

      **FIFO, first-in first-out**

      - `Queue()` creates a new queue that is empty. It needs no parameters and returns an empty queue.

      - `enqueue(item)` adds a new item to the rear of the queue. It needs the item and returns nothing.

      - `dequeue()` removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.

      - `isEmpty()` tests to see whether the queue is empty. It needs no parameters and returns a boolean value.

      - `size()` returns the number of items in the queue. It needs no parameters and returns an integer.

        | `q.isEmpty()`      | `[]`                 | `True`  |
        | ------------------ | -------------------- | ------- |
        | `q.enqueue(4)`     | `[4]`                |         |
        | `q.enqueue('dog')` | `['dog',4]`          |         |
        | `q.enqueue(True)`  | `[True,'dog',4]`     |         |
        | `q.size()`         | `[True,'dog',4]`     | `3`     |
        | `q.isEmpty()`      | `[True,'dog',4]`     | `False` |
        | `q.enqueue(8.4)`   | `[8.4,True,'dog',4]` |         |
        | `q.dequeue()`      | `[8.4,True,'dog']`   | `4`     |
        | `q.dequeue()`      | `[8.4,True]`         | `'dog'` |
        | `q.size()`         | `[8.4,True]`         | `2`     |