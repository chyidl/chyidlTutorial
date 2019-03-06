#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# start.py
# Python3_Metaprogramming
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
# Created by Chyi Yaqing on 03/05/19 22:52.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT


class Structure:
    _fields = []

    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    # def __init__(self, name, shares, price):
    #   self.name = name
    #    self.shares = shares
    #    self.price = price


class Point(Structure):
    _fields = ['x', 'y']

    # def __init__(self, x, y):
    #    self.x = x
    #    self.y = y


class Address(Structure):
    _fields = ['hostname', 'port']

    # def __init__(self, hostname, port):
    #    self.hostname = hostname
    #    self.port = port
