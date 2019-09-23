/*
 * HyperLogLog.java
 * java
 *
 *             .''
 *   ._.-.___.' (`\
 *  //(        ( `'
 * '/ )\ ).__. )
 * ' <' `\ ._/'\
 *    `   \     \
 *
 * Created by Chyi Yaqing on 09/20/19 16:25.
 * Copyright (C) 2019. Chyi Yaqing.
 * All rights reserved.
 *
 * Distributed under terms of the MIT license.
 */

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

public class HyperLogLog {
    
    // Redis服务器IP
    private static String REDIS_HOST = "192.168.1.243";
    // Redis端口号
    private static int REDIS_PORT = 6379;
    // 访问密码
    private static String REDIS_AUTH = "000000";

    // 可用连接实例的最大数目，默认值8
    // 如果赋值为-1,则表示不限制;如果pool已经分配了maxActive个jedis实例，则此时pool的状态为exhausted(耗尽)
    private static int MAX_ACTIVE = 128;

    // 控制一个pool最多有多少个状态为idle(空闲)的jedis实例，默认值为8
    private static int MAX_IDLE = 10;

    // 等待可用连接的最大时间，单位毫秒，默认值为-1,表示永不超时，如果等待超过等待时间，则直接抛出JedisConnectionException;
    private static int MAX_WAIT = 10000;
    private static int TIMEOUT = 10000;

    // 在borrow一个jedis实例时，是否提前进行validate操作，如果为true,则得到的jedis实例均是可用的
    private static boolean TEST_ON_BORROW = true; 

    private static JedisPool jedisPool = null; 

    /**
     *初始化Redis连接池
     * */
    static {
        try {
            JedisPoolConfig poolConfig = new JedisPoolConfig();
            poolConfig.setMaxActive(MAX_ACTIVE);
            poolConfig.setMaxIdle(MAX_IDLE);
            poolConfig.setMaxWait(MAX_WAIT);
            poolConfig.setTestOnBorrow(TEST_ON_BORROW);
            jedisPool = new JedisPool(config, REDIS_HOST, REDIS_PORT, TIMEOUT, REDIS_AUTH);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        // Connecting to Local Redis server 
        Jedis jedis = null;
        try {
            jedis = jedisPool.getResource();
            System.out.println("Server is running: " + jedis.ping());
            jedis.select(0);
            jedis.auth("000000");
            // ... do stuff here ... for example 
            for (int i = 0; i < 1000; i++) {
                jedis.pfadd("codehole", "user" + i);
                long total = jedis.pfcount("codehole");
                if (total != i + 1) {
                    // check whether server is running or not 
                    System.out.printf("%d %d\n", total, i + 1);
                    break;
                }
            }
        } finally {
            if (jedis != null) {
                jedis.close();
            }
        }
        /// ... when closing your application
        jedisPool.close();
    }
}

