# invert_binary_tree

A simple test to try and invert a full binary tree in under 10 lines of code.

This mainly works on full binary trees, like this one
```
            1
          /   \
         /     \
        2       3
       / \     / \
      /   \   /   \
     4     5 6     7
```

Array representation
`[1, 2, 3, 4, 5, 6, 7]`

The resulting tree would look like this
```
            1
          /   \
         /     \
        3       2
       / \     / \
      /   \   /   \
     7     6 5     4
```

Array representation
`[1, 3, 2, 7, 6, 5, 4]`

Full binary trees are very predictable as the index range multiplies by 2 at each scope.

Normally, classes and recursion is preferred for performance and scalability. This isn't meant to be a scalable solution, just an experiment to see what is possible.