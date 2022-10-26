from curses import keyname
import random;
from math import ceil
import sys
from collections import defaultdict

def stripe_to_str(dct):
    result = []
    for element in dct.keys():
        result.append(element + ':' + str(dct[element]))
    return ','.join(result)

items_file = open('products.txt', 'r')

def mapper():
    with open('map.txt', 'w') as f:
        f.write('')
    with open('products.txt') as f:
        for line in f:
            items = line.strip().split(' ')
            for i in items:
                d = {}
                for j in items:
                    if i != j:
                        pair = i + ' ' + j
                        d[pair] = 1
                with open('map.txt', 'a') as f:
                    for key, value in d.items():
                        new_str = key + ' : ' + str(value) + '\n'
                        f.write(new_str)
                # print('%s\t%s' % (i, stripe_to_str(stripe)))
    # print(d)
    # for key, value in d.items():
    #     print(key, ' : ', value)

def reducer():
    d = {}
    with open('map.txt') as f:
        for line in f:
            products = line.split(' : ')[0]
            value = int(line.split(' : ')[1][0:1])
            if products in d.keys():
                d[products] += value
            else:
                d[products] = value
    with open('reduce.txt', 'w') as f:
        for key, value in d.items():
            new_str = key + ' : ' + str(value) + '\n'
            f.write(new_str)
    # for (products, value) in d.items():
    #     if products in d.keys():
    #         #if the value is already in list, add current value to the sum
    #         reduced_d[products] += value
    #     else:
    #         #if the value is not yet in list, create an entry
    #         reduced_d[products] = value
    # print(1)



# with open('products.txt') as f:
#     for line in f:
#         items = line.strip().split(' ')
#         for i in items:
#             stripe = defaultdict(int)
#             for j in items:
#                 if i != j:
#                     stripe[j] += 1

#             print('%s\t%s' % (i, stripe_to_str(stripe)))

# for keys, values in d.items():
#     keys_test = keys.split(' ')[1]+ ' ' + keys.split(' ')[0]
#     # print(keys_test)
#     if values>1:
#         print(keys,values)
#         print(keys_test)

# mapper()
reducer()


# Нужно доделать reducer, чтобы он на вход получал словарь d, в котором на данный момент к каждому ключу идёт значение 1. А на выходе из reducer мы должны получить словарь, в котором просуммируются все единички у одинаковых пар.