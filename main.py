"""
Main entry point for running the assignment.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import gc
gc.collect()

from data_loader import load_market_data
from strategies import (
    NaiveMovingAverageStrategy,
    WindowedMovingAverageStrategy,
    OptimizedNaiveMovingAverageStrategy
)
from profiler import profile_runtime, profile_memory
from reporting import plot_runtime, plot_memory, results_table 


def main():
    data = load_market_data("data/market_data.csv")
    #print(data[:5])  # Print first 5 data points as a sample

    strategies = {
        "Naive": NaiveMovingAverageStrategy(),
        "Windowed": WindowedMovingAverageStrategy(window_size=10),
        "RefactoredNaive" : OptimizedNaiveMovingAverageStrategy()
    }

    input_sizes = [1000, 10_000, 100_000]
    results = {}

    for name, strategy in strategies.items():
        results[name] = {
            "sizes": [],
            "runtimes": [],
            "memory": [],
        }

        for size in input_sizes:
            subset = data[:size]
            results[name]["sizes"].append(size)
            results[name]["runtimes"].append(
                profile_runtime(strategy, subset)
            )
            results[name]["memory"].append(
                profile_memory(strategy, subset)
            )

    plot_runtime(results)
    plot_memory(results)
    results_table(results)

if __name__ == "__main__":
    main()
