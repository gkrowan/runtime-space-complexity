import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import io
import pstats
from datetime import datetime

from models import MarketDataPoint
from strategies import NaiveMovingAverageStrategy
from profiler import profile_cpu


def test_naive_strategy_has_sum_hotspot():
    strategy = NaiveMovingAverageStrategy()

    data = [
        MarketDataPoint(
            timestamp=datetime.now(),
            symbol="AAPL",
            price=float(i),
        )
        for i in range(1000)
    ]

    stats = profile_cpu(strategy, data)

    stream = io.StringIO()
    stats.stream = stream
    stats.print_stats()

    output = stream.getvalue()

    assert "generate_signals" in output
    assert "sum" in output
