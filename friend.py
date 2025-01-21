import helpers as h
from timerange import TimeRange
from dataclasses import dataclass, field
#because ClassVar makes the attribute's class scope more explicit
from typing import ClassVar


@dataclass
class Friend:
    #Tracks busy minutes across all friends collectively
    all_busy_minutes_range: ClassVar[list] = []
    name: str
    busy_time_ranges:  list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)
        #Add the minutes range object to a class attribute:
        Friend.all_busy_minutes_range.append(obj.minutes_range)

    #def __repr__(self):
        #return (
            #f"Friend(name='{self.name}', "
            #f"busy_time_ranges={self.busy_time_ranges})"
        #)
