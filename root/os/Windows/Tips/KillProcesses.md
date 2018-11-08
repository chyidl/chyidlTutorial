# Kill Processes from Command Prompt 

I'm sure you are familiar with the traditional way to kill or end a process in Windows using Task Manager. This method is effective but not nearly as fun as killing a process in Command Prompt. Additionally, killing processes in Command Prompt provides much more control and the ability to end multiple processes at once.

All of this is possible with the TaskKill command. You can kill a process by the process ID (PID) or by image name (EXE filename).

C:\>tasklist 
- Open up an Administrative level Command Prompt and run tasklist to see all of the running processes. IM (image name) 

C:\>Taskkill /IM firefox.exe /F 

or

C:\>Taskkill /PID 9527 /F 
- kill the firefox process , /F flag is kills the process forcefully. If you have multiple instances of animage open such as multiple firefox.exe processes, running the taskkill /IM firefox.exe command will kill all instances. When you specify the PID only the specific instance of firefox will be terminated.

The real power of taskkill are the filtering options that allow you to use the following avriables and operators.

Variables:

- STATUS
- IMAGENAME
- PID
- SESSION
- CPUTIME
- MEMUSAGE
- USERNAME
- MODULES
- SERVICES
- WINDOWTITLE

Operators:

- eq (equals)
- ne (not equal)
- gt (greater than)
- lt (less than)
- ge (greater than or equal)
- le (less than or equal)

"*" is the wildcard 

For example, let's say you want to end all processes that have a window title that starts with "Internet"
C:\>taskkill /FI "WINDOWTITLE eq Internet*" /F 

How about killing all processes running under the Steve account
C:\>taskkill /FI "USERNAME eq Steve" /F 

It is also possible to kill a process running on a remote computer with taskkill. Just run the following to kill notepad.exe on a remote computer called SteveDesktop:
C:\>taskkill /S SteveDesktop /U RemoteAccountName /P RemoteAccountPassword /IM notepad.exe /F 

- SLEEP <seconds> | SLEEP -m <time in milliseconds> 
- PING 127.0.0.1 -n 6 > nul  # using ping command to relay 5 seconds 


How to check if a process is running via a batch script. 

