#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_trie_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/27/19 10:33.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
In computer science, a trie, also called digital tree, radix tree or prefix
tree, is a kind of search tree - an ordered tree data structure used to store a
dynamic set or associative array where the keys are usually strings.

Trie | (Delete)
During delete operation we delete the key in bottom up manner using recursion.
The following are possible conditions when deleting key from trie.
    1) Key may not be there in trie. Delete operation should not modify trie
    2) Key present as unique key(no part of key contains another key (prefix),
    not the key itself is prefix of another key in trie). Delete all the nodes.
    3) Key is prefix key of another long key in trie. Unmark the leaf node.
    4) Key present in trie, having atlest one other key as prefix key. Delete
    nodes from end of key until first leaf node of longest prefix key.
"""
# Python program for insert and search operation in a Trie


class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOdWord is True if node represent the end of the word
        self.isEndOfWord = False


# Trie树是一种非常独特的、高效的字符串匹配算法
class Trie:
    # Trie data structure class
    def __init__(self):
        # 存储无意义字符
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

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


# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    t.delete(t.root, "the")
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
