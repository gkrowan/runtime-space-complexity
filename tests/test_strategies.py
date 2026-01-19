import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from datetime import datetime, timedelta

from models import MarketDataPoint
from strategies import (
    NaiveMovingAverageStrategy,
    WindowedMovingAverageStrategy,
)


def make_ticks(prices):
    start = datetime(2024, 1, 1, 9, 30)
    return [
        MarketDataPoint(
            timestamp=start + timedelta(seconds=i),
            symbol="AAPL",
            price=p,
        )
        for i, p in enumerate(prices)
    ]


def test_strategies_produce_same_signals():
    prices = [100, 101, 102, 101, 100, 99, 100]
    ticks = make_ticks(prices)

    naive = NaiveMovingAverageStrategy()
    windowed = WindowedMovingAverageStrategy(window_size=len(prices))

    naive_signals = []
    windowed_signals = []

    for tick in ticks:
        naive_signals.append(naive.generate_signals(tick))
        windowed_signals.append(windowed.generate_signals(tick))

    assert naive_signals == windowed_signals
