import events


class HidingEvent(events.EmptyEvent):
    weight = 1
    symbol = "H"

    def execute(self):
        pass

    def message(self):
        print("All Fields are hidden\n")


events.all_events.append(HidingEvent)
