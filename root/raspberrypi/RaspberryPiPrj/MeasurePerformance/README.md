Measure Performance
===================

Measure Disk Performance 
------------------------
>Using Fio : is a free and open source tool that can be used for benchmark and hardware verfification.
```
# install Fio
$ sudo apt install fio -y 

# Working with Fio 

# Example1: Random Write Test : write a total 2GB file[4 jobsx512MB=2GB] running 4 processes at a time 
$ sudo fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting

# Example2: Random Read Test : reads a total 2GB of files, running 4 processes at once.
$ sudo fio --name=randread --ioengine=libaio --iodepth=16 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reposting 

# Example 3: Read Write Performance Test
$ sudo fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=random_read_write.fio --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
```
