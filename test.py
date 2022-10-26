from curses import keyname
import random;
from math import ceil
import sys
from collections import defaultdict

d={}

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

                # print('%s\t%s' % (i, stripe_to_str(stripe)))
print(d)