import redis
import threading

# 创建连接池
pool = redis.ConnectionPool(host="localhost", port=6379, db=0, password='macintosh')
r = redis.StrictRedis(connection_pool = pool)

KEY = "ticket_count"

# 模拟第i用户进行抢票
def sell(i):
    # 初始化 pipe
    pipe = r.pipeline()
    while True:
        try:
            # 监视票数
            pipe.watch(KEY)
            # 查看票数
            c = int(pipe.get(KEY))
            if c > 0:
                # 开始事务
                pipe.multi()
                c = c-1
                pipe.set(KEY, c)
                pipe.execute()
                print("用户 {} 抢票成功, 当前票数 {}".format(i, c))
                break
            else:
                print("用户 {} 抢票失败, 票卖完了".format(i))
                break
        except Exception as e:
            print("用户{}抢票失败，重试一次".format(i))
            continue
        finally:
            pipe.unwatch()


if __name__ == '__main__':
    # 初始化
    r.set(KEY, 5)
    for i in range(100):
        t = threading.Thread(target=sell, args=(i,))
        t.start()
