# 抢票模拟使用DECR原子操作
import redis
import threading

pool = redis.ConnectionPool(host='localhost', port=6379, db=0, password='macintosh')
r = redis.StrictRedis(connection_pool=pool)

KEY = "ticket_count"
def sell(i):
    temp = r.decr(KEY)
    if temp >= 0:
        print("用户{} 抢票成功，当前票数{}".format(i, temp))
    else:
        print("用户{}抢票失败,票卖完了".format(i))


if __name__ == '__main__':
    r.set(KEY, 5)
    for i in range(8):
        t = threading.Thread(target=sell, args=(i,))
        t.start()
