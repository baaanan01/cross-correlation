import random;
from math import ceil
import sys
from collections import defaultdict

items = ["carrot", "apple", 'cucumber', 'onion', 'salad', 'tomato', 'potato', 'strawberry', 'melon', 'potato', 'banana', 'avocado', 'grape', 'cherry', 'blueberry', 'peach', 'lemon', 'mango', 'garlic', 'corn', 'coconut', 'pineapple', 'pepper', 'pear', 'olive', 'qiwi', 'cabbage', 'cheese', 'egg', 'beef', 'chicken', 'bread', 'milk', 'bacon', 'pancakes', 'tea', 'cookie', 'peanut', 'cola', 'pepsi', 'water', 'butter', 'cake']

with open('products.txt', 'w') as f:
    f.write('')

for i in range (0,10):
    with open('products.txt', 'a') as f:
        f.write(' '.join(random.sample(items, ceil(random.random()*4+2))) + '\n')

