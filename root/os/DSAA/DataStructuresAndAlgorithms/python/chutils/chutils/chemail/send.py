#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# receive.py
# chemail
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
# Created by Chyi Yaqing on 03/06/19 12:29.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
POP3 收取邮件
收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上，收取邮件最常用的协议是POP协议，目前版本号为3,俗称POP3

POP3协议收取的不是一个已经阅读的邮件本身，而是邮件的原始文本
要将POP3收取的文本变成可以阅读的邮件，还需要email模块提供的各种类解析原始文本，编程可阅读的邮件对象

收取邮件分两步:
    第一步: poplib 把邮件的原始文本下载到本地
    第二步：email解析原始文本，还原邮件对象
"""
import os
from chemail import ChyiEmail


def sendMessage(
         fromAddr, fromPasswd, toNames, toEmails,
         subject="Hi", msgTemplate="lol", attach=['./iMac_G4.png']):
    """
    fromAddr:
    fromPasswd:
    toNames: this is list
    toEmails: this is list
    subject
    msgTemplate: string.Template
    """
    sendEmail = ChyiEmail(
            fromAddr,
            fromPasswd,
            toNames,
            toEmails,
            subject,
            msgTemplate,
            attach)
    sendEmail.sendMsg()  # Send massage


if __name__ == '__main__':
    env_dist = os.environ
    fromAddr = env_dist.get('Email_addr')
    fromPasswd = env_dist.get('Email_password')
    toNames = ['Chyi Yaqing']
    toEmails = [env_dist.get('Email_receive')]
    sendMessage(fromAddr, fromPasswd, toNames, toEmails)
