"""
Strategy implementations and complexity annotations.
"""

from collections import deque
from typing import List

from models import Strategy, MarketDataPoint


class NaiveMovingAverageStrategy(Strategy):
    """
    Naive moving average strategy.

    Time Complexity:
        - Per tick: O(n)
        - Total: O(n^2)

    Space Complexity:
        - O(n) (stores full price history)
    """

    def __init__(self):
        self.prices = []

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        # O(1): append price
        self.prices.append(tick.price)

        # O(n): recompute average from scratch
        avg_price = sum(self.prices) / len(self.prices)

        if tick.price > avg_price:
            return ["BUY"]
        else:
            return ["SELL"]


class WindowedMovingAverageStrategy(Strategy):
    """
    Optimized moving average strategy using a fixed window.

    Time Complexity:
        - Per tick: O(1)

    Space Complexity:
        - O(k), where k is window size
    """

    def __init__(self, window_size: int = 10):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        # O(1): remove oldest element if window is full
        if len(self.window) == self.window_size:
            self.running_sum -= self.window[0]

        # O(1): append new price
        self.window.append(tick.price)
        self.running_sum += tick.price

        avg_price = self.running_sum / len(self.window)

        if tick.price > avg_price:
            return ["BUY"]
        else:
            return ["SELL"]

class OptimizedNaiveMovingAverageStrategy(Strategy):
    """
    Refactored Naive moving average strategy using running sum 
        - attempting to pass 1 sec time test while keeping full price history

    Time Complexity:
        - Per tick: O(1)

    Space Complexity:
        - O(n) (stores full price history)
    """

    def __init__(self):
        self.prices = []
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        # O(1): append price
        self.prices.append(tick.price)
        self.running_sum += tick.price

        # O(1): recompute average with the running sum, avoid repeating operations
        #avg_price = sum(self.running_sum / len(self.prices))

        avg_price = self.running_sum / len(self.prices)
        
        if tick.price > avg_price:
            return ["BUY"]
        else:
            return ["SELL"]
        