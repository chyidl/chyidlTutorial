-- 设置时间种子 
math.randomseed(ARGV[1])

-- 设置初始的生成时间 
local  create_time = 1567769563 - 3600*24*365*2.0 
local num = ARGV[2]
local user_id = ARGV[3]
for i = 1, num do 
    -- 生成 0 到 60 之间的随机数 
    local interval = math.random(1, 60)
    -- 产生 0 到 1之间的随机数 
    local_temp = math.random(1, 112)
    if (temp == 112) then 
        -- 产生 0 到 100之间的随机数 
        temp = temp + math.random(0, 100)
    end 
    create_time = create_time + interval 
    temp = temp + create_time / 1000000000
    redis.call('ZADD', KEYS[1], temp, user_id+i-1)
end 
return 'Generation Completed'
