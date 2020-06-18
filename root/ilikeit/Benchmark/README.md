Benchmark
=========
> measure performance

* Disk Performance
  - Measuring random IOPS with FIO 
```
IOPS: Input/Output Operations Second. 
  1. Random reads, random writes, or a combination of both. Databases in particular will pull data from all over your disk - known as random access.
  2. 4 kilobyte blocks, Again, databases and many other programs will read very small chunks of data-4 kilobytes is a good working estimate.
  3. Multiple threads. 

FIO is a popular tool for measuting IOPS on a Linux server. 
$ sudo apt-get update && apt-get install -y make gcc libaio-dev 
$ wget https://github.com/axboe/fio/archive/fio-3.20.zip; extract fio*
$ cd fio* 
$ make 
$ sudo make install

Random read/write performance 
> will create a 4GB file, and perform 4Kb reads and writes using a 75%/25%(ie 3 reads are performed for every 1 write) split within the file, with 64 operations running at a time. The 3:1 ratio is a rougth approximation of your typical database.
$ fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
test: (g=0): rw=randrw, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.1
Starting 1 process
test: Laying out IO file (1 file / 4096MiB)
Jobs: 1 (f=1): [m(1)][100.0%][r=6742KiB/s,w=2202KiB/s][r=1685,w=550 IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=30999: Thu Jun 18 10:56:10 2020
   read: IOPS=1603, BW=6415KiB/s (6569kB/s)(3070MiB/490043msec)
   bw (  KiB/s): min= 5956, max= 7522, per=99.51%, avg=6383.40, stdev=122.48, samples=980
   iops        : min= 1489, max= 1880, avg=1595.42, stdev=30.68, samples=980
  write: IOPS=535, BW=2144KiB/s (2195kB/s)(1026MiB/490043msec)
   bw (  KiB/s): min= 1697, max= 2695, per=99.53%, avg=2133.01, stdev=117.08, samples=980
   iops        : min=  424, max=  673, avg=532.69, stdev=29.20, samples=980
  cpu          : usr=0.69%, sys=1.79%, ctx=134474, majf=0, minf=7
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwt: total=785920,262656,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=6415KiB/s (6569kB/s), 6415KiB/s-6415KiB/s (6569kB/s-6569kB/s), io=3070MiB (3219MB), run=490043-490043msec
  WRITE: bw=2144KiB/s (2195kB/s), 2144KiB/s-2144KiB/s (2195kB/s-2195kB/s), io=1026MiB (1076MB), run=490043-490043msec

Disk stats (read/write):
  vda: ios=785979/262904, merge=1/204, ticks=23299656/7930424, in_queue=27264812, util=88.85%

Random read performance:
$ fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randread 
test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [r(1)][99.8%][r=8832KiB/s,w=0KiB/s][r=2208,w=0 IOPS][eta 00m:01s]s]
test: (groupid=0, jobs=1): err= 0: pid=6434: Thu Jun 18 13:17:40 2020
   read: IOPS=2140, BW=8564KiB/s (8769kB/s)(4096MiB/489784msec)
   bw (  KiB/s): min= 6700, max=10231, per=99.52%, avg=8521.53, stdev=292.35, samples=979
   iops        : min= 1675, max= 2557, avg=2130.14, stdev=73.07, samples=979
  cpu          : usr=0.63%, sys=1.61%, ctx=160452, majf=0, minf=72
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwt: total=1048576,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
   READ: bw=8564KiB/s (8769kB/s), 8564KiB/s-8564KiB/s (8769kB/s-8769kB/s), io=4096MiB (4295MB), run=489784-489784msec

Disk stats (read/write):
  vda: ios=1048259/190, merge=0/79, ticks=31234292/5464, in_queue=22823644, util=74.42%

Random write performance 
$ fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randwrite
test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.1
Starting 1 process
Jobs: 1 (f=1): [w(1)][100.0%][r=0KiB/s,w=9541KiB/s][r=0,w=2385 IOPS][eta 00m:00s]
test: (groupid=0, jobs=1): err= 0: pid=12777: Thu Jun 18 13:27:53 2020
  write: IOPS=2140, BW=8562KiB/s (8767kB/s)(4096MiB/489883msec)
   bw (  KiB/s): min= 6753, max=10251, per=99.52%, avg=8519.50, stdev=222.52, samples=979
   iops        : min= 1688, max= 2562, avg=2129.62, stdev=55.62, samples=979
  cpu          : usr=0.61%, sys=1.48%, ctx=90159, majf=0, minf=8
  IO depths    : 1=0.1%, 2=0.1%, 4=0.1%, 8=0.1%, 16=0.1%, 32=0.1%, >=64=100.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
     issued rwt: total=0,1048576,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
  WRITE: bw=8562KiB/s (8767kB/s), 8562KiB/s-8562KiB/s (8767kB/s-8767kB/s), io=4096MiB (4295MB), run=489883-489883msec

Disk stats (read/write):
  vda: ios=260/1048859, merge=0/490, ticks=11012/31229040, in_queue=22690420, util=73.99%

Measuring latency with IOPing 
> The final aspect of evaluating disk performance is to measure the latency on individual requests. One way to do so is to install ioping using the following command:
$ sudo apt-get update && sudo apt-get install -y make gcc libaio-dev 
$ wget https://github.com/koct9i/ioping/archive/v1.2.tar.gz; extract ioping* 
$ cd ioping* 
$ make 
$ sudo make install 

Run ioping to get an idea of the per-request latency:
$ ioping -c 10 .
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=1 time=3.19 ms (warmup)
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=2 time=798.9 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=3 time=728.5 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=4 time=787.9 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=5 time=773.2 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=6 time=746.1 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=7 time=681.4 us (fast)
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=8 time=764.1 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=9 time=702.5 us
4 KiB <<< . (ext4 /dev/vda1 39.2 GiB): request=10 time=740.2 us

--- . (ext4 /dev/vda1 39.2 GiB) ioping statistics ---
9 requests completed in 6.72 ms, 36 KiB read, 1.34 k iops, 5.23 MiB/s
generated 10 requests in 9.00 s, 40 KiB, 1 iops, 4.44 KiB/s
min/avg/max/mdev = 681.4 us / 747.0 us / 798.9 us / 36.5 us
```
