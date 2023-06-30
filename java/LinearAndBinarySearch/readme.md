## Search Algorithms

### Linear Search
This is the easiest way to search for an element on a list. Its complexity is ``O(n)`` because it
reads all the elements on the worst case once. The best case of this algorithm is when the element
is located at the first position of the array and the worst case is when it's not located at
any position of the array.

### Binary Search
This is a faster algorithm than linear search because its complexity is ``O(log(n))``. However
the value list must be sorted for its full functioning. Its best case happens when the element is 
located at the very center of the array and its worst case happens when the element is located at 
the extremity of the array.