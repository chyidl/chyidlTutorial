Lecture 1: Course Overview + The Shell
======================================
```
absulute path: 
relation path: 
cd: 
pwd: 
.: the current directory 
..: the parent directory 
ls:
~: Home directory
cd -: previous directory 
--help: information help
d: directory 
read write execute: 
make any sense: 没有任何意义 
directory -execute premission: 
mv: rename file 
cp: copy 
rm: removing --recusive 
rmdir: 
mkdir: escape space
man: manual page 
Ctrl-L: clear screen 
input stream: 
output stream: 
> : rewrite the input 
< : 
cat: print the content of a file  cat < hello.txt > hello2.txt
>>:append
| : pipe  
tail : read from input and write to output
curl: 
root user: allowed to do 
administator user: 
sudo: su 
tee: 
find: 
xdg-open: for linux
check it out: 查查看 
```
new email notify brightness keyboard 

Lecture 2:Shell Tools and Scripting
=================================== 
```
"": 
'': 

mcd () {
  mkdir -p "$1"
  cd $1"
}

$0 : the name of the script 
$# : the number of arguments that we are gving to the command 
$$ : the process ID of this command that is running 
$@ : will expand to all the arguments
$? : get your the error code from the previous command
$_ : get your the last argumebt of the previous command
0 : means everything went fine
cat <(ls) <(ls ..) : 
* : 
? : single one 

mv image.{png,jpeg}
{a..j} : 
diff : 

#!/usr/bin/env python3 
rg : recursively search current directory for lines matching a pattern
sudo apt-get install shellcheck : 
convert :
ffmpeg : 
tldr : 
  tldr convert 
  tldr ffmpeg 
how to find file ? 
ls: 
find . -name src -type d 
find . -path '**/test/*.py' -type f 
find . -mtime -1 
find . -name "*.tmp" -exec rm {} \;
find short command fd:
locate : 
grep : 
grep foobar mcd.sh 
grep -R foobar 
rg: command line ripgrep
ack: 
ag: 
history: 
Ctrl-R : backward search 
fzf: fuzzy match 
-R : recursively 
tree: 
broot: 
nnn : 
```
```
#!/bin/bash 

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do 
  # 2: mean standard error 
  grep foobar "$file" > /dev/null 2> /dev/null 
  # When pattern is not found, grep has exit status 
  # We redirect STDOUT and STDERR to a null register about them 
  if [[ "$?" -ne 0 ]]; then 
    echo "File $file does not have any foobar, adding one"
    echo "# foobar" » "$file"
  fi 
done
```

Lecture 3: Editors (VIM)
-----------------------
vim emulation mode: 
any questions so far 
> Vim is a model editor?
> 1. normal model: 
> 2. insert model:
> 3. replace mode 
> 4. selection mode 
> 5. command mode : 
>
key rebinding 

