from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str
    end_time: str

    start_minutes : int = field(init=False)
    start_minutes : int = field(init=False)




t1 = TimeRange(start_time="00:30", end_time="05:00")
print(t1)