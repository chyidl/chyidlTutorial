#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def you_say():
    print("Tomato")

async def i_say():
    print("Tomahto")

# Let's call the whole thing... "off"
def spam():
    you_say()
    await i_say()
