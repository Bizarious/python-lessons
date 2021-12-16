from abc import ABC, abstractmethod


class Event(ABC):
    weight = 0

    def __init__(self, board):
        self._board = board

    @abstractmethod
    def execute(self):
        pass


class TestEvent(Event):
    weight = 1

    def __init__(self, board):
        super().__init__(board)

    def execute(self):
        print("Executing Event")


_all_events = [TestEvent]

events = []

for event in _all_events:
    for _ in range(event.weight):
        events.append(event)
