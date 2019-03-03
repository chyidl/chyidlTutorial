#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# stack_browser_back_forward_button_implement.py
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
# Created by Chyi Yaqing on 03/03/19 09:52.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Using to implement the back and forward button of a browser

Use Two Stacks for the forward and back. Since all you have a remember is the
last thing page you came from and the last page you came back from. One stack
will be for "undoing", i.e. Going backward to the page you were just at, and
one would be for "redoing"I.e.Going forward.
"""


class Stack:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if self.size < self.capacity:
            self.items.append(item)
        else:
            raise IndexError("This stack is full, out of capacity")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("This stack is Empty, out of capacity")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return False if len(self.items) > 0 else True

    @property
    def size(self):
        return len(self.items)


class Browser:
    def __init__(self, url=None):
        self.current_url = url
        self.backward_stack = Stack()
        self.forward_stack = Stack()

    def backward_button(self):
        if not self.backward_stack.isEmpty():
            self.forward_stack.push(self.current_url)
            print("Current url :{}".format(self.current_url))
            self.current_url = self.backward_stack.pop()
            print("Will back to the old url: {}".format(self.current_url))
        else:
            raise ("This is the last url, couldn't backforward")

    def forward_button(self, new_url):
        print("Current url :{}".format(self.current_url))
        self.backward_stack.push(self.current_url)
        print("Will go to the new url: {}".format(new_url))
        self.current_url = new_url


if __name__ == '__main__':
    chrome = Browser(url="https://google.com")
    chrome.forward_button("https://twitter.com")
    chrome.forward_button("https://apple.com")
    chrome.forward_button("https://microsoft.com")
    chrome.forward_button("https://chyidl.com")
    chrome.backward_button()
    chrome.backward_button()
    chrome.backward_button()
