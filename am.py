def my_function(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return my_function([x for x in lst[1:]])
