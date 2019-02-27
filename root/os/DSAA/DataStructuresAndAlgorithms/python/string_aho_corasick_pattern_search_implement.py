#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_aho_corasick_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/27/19 12:15.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Aho-Corasick Algorithm for Pattern Searching:

"""
class AhoNode:
    # Trie node class
    def __init__(self):
        # 字符集只包含a~z 26个字符
        self.children = [None]*26
        # isEndOdWord is True if node represent the end of the word
        self.isEndOfWord = False  # 结尾字符
        # 失败指针
        self.fail = None


# Trie树是一种非常独特的、高效的字符串匹配算法
class Aho_Corasick:
    # Trie data structure class
    def __init__(self):
        # 存储无意义字符
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return AhoNode()

    def _charToIndex(self, ch):
        # Private helper function Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, inserts key into trie If the key is prefix of trie
        # node, just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # Mark last node as leaf
        pCrawl.isEndOfWord = True

    # Returns true if root has no children, else False
    def isEmpty(self, root):
        for i in range(26):
            if root.children[i]:
                return False
        return True

    # Recursive function to delete a key from given Trie
    def delete(self, root, key, depth=0):
        # If tree is empty
        if (self.isEmpty(root)):
            return
        # If last character of key is being processed
        if depth == len(key):
            # This node is no more end of word after removal of given key
            if root.isEndOfWord:
                root.isEndOfWord = False
            # If given is not prefix of any other word
            if self.isEmpty(root):
                del root
                root = None
            return root
        # if not last character, recur for the child obtained using ASCII value
        index = self._charToIndex(key[depth])
        root.children[index] = self.delete(root.children[index], key, depth+1)

        # If root does not have any child (its only child got deleted), and
        # it is not end of another word.
        if (self.isEmpty(root) and root.isEndOfWord is False):
            del root
            root = None
        return root

    def search(self, key):
        # Search key in the trie Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl is not None and pCrawl.isEndOfWord
