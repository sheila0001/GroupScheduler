from timerange import TimeRange
import helpers as h
from friend import Friend
from custom_list import CustomList


def main():
    # starts with all minutes in a day (0–1439)
    available_minutes = CustomList(range(1440)) #removes the busy minutes to find the free minutes.
    f1 = Friend("Jane")
    f1.add_busy_range(TimeRange(start_time="08:00", end_time="10:00"))  # 480 to 600
    f2 = Friend("Chris")
    f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))  # 720 to 840

    # Filter out unavailable minutes
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    print(available_minutes)   


if __name__ == "__main__":
    main()




    







#if __name__ == "__main":
    #main()