

def timerange_to_minutes(t_str):

def minutes_to_timerange_str(m):

    """
    Return a timerange string in format of HH:MM for the given integer 
    : param m:
    :return:
    m = 90 -> 01:30
    """
    hour = m // 60
    hour_str= f"{hour:02d}" #format string will ouput number with 2 digits
    minutes = m % 60
    minutes_str= f"{minutes:02d}" 

    return (f"{hour_str}:{minutes_str}")


def prettify_available_minutes(): ...

print(minutes_to_timerange_str(m=65))

