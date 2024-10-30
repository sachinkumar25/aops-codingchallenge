# AoPS Coding Challenge - Pyramid Descent

Hey! This is my solution for the Art of Problem Solving (AoPS) programming challenge. The challenge involves finding a path down a pyramid of numbers where multiplying the numbers along the path gives us a target value.

## The Problem
Given a pyramid of numbers and a target value, we need to find a path from top to bottom that when multiplied together equals the target. We can only move down-left (L) or down-right (R) at each step.

Example:
```
   1
  2 3
 4 1 1
```
Target = 2
Solution = "LR" (1 → 2 → 1)

## How to Run
1. Clone this repo
2. Make sure your input is in `pyramid_sample_input.txt`
3. Run the solver:
```bash
python puzzle_solver.py
```

## Input Format
Your input file should look like this:
```
Target: 720
2
4,3
3,2,6
2,9,5,2
10,5,2,15,5
```

## Sample Output
```
Found it! Path: LLRR
```

## My Approach
I used recursion to try all possible paths and added some optimizations:
- Stop when product exceeds target (if all remaining numbers are positive)
- Built path strings as we go
- Simple error handling for file reading
