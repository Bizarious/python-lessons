class EmptyEvent:
    weight = 0
    symbol = " "

    def __init__(self, board):
        self._board = board

    def execute(self):
        pass

    def message(self):
        pass


class TestEvent(EmptyEvent):
    weight = 1
    symbol = "?"

    def __init__(self, board):
        super().__init__(board)

    def execute(self):
        pass

    def message(self):
        print("Executing EmptyEvent")


_all_events = [TestEvent]

events = []

for event in _all_events:
    for _ in range(event.weight):
        events.append(event)
