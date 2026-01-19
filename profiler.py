"""
Runtime and memory profiling utilities.
"""

import timeit
import cProfile
import pstats
from memory_profiler import memory_usage


def run_strategy(strategy, data):
    for tick in data:
        strategy.generate_signals(tick)


def profile_runtime(strategy, data):
    """
    Measure execution time using timeit.
    """
    return timeit.timeit(
        lambda: run_strategy(strategy, data),
        number=1
    )


def profile_memory(strategy, data):
    """
    Measure peak memory usage.
    """
    mem_usage = memory_usage(
        (run_strategy, (strategy, data)),
        interval=0.1,
        max_usage=True
    )
    return mem_usage


def profile_cpu(strategy, data):
    """
    Collect cProfile statistics.
    """
    profiler = cProfile.Profile()
    profiler.enable()
    run_strategy(strategy, data)
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    return stats
