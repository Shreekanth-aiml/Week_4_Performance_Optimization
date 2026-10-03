# Week 4 - Performance Optimization in Python

## Project Overview

This project focuses on improving the performance of a Python application by identifying a performance bottleneck, applying an optimization technique, and comparing the execution time before and after optimization.

The application finds duplicate numbers in a list.

## Original Application

The original version uses nested loops to compare elements in the list. This approach requires a large number of comparisons when the input size increases.

File:

`original_app.py`

## Performance Analysis

Python's built-in `cProfile` tool was used to analyze the original application and identify the time-consuming parts of the program.

The profiling result is stored in:

`profiling_original.txt`

## Optimization

The optimized version uses Python's `set` data structure.

A set allows efficient checking of whether a number has already been encountered. This eliminates the need for the expensive nested-loop comparison used in the original version.

File:

`optimized_app.py`

## Benchmarking

The `benchmark.py` file measures the execution time of both the original and optimized versions.

The performance results are stored in:

`performance_results.txt`

## Testing

Automated tests were created using Python's `unittest` framework.

The tests verify that the original and optimized versions produce the same results.

Run the tests using:

```bash
python -m unittest test_app.py
```
