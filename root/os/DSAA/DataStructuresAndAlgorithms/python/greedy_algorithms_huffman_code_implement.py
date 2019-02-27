#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# greedy_algorithms_huffman_code_implement.py
# python
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
# Created by Chyi Yaqing on 02/27/19 13:07.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
In computer science and information theory, a Huffman code is a particular type
of optimal prefix code that is commonly used for lossless data compression. The
process of finding and/or using such a code proceeds by means of Huffman codein
an algorithm developed by David A.Huffman while he was a Sc.D.student at MID,
and published in the 1952 paper "A Method for the Construction of
Minimum-Redundancy Codes"

Huffman coding is a lossless data compression algorithms. The idea is to assign
variable-length codes to input characters, lengths of the assigned codes are
based on the frequencies of corresponding characters. The most frequent
character gets the smallest code and the least frequent character gets the
largest code.

There are mainly two major parts in Huffman Coding
    1) Build a Huffman Tree from input characters
    2) Traverse the Huffman Tree and assign codes to characters

Build Huffman Tree:
    Input is array of unique characters along with their frequency of
    occurrences and out-put is Huffman Tree.
    1) Create a leaf node for each unique chracter and build a min heap of all
    leaf nodes

    2) Extract two nodes with the minimum frequency from the min heap

    3) Create a new internal node with frequency euqal to the sum of the two
    nodes frequencies. Make the first extracted node as its left child and the
    other extracted node as its right child. Add this node to the min heap.

    4) Repeat steps#2 and #3 until the heap contains only one node. The remain
    node is the root node and the tree is complete.

http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

"""
import heapq
import os


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __cmp__(self, other):
        if (other is None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq


class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # Functions for compression:

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if (root is None):
            return
        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encodde_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            os.exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self):
    filename, file_extension = os.path.splitext(self.path)
    output_path = filename + ".bin"

    with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
        text = file.read()
        text = text.rstrip()
        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        encoded_text = self.get_encoded_text(text)
        padded_encoded_text = self.pad_encoded_text(encoded_text)

        b = self.get_byte_array(padded_encoded_text)
        output.write(bytes(b))
    print("Compressed")
    return output_path

