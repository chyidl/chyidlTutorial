Monitor Linux Performance 
=========================

1. Top - Linux Process Monitoring
---------------------------------
> The top command used to display all the running and active real-time processes in ordered list and updates it regularity.
It display CPU usage, Memory usage, Swap Memmory, Cache Size, Buffer Size, Process PID, User, Commands, It also shows high
memory and cpu utilization of a running processes. 
```
Shift+o -- to Sort field via field letter, for example press 'a' letter to sort process with PID(Process ID)

# Use top command with 'u' option will display specific User process details
$ top -u root  # Display Specific User Process 

# Highlight Running Process in Top 
Press 'z' option in running top command will display running process in color whihc may help you to identified running process easily.

# Shows Absolute Path of Processes 
Press 'c' option in running top command, it will display absolute path of running process.

# Change Delay or Set 'Screen Refresh Interval' in Top 
By default screen refresh interval is 3.0 seconds, same can be change pressing 'd' option in running top command and change it as desired as shown below.

# Kill running process with argument 'k'
You can kill a process after finding PID of process by pressing 'k' option in running top command without exiting from top window as shown below.

# Sort by CPU Utilisation 
Press (Shift + p) to sort processes as per CPU utilization 

# Renice a Process 
use 'r' option to change the priority of the process also called Renice.

# Save Top Command Results 
To save the running top command results output to a file /root/.toprc use the following command.
$ top -n 1 -b > top-output.txt 

# Getting Top Command Help 
Press 'h' option to obtain the top command help 

# Exit Top Command After Specific repetition 
Top output keep refreshing until you press 'q'. With below command top command will automatically exit after 10 number of repetition 
$ top -n 10 
```


