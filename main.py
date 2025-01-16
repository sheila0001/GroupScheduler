from timerange import TimeRange
import helpers as h
from friend import Friend


def main():
    available_minutes = list(range(1440))
    f1 = Friend("Jane")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00"))  # 480 to 600
    f2 = Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))  # 720 to 840

    # Filter out unavailable minutes
    busy_minutes = set()
    for r in Friend.all_busy_minutes_range:
        busy_minutes.update(r)  # Add all busy minutes from the range

    # Create a new list of available minutes by excluding busy minutes
    available_minutes = [m for m in available_minutes if m not in busy_minutes]
    print(available_minutes)


if __name__ == "__main__":
    main()




    







#if __name__ == "__main":
    #main()