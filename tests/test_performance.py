import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import time
import gc
import pytest
from datetime import datetime

from models import MarketDataPoint
from strategies import WindowedMovingAverageStrategy, OptimizedNaiveMovingAverageStrategy
from memory_profiler import memory_usage


def test_windowed_strategy_performance():
    strategy = WindowedMovingAverageStrategy(window_size=10)

    data = [
        MarketDataPoint(
            timestamp=datetime.now(),
            symbol="AAPL",
            price=float(i % 100),
        )
        for i in range(100_000)
    ]

    gc.collect()

    start = time.perf_counter()

    mem_peak = memory_usage(
        (lambda: [strategy.generate_signals(t) for t in data],),
        max_usage=True
    )

    elapsed = time.perf_counter() - start

    
    assert mem_peak < 100.0, f"Memory too high: {mem_peak:.2f}MB"
    assert elapsed < 1.0, f"Runtime too slow: {elapsed:.2f}s"


def test_optimized_naive_strategy_performance():
    strategy = OptimizedNaiveMovingAverageStrategy()

    data = [
        MarketDataPoint(
            timestamp=datetime.now(),
            symbol="AAPL",
            price=float(i % 100),
        )
        for i in range(100_000)
    ]

    gc.collect()

    start = time.perf_counter()

    mem_peak = memory_usage(
        (lambda: [strategy.generate_signals(t) for t in data],),
        max_usage=True
    )

    elapsed = time.perf_counter() - start

    
    assert mem_peak < 100.0, f"Memory too high: {mem_peak:.2f}MB"
    assert elapsed < 1.0, f"Runtime too slow: {elapsed:.2f}s"