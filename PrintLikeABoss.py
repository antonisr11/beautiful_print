def print_like_a_boss(*elements,left_side=True,title=True,show_count=True):

    max_length=-1
    for element in elements:
        if len(element)>max_length:
            max_length=len(element)

    if show_count:
        count=tuple()
        if title:
            count = count + ("Num",)
        for i in range(0,max_length):
            temp_number=str(i+1)
            for j in range(0, len(str(len(elements))) - len(str(i))):
                temp_number= "0" + temp_number
            count = count + (temp_number,)
        elements = (count,) + elements

    max_list=list()
    for element in elements:
        temp_max=-1
        for sub_element in element:
            if len(str(sub_element))>temp_max:
                temp_max=len(str(sub_element))
        max_list.append(temp_max+1)

    for i in range(0,max_length):
        x=-1
        print("|", end="")
        for element in elements:
            x+=1
            if left_side:
                try:
                    print(element[i],end="")
                    for j in range(0, max_list[x] - len(str(element[i]))):
                        print(" ", end="")
                except IndexError:
                    for j in range(0, max_list[x]):
                        print(" ", end="")
                print("|",end="")
            else:
                try:
                    test=element[i]
                    for j in range(0, max_list[x] - len(str(element[i]))):
                        print(" ", end="")
                    print(test,end="")
                except IndexError:
                    for j in range(0, max_list[x]):
                        print(" ", end="")
                print("|",end="")
        print("")
        if i==0 and title:
            print("|", end="")
            for j in range(0,len(max_list)):
                for k in range(0,max_list[j]):
                    print("-",end="")
                print("|",end="")
            print("")
    return
