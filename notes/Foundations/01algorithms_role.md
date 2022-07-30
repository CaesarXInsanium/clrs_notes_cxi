# Chapter 1: Algorithms

`Algorithm`: set of instructions tailored to solve a problem

- receive **input** and give **output**
- example: take numbers in random order to sort them from least to greatest
- algorithm can only be correct if for each possible instance of a problem, algorithm outputs the correct solution to problem
- incorrect algorithms can be useful if their error rate is low enough

`Instance of Problem`: consists of input that satisfies constraints imposed in problem statement needed to compute solution to problem

Examples of Problems to be solved

- sorting human genomes
- traveling salesman problem
- cryptography and online secret keeping, secure transactions'
- resource allocation 

`Data Structure`: method of storing data in a computer in a way the meets constraints

`Parallelism`: splitting work amongst more than one processor cores and threads to speed up computation times


### Exercises: Algorithms

1. Example of application the requirements computing convex hull 
  - sorting the mail
  - finding the best way to package an item for shipping
2. measures of efficiency
  - amounts of memory required, space. Reliability and error rate. Simplicity and ability for humans to understand it
3. describe data structure 
  - dictionaries: it has insane look up times however if there are too many collisions then it could begin to slow down with the greater amount of times store inside
4. compare contrast the shortest path and traveling salesman
  - they are similar since both are trying to find the best 'path'
5. what sort of problem has only one solution
  - decrypting encrypted files
  - Finding the shortest path across all points in graph

## Algorithms as a Technology

Time and space are two things that are limited. Time that a computer takes to compute a thing and amount of memory and hard drive space in which to do it in

`Efficiency`: time and space required to compute solution compared against other algorithms

## Algorithms and other Technologies

- total system performance can heavily depend on algorithms used in the running of the system
- knowledge and understanding of algorithms is the thing that separates software engineers from script kiddies

### Exercises: Algorithms as a Technology

1. Example of application that requires algorithm as fundamental of function
  - computer graphics and ability to display same image regardless of hardware, display, CPU architecture and graphics card. Layers upon layers of abstraction
2. at which point is insertion sort better than merge sort
  - finds at which value n are both equations equal.
  - 8n^2 = 64nlogn
  - n = 8logn
  - n / log(n) = 8
3. answer is simply 1 
  - same method as above

### Problems

#### Comparison of Running Times

| Time Complexity| 1 second | 1 minute | 1 hour | 1 day | 1 month | 1 year | 1 century |
|----------------|----------|----------|--------|-------|---------|--------|-----------|
| $\log{n}$     | 0        | 1.77     |3.55    | 4.94  | 6.43 | 7.51  | 9.51 |
| $\sqrt{n}$     | 1  | 7.7 | 60  | 294 | 1637 | 5669 | 56693|
| $n$            | 1        | 60       | 3600   | 86400 | 2678400 | 32140800 | 3214080000 | 
| $n\log{n}$     | 1 | 60 | 3600 | 86400 | 2.68e7 | 3.21e7 | 3.21e9 |
| $n^2$          | 0 | 107 | 12803 | 426515 | 1.72e7 | 2.41e8 | 3.1e10 |
| $n^3$          | 1 | 3600 | 1.3e6 | 7.46e9 | 7.2e12 | 1e15 | 1e19 |
| $2^n$          | 1 | 21600 | 4.7e10 | 6.4e14 | 1.9e19 | 3.3e22 | 3.3e28 |
| $n!$           | 2 | ?? | ?? ?? |?? |?? |?? | ?? |

\pagebreak
