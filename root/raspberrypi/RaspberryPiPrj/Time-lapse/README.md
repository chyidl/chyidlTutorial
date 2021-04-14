Time-lapse
==========
> To create a time-lapse video, simply configure the Raspberry Pi to take a picture at a regular interval, such as once a seconds, then use an application ffmpeg to stitch the picture together into a video.

Create your own Time Lapse script
---------------------------------
```
# Install dependencies
$ sudo apt-get install -y python-picamera python-yaml imagemagick

create script timelapse.py
# timelapse.py
from picamera import PiCamera

camera = PiCamera()
camera.capture('image.jpg')
```

Appendix
--------
* YAML
> 一种通用的数据串形化格式
```
1. 大小写敏感
2. 使用缩进标示层级关系
3. 缩进时不允许使用Tab健, 只允许使用空格
4. 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
5. # 标示注释，

YAML支持的数据结构有三种
    对象: 键值对的集合，又称为映射(mapping)/哈希(hashes)/字典(dictionary)
        hash: {name: Steve, foo: bar}
        or
        hash:
            name: Steve
            foo: bar
    数组: 一组按次序排列的值,又称为序列 sequence/列表 list
        animal: [cat, dog]
    纯量: scalars 单个的、不可再分的值
        纯量是最基本的，不可在分的值
        字符串:
            单引号和双引号都可以使用，双引号不会对特殊字符转义
        布尔值 true,false
        整数
        浮点数
        Null: - 表示
        时间
        日期
    YAML允许使用两个感叹号!!强制转换数据类型
        e: !!str 123

```

