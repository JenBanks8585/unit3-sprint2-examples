"""This is a mapreduce example"""

from functools import reduce

my_list = [1, 2, 3, 4]

# Traditional way of calculating SSV
ssv_trad = sum([i**2 for i in my_list])

# Mapreduce way of calculating SSV
squared_values = map(lambda i: i**2, my_list)


def add_numbers(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_numbers, squared_values)


print("Sum of Squared Values (trad): {}".format(ssv_trad))
print("Sum of Squared Values (MapReduce): {}".format(ssv_mapreduce))
