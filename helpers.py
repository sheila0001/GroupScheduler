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

#this function organizes the numbers in list minutes into smaller and grouped lists
def prettify_available_minutes():
    l = [0, 1, 2, 60, 61, 62]
    grouped_list = [] #store the final groups of consecutive numbers
    list_resettable =[] # hold the current group of consecutive numbers
    #Group the list so that:[[0,1,2], [60, 61, 62]]

    for element in l:
        if list_resettable == []:
            list_resettable.append(element)
            continue
        if list_resettable[-1] + 1 == element:
            list_resettable.append(element)
        
        else:
            grouped_list.append(list_resettable[:]) # # Add the current group to grouped_list.
            list_resettable.clear() # Clear the temporary list to start a new group.
            list_resettable.append(element) #Add the current number to the new group.

    #add the rest of the smalled lists in grouped_list
    grouped_list.append(list_resettable)
    print(grouped_list)

prettify_available_minutes()











