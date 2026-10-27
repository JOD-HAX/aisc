# Sample Inputs for All 23 AISC Practicals

Each block contains the exact lines to type, in order, using the reference PDF's primary sample.

## 01 - Discrete Perceptron, Unipolar Binary

```text
4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
0
1
10
```

## 02 - Discrete Perceptron, Bipolar Binary

```text
4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
10
```

## 03 - Continuous Perceptron, Unipolar Sigmoid

```text
4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
0
1
5000
```

## 04 - Continuous Perceptron, Bipolar Sigmoid

```text
4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
5000
```

## 05 - Hebbian, Unipolar Binary

```text
4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
-2.5
1
```

## 06 - Hebbian, Bipolar Binary

```text
4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
```

## 07 - Hebbian, Unipolar Continuous

```text
4
0 0 0
0 1 0
1 0 0
1 1 1
0 0
-2.5
1
```

## 08 - Hebbian, Bipolar Continuous

```text
4
-1 -1 -1
-1 1 -1
1 -1 -1
1 1 1
0 0
0
1
```

## 09 - Depth-Limited Search

```text
7
S A B
A C D
B E
C
D G
E G
G
S
G
3
```

## 10 - Depth-First Iterative Deepening

```text
7
S A B
A C D
B E
C
D G
E G
G
S
G
10
```

## 11 - Hill Climbing

```text
7
S 5 A B
A 3 C D
B 4 E
C 4
D 1 G
E 2 G
G 0
S
G
```

## 12 - A* Search

```text
7
S 6 A 1 B 4
A 5 C 3 D 1
B 3 E 2
C 4
D 5 G 6
E 1 G 1
G 0
S
G
```

## 13 - Min-Max

```text
3 5 6 9 1 2 0 -1
2
max
```

## 14 - Alpha-Beta Pruning

```text
3 5 6 9 1 2 0 -1
2
max
```

## 15 - Five Fuzzy Operations

```text
0.2 0.5 0.7 1.0
0.6 0.3 0.9 0.4
```

## 16 - Fuzzy Relation Composition

```text
2
0.6 0.3
0.2 0.9
1.0 0.5 0.3
0.8 0.4 0.7
```

## 17 - Weighted Average Defuzzification

```text
2 5 8
0.3 0.8 0.5
```

## 18 - Centroid Defuzzification

```text
1 2 3 4 5 6 7 8
0.1 0.3 0.6 1.0 0.8 0.5 0.4 0.2
```

## 19 - Centre of Sum Defuzzification

```text
1 2 3 4 5 6 7 8
0.2 0.6 1.0 0.6 0.2 0 0 0
0 0 0 0.3 0.7 1.0 0.7 0.3
```

## 20 - Height Defuzzification

```text
1 2 3 4 5 6 7 8
0.2 0.6 1.0 0.6 0.2 0 0 0
0 0 0 0.3 0.7 1.0 0.7 0.3
```

## 21 - Centre of Area Defuzzification

```text
1 2 3 4 5 6 7 8
0.1 0.3 0.6 1.0 0.8 0.5 0.4 0.2
```

## 22 - Winner-Take-All

```text
6
1 1
2 1
1 2
8 8
9 8
8 9
2
2 2
7 7
0.5
0.5
5
```

## 23 - Learning Vector Quantization

```text
6
1 1 0
2 1 0
1 2 0
8 8 1
9 8 1
8 9 1
2
2 2 0
7 7 1
0.5
0.5
5
```

