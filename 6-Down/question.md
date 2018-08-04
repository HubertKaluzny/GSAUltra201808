## 6 Down: "Alan and Ada"

>Ada is excited about directed acyclic graphs (DAGs). Today, she's learning how to topologically sort a DAG. She has written her own version of the algorithm (in pseudocode) as follows:

```
1 // Notes:
 2 // "n" is the number of nodes in the DAG
 3 // "edges" is a tuple denoting the edges in the DAG
 4 // the nodes are indexed 1, 2, ... n.
 5 // "[]" denotes an empty array.
 6 // "{}" denotes an empty set.
 7 // "x.append(v)" appends "v" at the end of array "x".
 8
 9 def TopoSort(n, edges):
10     ans = []        // array which will contain the output
11     in_deg = []     // in_deg[i] denotes the number of incoming edges at node i
12     open_nodes = {} // a set of nodes
13
14     // initialize "in_deg"
15     for i = 0 to n-1:
16         in_deg.append(0)
17
18     for each edge (u -> v) in edges:
19         in_deg[v]++
20
21     // add nodes with indegree 0 to the set
22     for i = 0 to n-1:
23         if in_deg[i] == 0:
24             open_nodes.add(i)
25
26     while open_nodes is not empty:
27         u = random value from set open_nodes
28         remove u from open_nodes
29
30         ans.append(u)
31
32         for each edge (u -> v) that begins at node u:
33             in_deg[v]--
34             if in_deg[v] == 0:
35                 open_nodes.add(v)
36
37     return ans
```

>The above algorithm is a randomised algorithm, since in line 27 we introduce randomness by picking a random element from the set. Because of this, the value of the <i>open_nodes</i> set can be different across different runs of the algorithm on the same input graph.
>
>Ada's colleague Alan comes along and gives to her a DAG and a set of integers <i>V = {v1, v2, ..., vk}</i>. He says that he'll run the randomised algorithm once. Now, he asks Ada to tell him the probability of the <i>open_nodes</i> set being equal to V at any point in the algorithm's execution. Ada argues that calculating this probability is very difficult, but she can instead tell Alan if the probability is zero or non-zero.
>
>Write a function that takes a tuple of T test cases as input. Each test case is a tuple of:
- An integer N denoting the number of nodes in the graph <i>(1 <= N <= 10^5)</i>
- A tuple of M tuples of integers (U, V), each denoting that a directed edge from node U to node V exists in the graph (<i>M <= 2 x 10^5</i> and  <i>1 <= U, V <= N</i>)
- A tuple of K integers V1, V2, ..., Vk denoting the nodes in the set Alan has given
>
>Your function should output the sum of 2^i * f(i) for all the tests, where i is the  index of the test case in T, and f(i) is 1 if the probability of the ith test case is non-zero, else f(i) is 0.

I don't know much about sorting algorithms for directed acyclic graphs, and I'm pretty sure I missed out on some base cases when calculating the probability.
