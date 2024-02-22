class Score:

    def __init__(self, start=2000) -> None:
        self._score = start

    def subtract_point(self, amount=50) -> None:
        self._score -= amount

    @property
    def score(self) -> int:
        return self._score
