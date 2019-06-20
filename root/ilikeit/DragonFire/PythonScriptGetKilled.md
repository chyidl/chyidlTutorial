Python Script Gets killed
=========================

* Script Starts without any problem but suddenly gets killed.
```
 00:12:17  pi@RPi3BPlus  ~/chyidl.com/PyPrj 
$ python3 test_bulk_load_data_mysql.py
Connected to DB: XXX
[1]    10617 killed     python3 test_bulk_load_data_mysql.py
```

* Check syslog for **Out Of Memory** killer
```
 1237 Jun 19 01:46:29 RPi3BPlus kernel: [106417.500830] Out of memory: Kill process 10617 (python3) score 784 or sacrifice child
 1238 Jun 19 01:46:29 RPi3BPlus kernel: [106417.548602] Killed process 10617 (python3) total-vm:1593140kB, anon-rss:789260kB, file-rss:0kB, shmem-rss:0kB
 1239 Jun 19 01:46:29 RPi3BPlus kernel: [106418.174425] oom_reaper: reaped process 10617 (python3), now anon-rss:0kB, file-rss:0kB, shmem-rss:0kB
```
