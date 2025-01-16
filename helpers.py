def timerange_to_minutes(t_str):
    """
    This will return the amount of minutes for time ranges in format HH:MM
    :param t_str:
    :return:
    """
    hour = int(t_str.split(":")[0])
    minutes = int(t_str.split(":")[1])
    hour_to_minutes = hour * 60

    return hour_to_minutes + minutes






