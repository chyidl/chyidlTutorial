#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Chyi Yaqing'
# __version__ = "0.0.1"
# __maintainer__ = "Chyi Yaqing"
# __status__ = "Production"
"""
Here are four basic steps for sending emails using Python3:
    1. Set up the SMTP server and log into your account
    2. Creare the MEMEMultipart message object and load it with appropriate
        headers for From, To, and Subject fields
    3. Add your message body.
    4. Send the message using the SMTP server object
"""
# import the smtplib module. It should be included in Python3 by default
# SMTP (Simple Mail Transfer Protocol) is an application-level protocol(
# on top of TCP)
# SMTP is delivery protocol only, you can't retrieve email with it.
# If you want to retrieve email, you need to check out the IMAP
# (Internet Message Access Protocol)
# smtplib which handles all of the different parts of the protocl, like
#   connecting, authenticating, validation, sending email
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# SMTP server lists
smtp_Dicts = {
        'gmail': ('smtp.gmail.com', 587),
        'yahoo': ('smtp.mail.yahoo.com', 587),
        'hotmail': ('smtp-mail.outlook.com', 587),
        'live': ('smtp.live.com', 587),
        'qq': ('smtp.qq.com', 587),
        '163': ('smtp.163.com', 994),
        }

# Have the message template
message_Template = """Dear ${PERSON_NAME},

This is a test message.
Have a good day!

Yours Truly
"""


class ChyiEmail:
    def __init__(
            self,
            fromAddr,
            fromPasswd,
            toNames,
            toEmails,
            subject,
            msgTemplate=message_Template):
        self._addr = fromAddr
        self._passwd = fromPasswd
        self._toNames = toNames     # list
        self._toEmails = toEmails   # list
        self._subject = subject     #
        self._msgTemplate = Template(msgTemplate)    # Template Object

    def _setupSMTP(self):
        # set up the SMTP server
        (self._server_host, self._server_port) = smtp_Dicts[
                self._addr.split('@')[-1][:-4]]
        try:
            self._server = smtplib.SMTP(
                    host=self._server_host,
                    port=self._server_port)
            self._server.ehlo()     # Says 'hello' to the server
            self._server.starttls()  # Start TLS encryption
            self._server.login(self._addr, self._passwd)  # Log in to server
        except Exception as err:
            print('Oops! SMTPServer unexpectedly, {}'.format(err))
            raise err

    def sendMsg(self):
        self._setupSMTP()

        # For each contact, send the email:
        for name, email in zip(self._toNames, self._toEmails):
            msg = MIMEMultipart()   # Create a message

            # add in the actual person name to the message template
            message = self._msgTemplate.substitute(PERSON_NAME=name.title())

            # setup the parameters of the message
            msg['From'] = self._addr
            msg['To'] = email
            msg['Subject'] = self._subject
            msg.add_header('Content-Type', 'text/plain')
            # add in the message body
            msg.attach(MIMEText(message, 'html', 'utf-8'))

            # send the message via the server set up earlier
            self._server.send_message(msg)

            del msg

        # Terminate the SMTP session and close the connection
        self._server.quit()

    def __del__(self):
        # Terminate the SMTP session and close the connection
        # Return the result of the SMTP QUIT command
        pass


def sendMessage(
        fromAddr='test@qq.com',
        fromPasswd='ilsuveijbqelbabh',
        toNames=['Chyi Test'],
        toEmails=['test@gmail.com'],
        subject="", msgTemplate=""):
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
            msgTemplate)
    sendEmail.sendMsg()  # Send massage


if __name__ == '__main__':
    sendMessage()
