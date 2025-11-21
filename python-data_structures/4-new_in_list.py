#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list.copy()

    # If index is invalid, return the copy unchanged
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Replace the element in the copy (not the original)
    new_list[idx] = element
    return new_list
