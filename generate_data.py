"""
Generate simulated market data
"""

import csv
import random
from datetime import datetime, timedelta


def generate_market_data(
    output_path="market_data.csv",
    n_ticks=100_000,
    symbols=("AAPL",),
    start_price=150.0,
    start_time=datetime(2024, 1, 1, 9, 30),
    delta_seconds=1,
    volatility=0.1,
    seed=347,
):
    random.seed(seed)

    current_time = start_time
    prices = {symbol: start_price for symbol in symbols}

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "symbol", "price"])

        for i in range(n_ticks):
            symbol = symbols[i % len(symbols)]

            # Random walk price update
            price_change = random.gauss(0, volatility)
            prices[symbol] = max(1.0, prices[symbol] + price_change)

            writer.writerow([
                current_time.isoformat(),
                symbol,
                round(prices[symbol], 2),
            ])

            current_time += timedelta(seconds=delta_seconds)


if __name__ == "__main__":
    generate_market_data()
