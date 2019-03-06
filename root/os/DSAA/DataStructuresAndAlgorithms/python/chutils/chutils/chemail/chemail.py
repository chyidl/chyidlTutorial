#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# chemail.py
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
import smtplib  # smtplib 负责发送邮件
import poplib  # POP3协议 收邮件
from string import Template
# email 负责构造邮件
from email import encoders
from email.header import Header, decode_header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# 解析邮件
from email.parser import Parser

# SMTP server lists
# 25端口时明文传输
smtp_Dicts = {
        'gmail': ('smtp.gmail.com', 587),
        'yahoo': ('smtp.mail.yahoo.com', 587),
        'hotmail': ('smtp.office365.com', 587),
        'live': ('smtp.live.com', 587),
        'qq': ('smtp.qq.com', 587),
        '163': ('smtp.163.com', 994),
        }

# POP3 server lists
pop_Dicts = {
        'gmail': ('pop.gmail.com', 995),
        'yahoo': ('pop.mail.yahoo.com', 995),
        'hotmail': ('outlook.office365.com', 995),
        'live': ('pop3.live.com', 995),
        'qq': ('pop.qq.com', 995),
        '163': ('pop.163.com', 995),
        }


# Have the message template
message_Template = """Dear ${PERSON_NAME},

This is a test message.
Have a good day!

Yours Truly
"""


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def _attach_image(msg, filepath):
    with open(filepath, 'rb') as f:
        # 设置附件的MIME和文件名
        filename = filepath.split('/')[-1]
        filetype = filename.split('.')[-1]
        mime = MIMEBase('image', filetype, filename=filename)
        # 加上必要的头部信息
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
        return msg


# 解析附件内容并添加到MIMEBase
def _parse_attach(msg, plist):
    if not plist:
        # 附件为空
        return msg
    for fpath in plist:
        # 解析文件列表的后缀
        msg = _attach_image(msg, fpath)
    return msg


def _decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def _guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# 递归打印Message对象的层次结构
def _parser_Message_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = _decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = _decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s------------' % (' ' * indent))
            _parser_Message_info(part, indent+1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = _guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))


class ChyiEmail():

    def __init__(
            self,
            fromAddr,
            fromPasswd,
            toNames=[],
            toEmails=[],
            subject='Hi',
            msgTemplate=message_Template,
            attach=[]):
        self._addr = fromAddr  # 输入Email地址
        self._passwd = fromPasswd   # 输入Email口令
        self._toNames = toNames     # list 收件人列表
        self._toEmails = toEmails   # list 收件人邮件列表
        self._subject = subject     #
        self._msgTemplate = Template(msgTemplate)    # Template Object
        self._attach = attach  # 邮件附件 (默认情况下是文件路径,以文件后缀区分类型)

    def _setupSMTP(self):
        # connect to SMTP Server
        (self._server_host, self._server_port) = smtp_Dicts[
                self._addr.split('@')[-1][:-4]]
        try:
            self._server = smtplib.SMTP(
                    host=self._server_host, port=self._server_port)
            self._server.set_debuglevel(1)  # 打印出SMTP服务器交互信息
            self._server.ehlo()
            self._server.starttls()  # 创建安全连接
            self._server.login(self._addr, self._passwd)
        except Exception as err:
            print('Oops! Connect to SMTPServer unexpectedly, {}'.format(err))
            raise err

    def _setupPOP(self):
        # connect to POP3 Server
        (self._server_host, self._server_port) = pop_Dicts[
                self._addr.split('@')[-1][:-4]]
        try:
            self._server = poplib.POP3_SSL(
                    host=self._server_host, port=self._server_port)
            # 打开或者关闭调试信息
            self._server.set_debuglevel(1)
            # 打印POP3服务器的欢迎文字
            print(self._server.getwelcome().decode('utf-8'))
            # 身份认证
            self._server.user(self._addr)
            self._server.pass_(self._passwd)
            # self._server.login(self._addr, self._passwd)
        except Exception as err:
            print('Oops! Connect to POPServer unexpectedly, {}'.format(err))
            raise err

    def sendMsg(self):
        self._setupSMTP()

        # For each contact, send the email:
        for name, email in zip(self._toNames, self._toEmails):
            # msg = MIMEText 邮件本身 + MIMEBase 附件对象
            msg = MIMEMultipart()   # Create a message

            # add in the actual person name to the message template
            message = self._msgTemplate.substitute(PERSON_NAME=name.title())

            # setup the parameters of the message
            msg['From'] = _format_addr('chyidl.com 管理员 <%s>' % self._addr)
            msg['To'] = _format_addr('%s <%s>' % (name, email))
            msg['Subject'] = self._subject

            # add in the message body -- Send Plain And HTML
            # MIMEText对象 第一个参数：邮件正文;第二个参数:subtype;第三个参数： 编码方式
            msg.attach(MIMEText(message, 'plain', 'utf-8'))

            # Send HTML
            msg.attach(MIMEText('''
            <html>
                <body>
                    <h1>Hello</h1>
                    <p>send by
                        <a href="http://www.python.org">Python</a>
                    {}
                    <img src="cid:0">
                    </p>
                </body>
            </html>'''.format(message), 'html', 'utf-8'))

            # 添加附件就是加上一个MIMEBase，从本地读取一个图片
            msg = _parse_attach(msg, self._attach)

            # send the message via the server set up earlier
            self._server.send_message(msg)

            del msg

        # Terminate the SMTP session and close the connection
        self._server.quit()

    # Receive Email
    def receiveEmail(self):
        self._setupPOP()  # 连接到POP3服务器
        # stat() 返回邮件数量和占用空间
        print('Messages: %s. Size: %s' % self._server.stat())
        # list() 返回所有邮件的编号
        resp, mails, octets = self._server.list()
        print(mails)

        # 获取最新的一封邮件，注意索引号从1开始
        index = len(mails)
        # lines 存储邮件的原始文本的每一行, 可以获取整个邮件的原始文本
        resp, lines, octets = self._server.retr(index)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        # 将邮件内容解析为Message对象
        msg = Parser().parsestr(msg_content)

        # 递归打印Message对象
        _parser_Message_info(msg, indent=0)

        # 可以根据邮件索引号直接从服务器删除邮件
        # self._server.dele(index)

        # Terminate the POP session and close the connection
        self._server.quit()

    def __del__(self):
        # Terminate the SMTP session and close the connection
        # Return the result of the SMTP QUIT command
        pass
