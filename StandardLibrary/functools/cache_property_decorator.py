import functools

class DataSet:
    def __init__(self, sequence_of_numbers) -> None:
        self._data = tuple(sequence_of_numbers)
    
    @functools.cached_property
    def stdev(self):
        return statistics.stddev(self._data)
