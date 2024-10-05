from abc import ABC, abstractmethod


class Collector(ABC):
    """Aggregate codebench metrics."""

    def __init__(self, csv_source: str):
        self.csv_source = csv_source

    @abstractmethod
    def collect(self):
        pass
