#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time
import socket
import datetime
from chyiemail import sendMessage
import mysql.connector


# LPlus Test-Dev 01 MySQL
lplus_test_dev_01_conf = {
    'host': '',
    'port': 3306,
    'user': '',
    'password': '',
    'charset': 'utf8'
}

# Change to your own account information
fromAddr = '@qq.com'
fromPasswd = ''
Names = ['']
Emails = ['@gmail.com']
Subject = ""
message_Template = """<!DOCTYPE html>
<html>
    <body>
Dear ${PERSON_NAME},

[CHYIDL.COM.HOOK]

Yours Truly
    </body>
</html>
"""


def get_device_ip_address():
    try:
        if os.name == "nt":
            # On Windows
            result = "Running on Windows"
            hostname = socket.gethostname()
            result += "\nHostname: " + hostname
            host = socket.gethostbyname(hostname)
            result += "\nHost-IP-Address: " + host
            return result
        elif os.name == "posix":
            # gw = os.popen("ip -4 route show default").read().split()
            # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # s.connect((gw[2], 0))
            # ipaddr = s.getsockname()[0]
            # gateway = gw[2]
            # host = socket.gethostname()
            lsb_release = os.popen("lsb_release -a").read()
            # result = lsb_release + "\nIP:\t\t" + ipaddr + "\nGateway:\t\t" +
            # gateway + "\nHost:\t\t" + host
            ifconfig = os.popen("ifconfig").read()
            result = lsb_release + ifconfig
            return result
        else:
            result = os.name + " not supported yet."
            return result
    except Exception as e:
        return "Could not detect ip address, {}".format(e)


def get_mysql_storage_info(conf, totalStorage):
    """
    获取数据库占用空间大小
    :param conf: MySQL 连接信息
    :param totalStorage: 数据库总存储空间
    :return: status, rst: ture|false, string
    """
    try:
        status = False
        rst_str = """Host: {}\n""".format(conf['host'])
        check_storage_sql = 'SELECT TABLE_SCHEMA AS "Database Name", ' \
                            'ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) AS "Size in (GB)" ' \
                            'FROM information_schema.TABLES GROUP BY TABLE_SCHEMA ' \
                            'UNION ' \
                            'SELECT "Total Databases", SUM(`Size in (GB)`) AS "Size in (MB)" ' \
                            'FROM (SELECT TABLE_SCHEMA AS "Database Name", ' \
                            'ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) AS "Size in (GB)" ' \
                            'FROM information_schema.TABLES GROUP BY TABLE_SCHEMA) AS tmp_chyi GROUP BY "Size in (MB)";'
        cnx = mysql.connector.connect(**conf)
        cursor = cnx.cursor()
        cursor.execute(check_storage_sql)
        percentage = None; count = 0;
        print_str = """+--------------------+--------------+
| Database Name      | Size in (GB) |
+--------------------+--------------+"""
        print(print_str)
        rst_str += '<table style="width:50%"><tr><th>{}</th><th>{}</th></tr>\n'.format("database Name", "Size in (GB)")
        for (database, size) in cursor:
            if database == "Total Databases":
                percentage = size/totalStorage * 100
                if percentage > 90:
                    status = True
            count += 1
            print_str = """|{0}|{1}|""".format(database+' '*(20-len(database)), ((14-len(str(size)))*' '+str(size)))
            print(print_str)
            rst_str += '<tr><td>{}</td><td>{}</td></tr>\n'.format(database, size)
        print_str = """+--------------------+--------------+"""
        print(print_str)
        rst_str += '</table>'
        if percentage:
            print_str = "{} rows in result, current percentage {} %".format(count+1, round(percentage, 2))
            print(print_str)
            rst_str += print_str + "\n"
        return status, rst_str
    except mysql.connector.Error as err:
        print("mysql.connector.Error {}".format(err))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()


def timeit(func):

    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('[ %r ] %r (%r, %r) %2.2f sec' % (
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), func.__qualname__, args, kwargs, te-ts))
        return result

    return timed


@timeit
def run():
    status, rst_str = get_mysql_storage_info(lplus_test_dev_01_conf, 150)
    if status:
        template = message_Template.replace('[CHYIDL.COM.HOOK]', rst_str)
        sendMessage(fromAddr, fromPasswd, Names, Emails, Subject, template)
    print("[{}] Thanks my boss: -)".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == '__main__':
    run()

"""
+--------------------+--------------+
| Database Name      | Size in (GB) |
+--------------------+--------------+
|chyi_test           |          0.00|
|demo                |          0.06|
|hq                  |         19.51|
|information_schema  |          0.00|
|jyck                |          0.61|
|mysql               |          0.01|
|performance_schema  |          0.00|
|quant_new           |         67.59|
|recharge            |          0.00|
|sys                 |          0.00|
|test1               |          0.23|
|yongsheng_test      |          0.00|
|zonwer_test         |          0.00|
|Total Databases     |         88.01|
+--------------------+--------------+
15 rows in result, current percentage 58.67 %
[2019-06-12 16:39:23] Thanks my boss: -)
[ '2019-06-12 16:39:23' ] 'run' ((), {}) 1.11 sec
"""
