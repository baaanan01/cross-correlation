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

# with open('products.txt') as f:
#     for line in f:
#         items = line.strip().split(' ')
#         for i in items:
#             stripe = defaultdict(int)
#             for j in items:
#                 if i != j:
#                     stripe[j] += 1

#             print('%s\t%s' % (i, stripe_to_str(stripe)))

d = {}

def mapper():
    with open('products.txt') as f:
        for line in f:
            items = line.strip().split(' ')
            for i in items:
                stripe = defaultdict(int)
                for j in items:
                    if i != j:
                        pair = i + ' ' + j
                        # if pair in d:
                        #     d[pair] +=1
                        # else:
                        #     d[pair] = 1
                        d[pair] = 1
                        stripe[j] += 1

                print('%s\t%s' % (i, stripe_to_str(stripe)))
    print(d)
    # for key, value in d.items():
    #     print(key, ' : ', value)

def reducer():
    # for i in range(len(d)):
    reduced_d = {}
    for (products, value) in d.items():
        if products in d.keys():
            #if the value is already in list, add current value to the sum
            reduced_d[products] += value
        else:
            #if the value is not yet in list, create an entry
            reduced_d[products] = value
    print(1)


def red():      
    resultdict = {}                                                                       
    for key in d:                               
        try:
            resultdict[key] += d[key]        
        except KeyError:                                   
            resultdict[key] = d[key]   
    print(resultdict)

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

mapper()
# reducer()
# red()

# Нужно доделать reducer, чтобы он на вход получал словарь d, в котором на данный момент к каждому ключу идёт значение 1.
# А на выходе из reducer мы должны получить словарь, в котором просуммируются все единички у одинаковых пар.