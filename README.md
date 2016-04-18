# WAT

algo 2016 course,
nice refresher


# HOW

#### python3
```
python3 APlusB.py
```

#### python3
```
pip install memory_profiler
pip install psutil
python -m memory_profiler fib_table.py  
```
add `@profile` to functions you want to profile

#### cpp
`g++ -pipe -O2 -std=c++11 APlusB.cpp -o AplusB.exe`

#### test python3
```
pip install -U pytest
py.test ./greedy/different_summands/test_different_summands.py  
```

## Stress test

- compare differences on fast and slow solution
- debug start with small number set


## Algorithms design

- greedy algorithms
    - local solution -> try to generalize
    - pick gready choice and prove its safe
- divide and conquer
    - solve all pices separetly and put them together
- dynamic programming
    - large problem 
    - solve small lemma
- naive algorithms
    - slow
    - by the definition of the problem
    - all enumerations to compute best cases
    - sth that runs
    - prove that you understood the problem
    
## Decreasing O(n)
- standard tools:
    - sorting
    - new data structure
- finally use magic



## Data structct

### double linked list
- midle elems O(n)
- add/r emove front O(1)
- insert between nodes O(1)

### bread first
#### depth first
  ```
  q.que(root)
  while not q.deque
    print node
    if node.left:
        q.que(node.left)
  ```      
#### in order traverse
  ```
  if !tree return
  InOrdeTraversal(tree.left)
  print tree.key
  InOrderTraversal(tree.right)
  ```