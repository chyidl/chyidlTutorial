Oh-My-Zsh+Vim+Tmux OMG!
======================

Use Homebrew zsh instead of the OS X Default
--------------------------------------------
> If the zsh shell that Apple provides in Mac OS X is out of date, as it has been in Yosemite and EI Capitan, it's trivial to install the latest version, available on homebrew.
```
# Confirm the current active zsh version:
$ zsh --version 
zsh 5.3 (x86_64-apple-darwin18.0)

# Confirm the location of zsh:
$ which zsh 
/bin/zsh 

# Confirm the shell that's set for your user:
$ dscl . -read /Users/$USER UserShell 
UserShell: /bin/zsh

The . is short for locahost, and the $USER variable expands t your username. 

# Upgrade zsh with brew 
$ brew install zsh 

# Confirm brew's zsh location 
Apple provides /usr/local for OS X users to install packages to and it's already in your system path, so that's where brew installs, Confirm it:
$ ls -la /usr/local/bin/zs* 
lrwxr-xr-x  1 chyiyaqing  admin  27 Sep  3 23:42 /usr/local/bin/zsh -> ../Cellar/zsh/5.7.1/bin/zsh
lrwxr-xr-x  1 chyiyaqing  admin  33 Sep  3 23:42 /usr/local/bin/zsh-5.7.1 -> ../Cellar/zsh/5.7.1/bin/zsh-5.7.1

# Use the zsh that brew installed, use dscl. 
$ sudo dscl . -create /Users/$USER UserShell /usr/local/bin/zsh 
After that, restart your Terminal to have it take effect.
$ which zsh 
/usr/local/bin/zsh 
$ zsh --version 
zsh 5.7.1 (x86_64-apple-darwin18.2.0)


# Confirm You're Running Brew zsh 
$ echo $SHELL 

# Handling Upgrades 
$ sudo chown -R $(whoami):admin /usr/local 

(Linux)
$ chsh -s $(which zsh)
```

# Oh-My-Zsh + SpaceShip Theme
```
oh-my-zsh 

Clone this repo:
  $ git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"

Symlink spaceship.zsh-theme to your oh-my-zsh custom themes directory:
  $ ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

Set ZSH_THEME="spaceship" in your .zshrone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
```

Oh-My-Zsh + Bullet Train Theme 
------------------------------
* Requirements:
```
In or der to use the theme( Bullet Train ), you will first need:
	
1. Powerline compatible fonts like Vim Powerline patched fonts(https://github.com/powerline/fonts) 
# clone 
$ git clone https://github.com/powerline/fonts.git --depth=1
# install 
$ cd fonts
$ ./install.sh 
# clean-up a bit 
$ cd .. && rm -rf fonts 
# On Ubuntu like systems you'll need the ttf-ancient-fonts package to correctly display some unicode symbols that are not convered by Powerline fonts above.

2. A ZSH framework like oh-my-zsh(https://github.com/robbyrussell/oh-my-zsh)
# In order Oh-My-Zsh to work, Zsh must be installed 
# Run zsh --version to confirm 
# Expected result: zsh 5.1.1 or more recent 

$ sudo apt-get install git curl wget 
$ sudo apt-get install zsh 
$ chsh -s $(which zsh) 

3. Install oh-my-zsh 
$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

4. Make sure terminal is using 256-colors mode add ~/.zshrc file with export TERM="xterm-256color"

5. For oh-my-zsh users install bullet-train 
$ wget http://raw.github.com/caiogondim/bullet-train-oh-my-zsh-theme/master/bullet-train.zsh-theme
$ mv bullet-train.zsh-theme $ZSH_CUSTOM/themes/
$ vim ~/.zshrc
# change ZSH_THEME="bullet-train"
# add export LANGUAGE=en_US.UTF-8
# add export LC_ALL=en_US.UTF-8
# add export LANG=en_US.UTF-8
# add export LC_TYPE=en_US.UTF-8

5. Or powerlevel10k -- A fast reimplementation of Powerlevel9k ZSH theme 
$ git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k 
# Set ZSH_THEME=powerlevel10k/powerlevel10k in your ~/.zshrc 
# Fonts -- Recommended: Meslo Nerd Font patched for Powerlevel10k 
    MesloLGS NF Regular.ttf 
    MesloLGS NF Bold.ttf 
    MesloLGS NF Italic.ttf 
    MesloLGS NF Bold Italic.ttf 
# This will make MesloLGS NF font available to all applications on your system. Configure your terminal to use this font:
    iTerm2: Open iTerm2 -> Preferences -> Profiles -> Text and set Font to MesloLGS NF.
    Visual Studio Code: Open File -> Preferences -> Settings, enter terminal.integrated.fontFramily in the search box and set the value to MesloLGS NF.
    GNOME Terminal (the default Ubuntu termine): Open Terminal -> Preferences and click on the selected profile under Profiles. Check Custom font under Text Appearance and select MesloLGS NF Regular.
# Run p10k configure to pick the best style for your new font.

6. Let all changes be valid 
$ source ~/.zshrc 

7. Enabling Plugins
$ vim ~/.zshrc
plugins=(
    extract
    git 
)
```
![bullet-train](/imgs/ilikeit/Vim+Tmux/bullet-train.png?raw=true)
- [MesloLGS NF Regular.ttf](/root/ilikeit/Vim+Tmux/fonts/MesloLGS_NF_Regular.ttf)
- [MesloLGS NF Bold.ttf](/root/ilikeit/Vim+Tmux/fonts/MesloLGS_NF_Bold.ttf)
- [MesloLGS NF Italic.ttf](/root/ilikeit/Vim+Tmux/fonts/MesloLGS_NF_Italic.ttf)
- [MesloLGS NF Bold Italic.ttf](/root/ilikeit/Vim+Tmux/fonts/MesloLGS_NF_Bold_Italic.ttf)

Vim Setup Instructions
----------------------
* Install Vim  
```
macOS
# If you're on a mac, you can get the latest vim from Homebrew.
$ brew install macvim --override-system-vim 

Linux (Ubuntu)
$ sudo apt-get install vim 
```

* Oh My Vim!Pretty & versatile vim configuration  
```
# Create a vim configuration file in your home directory and a vim/bundle directory 
$ wget  https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/vimrc -O ~/.vimrc 
$ mkdir -p ~/.vim/bundle 
```

* Add vundle (Vundle, the plug-in manager for Vim)
```
# Vundle is short for Vim bundle and is a Vim plugin manager.
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim 
```

* Configure Plugins:
```
# Put this at the top of your **.vimrc** to use Vundle. 

#  >> Copyright 2018- chyidl (@Chyi Yaqing)

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required 
Plugin 'VundleVim/Vundle.vim'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
```

* Install Plugins
```
Launch vim and run :PluginInstall
To install from command line: 
$ vim +PluginInstall +qall
```
![vim +PluginInstall +qall](/imgs/ilikeit/Vim+Tmux/pluginInstall.png?raw=true)
- [.vimrc](/root/ilikeit/Vim+Tmux/vimrc)


Oh My Tmux!Pretty & versatile tmux configuration(Fork: https://github.com/gpakosz/.tmux) 
----------------------------------------------------------------------------------------
> tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen.
```
# 会话与进程
命令行的典型使用方式是，打开一个终端窗口(terminal window),输入命令，用户与计算机这种临时的交互，称为一次“会话”session.

会话的一个重要特点是，窗口与其中启动的进程是连在一起的，打开窗口，会话开始，关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完.

为了解决这个问题,会话与窗口可以“解绑”：窗口关闭时，会话并不终止，而是继续运行，等到以后需要的时候，再让会话“绑定”其他窗口.

Tmux的作用就是会话与窗口的“解绑”工具:
    1. 允许在单个窗口中，同时访问多个会话，对于同时运行多个命令行程序很有用
    2. 可以让新窗口“接入”已经存在的会话
    3. 允许每个会话有多个连接窗口，因此可以多人实时共享会话
    4. 支持窗口的垂直和水平拆分
类似的终端复用器还有 GNU Screen. 

* Installation 
Requirements:
	1. tmux **`>= 2.1`** running inside Linux, Mac, OpenBSD 
	2. outside of tmux, `$TERM` must be set to `xterm-256color`
	3. check tmux Version $ tmux -V

To install, run the following from your terminal: (you may want to backup your existing `~/.tmux.conf` first)
$ cd 
$ mv .tmux.conf .tmux.conf.old 
$ wget https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/tmux.conf -O .tmux.conf
$ wget https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/tmux.conf.local -O .tmux.conf.local 
```

Features
--------

1. `C-a` acts as secondary prefix, while keeping default `C-b` prefix 
2. visual theme inspired by Powerline 
3. maximize any pane to a new window with `<prefix> +` 
4. SSH/Mosh aware username and hostname status line information 
5. mouse mode toggle with `<prefix> m` 
6. automatic usage of `reattach-to-user-namespace` if available  
7. laptop battery status line information 
8. uptime status line information 
9. optional highlight of focused pane (tmux `>= 2.1`)
10. configurable new windows and panes behavior (optionally retain current path)
11. SSH/Mosh aware split pane (reconnects to remote server, expermental)
12. copy to OS clipboard (needs `reattach-to-user-namespace` on macOS, `xsel` or `xclip` on Linux)
13. [Facebook PathPicker]: https://facebook.github.io/PathPicker/(`brew update; brew install fpp;` on macOS; `sudo apt-get install PathPicker` on Linux)
14. [Urlview]: https://packages.debain.org/stable/misc/urlview 

The "maximize any pane to a new window with `<prefix> +`" feature is different from builtin `resize-pane -Z` as it allows you to further split a maximzed pane. It's also more flexible by allowing you to maximize a pane to a new window, then change window, then go back and the pane is still in maximized state in its own window. You can then minimize a pane by using `<prefix> +` either from the source window or the maximized window.

Mouse mode allows you to set the active window, set the active pane, resize panes and automatically switches to copy-mode to select text. 

Bindings
--------

tmux may be controlled from an attached client by using a key combination of a prefix key, followed by a command key. This configuration uses `C-a` as a secondary prefix while keeping `C-b` as the default prefix. In the following list of key bindings: 

    1. `<prefix>` means you have to either hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b<kbd>
    2. `<prefix> c` means you have to hit <kbd>Ctrl<kbd> + <kbd>a</kbd> or <kbd>Ctrl<kbd> +<kbd>b</kbd> followed by <kbd>c<kbd>
    3. `<prefix> C-c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a<kbd> or <kbd>Ctrl</kbd> + <kbd>b<kbd> followed by <kbd>Ctrl</kbd> + <kbd>c</kbd>

This configuration uses the following bindings:

    1. `<prefix> e` opens `~/.tmux.conf.local` with the editor defined by the `$EDITOR` environment variables (defaults to `vim` when empty)
    2. `<prefix> r` reloads the configuration
    3. `C-l` clears both the screen and the tmux history 
    4. `<prefix> C-c` creates a new session 
    5. `<prefix> C-f` lets you switch another session by name 
    6. `<prefix> C-h` and `<prefix> C-l` let you navigate windows (default `<prefix> n` and `<prefix> p` are unbound)
    7. `<prefix> Tab` brings you to the last active window 
    8. `<prefix> -` splits the current pane vertically 
    9. `<prefix> |` splits the current pane horizontally 
    10. `<prefix> h`, `<prefix> j`, `<prefix> k` and `<prefix> l` let you navigate panes as Vim 
    11. `<prefix> H`, `<prefix> J`, `<prefix> K`, `<prefix> L` let you resize panes
    12. `<prefix> <` and `<prefix> >` let you swap panes 
    13. `<prefix> +` maximizes the current pane to a new window 
    14. `<prefix> m` roggles mouse mode on or off 
    15. `<prefix> U` launches Urlview (if availabele)
    16. `<prefix> F` launches Facebook PathPicker (if available)
    17. `<prefix> Enter` enters copy-mode 
    18. `<prefix> b` lists the paste-buffers 
    19. `<prefix> p` pastes from the top paste-buffer 
    20. `<prefix> P` lets you choose the paste-buffer to paste from 

Bindings for `copy-mode-vi`:

	- 1. `v` begins selection / visual mode 
	- 2. `C-v` toggles between blockwise visual mode and visual mode 
	- 3. `H` jumps to the start of line 
	- 4. `L` jumps to the end of line 
	- 5. `y` copies the selection to the top paste-buffer 
	- 6. `Escape` cancels the current operation

Configuration 
-------------

While configuration tries tp bring same defualt settings, you may want to customize it future to your needs. Instead of altering the `~/.tmux.conf` file and diverging from upstream, the proper way is to edit the `~/.tmux.conf.local` file. 

Please refer to the default `~/.tmux.conf.local` file to know more about variables you can adjesy to alter different behavirors. Pressing `<prefix> e` will open `~/.tmux.conf.local` with the editor defined by the `$EDITOR` environment variable (defaults to `vim` when empty).

### Enabling the Powerline look

Powerline originated as a status-line plugin for Vim. Its popular eye-catching look is base on the use of special symbols

To make use of these symbols, there are several options: 

Then edit the **~/.tmux.conf.local** file (<prefix> e) and adjust the following variables:

```
tmux_conf_theme_left_separator_main = 
tmux_conf_theme_left_separator_sub = 
tmux_conf_theme_right_separator_main = 
tmux_conf_theme_right_separator_sub = 
```

###Configuring the status line

Contrary to the first iterations of this configuration, by now you have total control on the content and order of `status-left` and `status-right`.

Edit the `~/.tmux.conf.local` file (`<prefix> e`) and adjsut the `tmux_conf_theme_status_left` and `tmux_conf_theme_status_right` variables to your own preferences.

This is configuration supports the following buitin variables:

```
`#{battery_bar}` : horizontal battery charge bar 
`#{battery_percentage}` : battery percentage 
`#{battery_status}`: is battery charging or discharging 
`#{battery_vbar}`: vertical battery charge bar 
`#{circle_session_name}`: circled session number, up to 20 
`#{hostname}`: SSH/Mosh aware hostname information 
`#{hostname_ssh}`: SSH/Mosh aware hostname information, blank when not connection to a remote server through SSH/Mosh 
`#{loadavg}`: load average 
`#{pairing}`: is session attached to more than one client?
`#{prefix}`: is prefix being depressed?
`#{root}`: is current user root?
`#{synchronzied}`: are the panes synchronized?
`#{uptime_d}`: uptime days 
`#{uptime_h}`: uptime hours
`#{uptime_m}`: uptime minutes
`#{uptime_s}`: uptime seconds 
`#{username}`: SSH/Mosh aware username information 
`#{username_ssh}`: SSH aware username information, blank when not connected to a remote server through SSH/Mosh
```

Beside custom variables mentioned above, the `tmux_conf_theme_status_left` and `tmux_conf_theme_status_right` variables support usual tmux syntax, e.g. using `#(tmux-itunes-info)` to call an external command that inserts play music info. `#(curl wttr.in?format=3)` to call weather information provided by wttr.in

wttr.in is a console-oriented weather forecast service that supports various inforamtion representation methods like terminal-oriented ANSI-sequences for console HTTP clients (curl, httpie, or wget), HTML for web browsers, or PNG for graphical viewers.

```
tmux_conf_theme_status_left=' ❐ #S | ↑#{?uptime_d, #{uptime_d}d,}#{?uptime_h, #{uptime_h}h,}#{?uptime_m, #{uptime_m}m,} '
tmux_conf_theme_status_right='#{prefix}#{pairing}#(tmux-itunes-info)#(tmux-spotify-info)#{?battery_status, #{battery_status},}#{?battery_bar,     #{battery_bar},}#{?battery_percentage, #{battery_percentage},} , %r , %d %b %y | #{hostname}'
```

- [tmux-spotify-info](/root/ilikeit/Vim%2BTmux/tmux-spotify-info)
- [tmux-itunes-info](/root/ilike/Vim%2BTmux/tmux-itunes-info)
![tmux music info](/imgs/ilikeit/Vim+Tmux/tmux-itunes-info.png?raw=true)


### Accessing the macOS clipboard from with tmux sessions

Chris johnsen created the [`reattach-to-user-namespace` utility](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard) that makes `pbcopy` and `pbpaste` work again within tmux.

To install `reattach-to-user-namespace`, use either [MacPorts][] or [Homebrew][]:
    
    $ port install tmux-pasteboard
or 
    $ brew install reattach-to-user-namespace 

Once installed, `reattach-to-usernamespace` will be automatically detected.

[MacPorts]: http://www.macports.org/
[Homebrew]: http://brew.sh/

### tmux shortcuts & cheatsheet 
```
$ tmux					# start new  
$ tmux new -s name		# start new with session name 
$ tmux a				# attch  -- 用于重新接入某个已存在的会话
$ tmux a -t myname		# attach to 会话名称
$ tmux ls				# list sessions 
$ tmux kill-session -t myname # kill session 
$ tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill  # kill all the tmux sessions 
$ tmux switch -t 0      # 使用会话编号
$ tmux switch -t <session-name> # 使用会话名称 

Sessions 
:new <CR> new session 
<prefix> s	# list sessions 
<prefix> $ name session     # 重命名当前会话

Windows (Tabs)
<prefix> c	# create window 
<prefix> w	# list window 
<prefix> n	# next window 
<prefix> p	# previous window 
<prefix> f	# find window
<prefix> ,	# name window 
<prefix> &	# kill window 

Panes (splits)
<prefix> %	# vertical split 
<prefix> "	# horizontal split 

o			# swap panes 
q			# show pane numbers 
x			# kill pane 
+			# break pane into window 
-			# restore pane from window 
⍽			# space - toggle between layouts
<prefix> q	# (Show pane numbers, when the numbers show up type the key to goto that pane)
<prefix> {  # (Move the current pane left)
<prefix> }  # (Move the current pane right)
<prefix> z  # toggle pane zoom

Misc 
<prefix> d detach 
<prefix> t big clock
<prefix> ? list shortcuts
<prefix> : prompt

Configurations Options:
# Mouse support - set to on if you want to use the mouse
* setw -g mode-mouse off 
* set -g mouse-select-pane off 
* set -g mouse-resize-pane off 
* set -g mouse-select-window off 

# Set the default terminal mode to 256color mode
set -g default-terminal "screen-256color"

# enable activity alerts
setw -g monitor-activity on 
set -g visual-activity on 

# Center the window list 
set -g status-justify centre 

# Maximize and restore a pane 
unbind Up bind Up new-window -d -n tmp \; swap-pane -s tmp.1 \; select-window -t tmp 
unbind Down 
bind Down last-window \; swap-pane -s tmp.1 \; kill-window -t tmp
```
- [.tmux.conf](/root/ilikeit/Vim%2BTmux/tmux.conf)
- [.tmux.conf.local](/root/ilikeit/Vim%2BTmux/tmux.conf.local)

## Attach a tmux session to a remote machine 
```

```

## Using template files in Vim 

Vim templates or skeletons,allow you to specify a template to be used for new files with a certain extension.

The Vim philosophy encourages users to automate repeated actions and provides a rich toolkit with great documentation to achieve that.One example of this type of micro-optimisation is having a template or skeleton file that populates the vim buffer when a new file is opened.

```
# Add below code into .vimrc file 
" Using template files in Vim 
if has("autocmd")
    augroup templates
        autocmd BufNewFile *.* silent! execute '0r ~/.vim/templates/skeleton.'.expand("<afile>:e")
        autocmd BufNewFile * %substitute#\[:VIM_EVAL:\]\(.\{-\}\)\[:END_EVAL:\]#\=eval(submatch(1))#ge
    augroup END
endif
```
- [templates](/root/ilikeit/Vim+Tmux/templates/)
```
# Create a vim templates file in your home directory and a vim/bundle directory 
$ cp -r chyidlTutorial/root/ilikeit/Vim+Tmux/templates ~/.vim/
```

Update to Vim8 on Centos7
-------------------------
```
$ sudo yum install -y gcc git ncurses-devel
$ git clone https://github.com/vim/vim.git 
$ cd vim/src 
$ make distclean  # if you built Vim before 
$ make -j4 
$ sudo make install 
$ cp -ru vim/src/vim /usr/bin # overwrites /usr/bin/vim w/o confirmation 
```

Screen Vs. Tmux 
---------------
```
# Introduction
Screen or GNU Screen is a terminal multiplexer. In other words, it means that you can start a screen session and then open any number of windows (virtual terminals) inside that session. Processes running in Screen will continue to run when their window is not visible event if you get disconnected.

# Install Linux GNU Scrren 
$ screen --version 
Screen version 4.06.02 (GNU) 23-Oct-17

# Starting Named Session (Named sessions are useful when you run multiple screen sessions.)
$ screen -S session_name 

# Working with Linux Screen Windows 
$ screen -S session_name 

# Working With Linux Screen Windows
    Ctrl+a  c   : Create a new window (with shell)
    Ctrl+a "    : List all window 
    Ctrl+a 0    : Switch to window 0 (by number)
    Ctrl+a A    : Rename the current window 
    Ctrl+a S    : Split current region horizontally into two regions 
    Ctrl+a |    : Split current region vertically into two regions  
    Ctrl+a tab  : Switch the input focus to the next regions
    Ctrl+a Ctrl+a: Toggle between the current and previous region 
    Ctrl+a Q    : Close all regions but the current one 
    Ctrl+q X    : Close the current region 

# Detach from Linux Screen Session 
$ Ctrl+a d  # detach from the screen session at any time typing 

# Reattach to a Linux Screen 
```

vim+tmux - OMG!Code
-------------------
* Why vim?
    - highly customizable 
    - runs everywhere 
    - works with many programming languages
    - scriptable
* Features 
    - Model editing 
```
Model editing 
    change the meaning of the keys in each mode of operation 
    -> Normal Mode - navigate the structure of the file
        1. Don't use arrow keys 
        2. Don't use the mouse 
        You're a programmer Strive to be lazy 
        h j k l - left up down right
        -> ^E - scroll the window down 
        -> ^Y - scroll the window up 
        -> ^F - scroll down one page 
        -> ^B - scroll up one page 
        -> H  - move cursor to the top of the window 
        -> M  - move cursor to the middle of the window 
        -> L  - move cursor to the bottom of the window 
        -> gg - go to top of file
        -> G  - go to bottom of file 
        The secret sauce 
            -> text objects and motions 
                Think of a file as more than individual characters 
                text objects 
                    -> w - words
                    -> e - end of word
                    -> s - sentences 
                    -> p - paragraphs 
                    -> t - tags 
                Motions 
                    -> a - all 
                    -> i - in 
                    -> t - 'til
                    -> f - find forward 
                    -> F - find backward
                Combine with commands 
                Commands
                    -> d - delete(also cut)
                    -> c - change(delete, then place in insert mode)
                    -> y - yank (copy)
                    -> v - visually select
                {command}{text object or motion}    
                    -> diw - delete in word 
                    -> caw - change all word
                    -> yi) - yank all text inside parentheses 
                        
            -> the DOT command 
            -> macros 
    -> Insert Mode - eidting the file 
    -> Visual Mode - highlight portions of the file to manipulate at once 
    -> Ex Mode - Command mode 
```
