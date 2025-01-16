from timerange import TimeRange
from friend import Friend

def main():
    f1 = Friend("Jane")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00")) # from 480 until 600 min, Jane is not available
    f2=Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))

    for i in range(1440):
        print(i)






if __name__ == "__main":