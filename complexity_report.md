# Runtime & Space Complexity in Financial Signal Processing

## Complexity Report

Generate complexity_report.md with:
- Tables of runtime and memory metrics
- Complexity annotations
- Plots of scaling behavior
- Narrative comparing strategies and optimization impact


### Naive Moving Average Strategy:

| Operation    | Complexity |
| ------------ | ---------- |
| Time per tick| O(n)       |
| Total        | O(n^2)     |
| Memory       | O(n)       |

The naive moving average strategy recalculates the average for each additional tick by summing all previous prices, leading to linear time complexity per tick and quadratic total time complexity as the number of ticks increases. The memory complxity is linear because the full price history is stored. 

### Windowed Moving Average Strategy: 

| Operation     | Complexity |
| ------------- | ---------- |
| Time per tick | O(1)       |
| Memory        | O(k)       |

The windowed moving average strategy uses a fixed window size to maintain a running sum of the last k prices, where k is the window size. This allows for constant time complexity per tick since as the new price is added, the oldest price is removed from the sum. The memory complexity is O(k) as only the last k prices are stored in memory.

### Runtime and Memory Metrics

| Strategy | Ticks | Runtime (s) | Peak Memory (MB) |
| -------- | ----- | ----------- | ---------------- |
| Naive | 1000 | 0.003493 | 105.92 |
| Naive | 10000 | 0.536581 | 105.94 |
| Naive | 100000 | 44.006688 | 43.99 |
| Windowed | 1000 | 0.001011 | 43.73 |
| Windowed | 10000 | 0.009108 | 43.37 |
| Windowed | 100000 | 0.092764 | 49.98 |

### Scaling Behavior Plots

![Runtime Scaling](runtime_scaling.png)

![Memory Scaling](memory_scaling.png)


### Narrative Comparison

The Naive Moving Average strategy exhibits quadratic time complexity due to the need to sum all prices for each tick, leading to significant slowdowns as data size increases. In contrast, the Windowed Moving Average strategy maintains constant time complexity per tick by only updating the sum with the new price and removing the oldest price, resulting in much better performance for large datasets.

As the number of ticks approaches 100,000, the two strategies exhibit some unexpected memory behavior: the naive strategy actually has a lower peak memory usage than the windowed method. This was confusing to me at first, but I attribute it to the non-deterministic way that python's memory allocater works and the sampling-based method used by the memory profiler. Also, I found that run-to-run differences stabilize when I force garbage collection before calling main.py and running the entire process again. 

### Test Results: 

Test 1: Performance
- PASSED: memory usage is  <100MB memory for 100k ticks
- FAILED: Naive strategy does not run under 1 s
    - After refactoring Naive: 

Test 2: Profiling 
- PASSED: Expected hotspots and memory peaks

Test 3: Strategies
- PASSED: Naive and Windowed strategies compute the same trading recommendation.
