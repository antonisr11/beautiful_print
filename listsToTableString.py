def listsToTableString(*lists, left_side=True,titles= list() or tuple(), show_count=False):

    final_string=""

    # # Convert titles to list
    # titles=list(titles)

    max_length_inside_lists = list() # How big will this list's line be
    max_length_of_lists=-1 # How many lines the table will have

    for element in lists:
        if len(element)>max_length_of_lists:
            max_length_of_lists=len(element)

        temp_max=-1
        if not len(titles)==0:
            # When we have titles we should count them as length inside lists
            # We add 1 in titles because in 0 position there is names' list
            temp_max = len(titles[lists.index(element)+1])
        for sub_element in element:
            if len(str(sub_element)) > temp_max:
                temp_max = len(str(sub_element))
        max_length_inside_lists.append(temp_max + 1)

    # Choice: Do you want to show count?
    if show_count:
        # Appending to lists a new list with numbers
        count=tuple()
        for current_line_number in range(0,max_length_of_lists):
            temp_number=str(current_line_number+1)
            for j in range(0, len(str(max_length_of_lists)) - len(str(current_line_number+1))):
                temp_number= "0" + temp_number
            count = count + (temp_number,)
        # Make 1st list the numbers we want to count
        lists = (count,) + lists
        
        try:
            # Append in max_length_inside_list at 1st position
            # the max length of all numbers which is (the length of last element) or (title)
            if len(count[-1])<len(titles[0]):
                max_length_inside_lists.insert(0,len(titles[0]) + 1)
            else:
                raise IndexError
        except IndexError:
            max_length_inside_lists.insert(0, len(count[-1]) + 1)

    # Check if number of titles is right. Checking after appending count numbers in lists
    if (not len(titles) == len(lists)) and not len(titles) == 0:
        if show_count:
            raise ValueError("(1/3) Number of titles does not match with number of appended lists.\nValueError: (2/3) Don't forget to add title for number's count.\nValueError: (3/3) Expect "+str(len(lists))+", got "+str(len(titles)))
        else:
            raise ValueError("(1/2) Number of titles does not match with number of appended lists.\nValueError: (2/2) Expect "+str(len(lists))+", got "+str(len(titles)))

    # Choice: Show titles?
    if len(titles)>0:

        for title_i in range(0,len(titles)):
            final_string += "|" + str(titles[title_i]) + " " * int(max_length_inside_lists[title_i]-len(str(titles[title_i])))
        final_string += "|\n"

        for max_length_inside_current_list in max_length_inside_lists:
            final_string+= "|" + "-" * int(max_length_inside_current_list)
        final_string += "|\n"


    # Create string body
    for current_line_number in range(0,max_length_of_lists):
        final_string+="|" # Always start with |

        for list_i in range(0,len(lists)):
            try:
                if left_side:
                    final_string += \
                        str((lists[list_i])[current_line_number]) +\
                        " " * int(max_length_inside_lists[list_i] - len(str((lists[list_i])[current_line_number])))
                else:
                    final_string +=\
                        " " * int(max_length_inside_lists[list_i] - len(str((lists[list_i])[current_line_number])))\
                        + str((lists[list_i])[current_line_number])
            except IndexError:
                # This list has reach to an end so we set this block empty
                final_string+=" " * max_length_inside_lists[list_i]
            final_string+="|"
        final_string+="\n"
    return final_string
