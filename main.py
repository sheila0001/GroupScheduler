from timerange import TimeRange
import helpers as h
from friend import Friend


def main():
    available_minutes = list(range(1440))
    f1 = Friend("Jane")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00")) # from 480 until 600 min, Jane is not available
    #f2=Friend("Chris")
    #f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))

    for m in available_minutes[:] :
        if m in f1.busy_time_ranges[0].minutes_range:
            available_minutes.remove(m)

  

if __name__ == "__main__":
    main()




    







#if __name__ == "__main":
    #main()