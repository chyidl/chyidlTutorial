#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.18.Mapping_Names_to_Sequence_Elements.py
# ch01
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 01/30/19 21:23.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
# collections.namedtuple() is actually a factory method that returns
# a subclass of the standard Python tuple type.
# namedtuple is immutable
from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print('sub.addr : {}'.format(sub.addr))
print('sub.joined : {}'.format(sub.joined))
# namedtuple looks like a normal class instance, it is inter-changeable with a
# tuple and supports all of usual tuple operations
print("len(sub) : {}".format(len(sub)))
addr, joined = sub
print("addr : {}".format(addr))
print("joined : {}".format(joined))

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# namedtuple is immutable
s = Stock('ACME', 100, 123.45)
print(s)
# change any of the attributes, it can be done using the _replace() method
s = s._replace(shares=75)
print(s)

# _replace() method is that it can be a convenient way to populate named
# make a prototype tuple containing the default values and the use _replace
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
