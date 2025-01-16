#import helpers as h
from timerange import TimeRange
from dataclasses import dataclass, field


@dataclass
class Friend:
    name: str
    busy_time_ranges:  list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)

    def __repr__(self):
        return (
            f"Friend(name='{self.name}', "
            f"busy_time_ranges={self.busy_time_ranges})"
        )