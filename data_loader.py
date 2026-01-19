"""
CSV ingestion and MarketDataPoint creation.
"""

import csv
from datetime import datetime
from typing import List

from models import MarketDataPoint


def load_market_data(path: str) -> List[MarketDataPoint]:
    """
    Load market data from CSV.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    data = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamp = datetime.fromisoformat(row["timestamp"])
            symbol = row["symbol"]
            price = float(row["price"])

            data.append(
                MarketDataPoint(
                    timestamp=timestamp,
                    symbol=symbol,
                    price=price,
                )
            )

    return data
