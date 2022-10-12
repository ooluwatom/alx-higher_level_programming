#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    final_list = []
    try:
        i,j = 0,0
        new_list.append(my_list_1[i]/my_list_2[j])
    except TypeError:
        print('wrong type')
        new_list.append(0)
    except ValueError:
        print('division by 0')
        new_list.append(0)
    except IndexError:
        print('out of range')
    finally:
        if list_length == 0:
            return final_list.append(new_list[0])
        if list_length > 0:
            return final_list.append(new_list[0:(list_length + 1)])
