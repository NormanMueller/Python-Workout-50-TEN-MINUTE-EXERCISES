import collections


def sum_everything (*args):
    types = [type(i) for i in args ]
    types_count = collections.Counter(types) 
    output = args[0]
    if len(types_count) ==1 and args is not None:
        for element in args[1:]: 
            output += element
    return output
    



sum_everything('a','a')
sum_everything([21,2], [1,343])
