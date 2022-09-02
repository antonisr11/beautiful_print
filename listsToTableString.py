#test12

def listsToTableString(*lists, left_side=True,titles= list() or tuple(), show_count=False):

    final_string=""
    has_title=True
    if len(titles)==0:
        has_title=False

    # Check if number of titles is right.
    # Right: Show titles and don't show count, so length of titles must be equal to length of lists
    # Right: Show titles and show count, so length of titles must be equal to length of lists - 1 because show count list is not yet appended

    if (has_title and not show_count and not len(titles) == len(lists)) or (has_title and show_count and not (len(titles) == len(lists)-1)) :
        if show_count:
            raise ValueError(
                "(1/3) Number of titles does not match with number of appended lists.\nValueError: (2/3) Don't forget to add title for number's count.\nValueError: (3/3) Expect " + str(
                    len(lists)) + ", got " + str(len(titles)))
        else:
            raise ValueError(
                "(1/2) Number of titles does not match with number of appended lists.\nValueError: (2/2) Expect " + str(
                    len(lists)) + ", got " + str(len(titles)))


    max_length_inside_lists = list() # How big will this list's line be
    max_length_of_lists=-1 # How many lines the table will have

    for element in lists:
        if len(element)>max_length_of_lists:
            max_length_of_lists=len(element)

        temp_max=-1
        if has_title:
            # When we have titles we should count them as length inside lists

            if show_count:
                # We add 1 in titles because in 0 position there is names' list
                temp_max = len(titles[lists.index(element)+1])
            else:
                temp_max = len(titles[lists.index(element)])
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

    # Choice: Show titles?
    if has_title:

        for title_i in range(0,len(titles)):
            if left_side:
                final_string += "|" + str(titles[title_i]) + " " * int(max_length_inside_lists[title_i]-len(str(titles[title_i])))
            else:
                final_string += "|" + " " * int(max_length_inside_lists[title_i]-len(str(titles[title_i]))) + str(titles[title_i])

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
