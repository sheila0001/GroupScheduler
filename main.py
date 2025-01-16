import helpers as h
from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str
    end_time: str

    start_minutes : int = field(init=False, repr=False)
    start_minutes : int = field(init=False, repr=False)

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)



t1 = TimeRange(start_time="00:30", end_time="05:00")
print(t1)