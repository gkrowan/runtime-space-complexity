"""
Core domain models and strategy interface.
"""

from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable market data tick.

    Space Complexity: O(1) per instance
    """
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    """

    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        """
        Generate trading signals for a single tick.
        """
        pass
