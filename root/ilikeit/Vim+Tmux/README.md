# Oh-My-Zsh+Vim+Tmux OMG!

## Oh-My-Zsh + Bullet Train Theme 

Requirements:

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

6. Enabling Plugins
$ vim ~/.zshrc
plugins=(
    extract
    git 
    zsh-autosuggestions
)
```

## Vim 

### Vim setup instructions

1. Download Vim 

```
# If you're on a mac, you can get the latest vim from Homebrew.
$ brew install macvim --override-system-vim 
```

2. Create a vimrc 

```
# Create a vim configuration file in your home directory and a vim/bundle directory 
$ wget  https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/vimrc -O ~/.vimrc 
$ mkdir -p ~/.vim/bundle 
```

3. Add vundle (Vundle, the plug-in manager for Vim)

```
# Vundle is short for Vim bundle and is a Vim plugin manager.
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim 
```

4. Configure Plugins:

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

5. Install Plugins
```
Launch vim and run :PluginInstall
To install from command line: 
$ vim +PluginInstall +qall
```

- [.vimrc](/root/ilikeit/Vim+Tmux/vimrc)


## Tmux 

### Installation 

Requirements:
	1. tmux **>= 2.1** running inside Linux, Mac, OpenBSD 
	2. outside of tmux, $TERM must be set to **xterm-256color**
	3. check tmux Version $ tmux -V

To install, run the following from your terminal: (you may want to backup your existing ~/.tmux.conf first)

```
$ mv .tmux.conf .tmux.conf.old 
$ wget https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/tmux.conf -O .tmux.conf
$ wget https://raw.githubusercontent.com/chyidl/chyidlTutorial/master/root/ilikeit/Vim%2BTmux/tmux.conf.local -O .tmux.conf.local 
```

### Features

1. C-a acts as secondary prefix, while keeping default C-b prefix 
2. visual theme inspired by Powerline 
3. maximize any pane to a new window with <prefix> + 
4. SSH aware username and hostname status line information 
5. mouse mode toggle with <prefix> m 
6. automatic usage of **reattach-to-user-namespace** if available 
7. laptop battery status line information 
8. uptime status line information 
9. optional highlight of focused pane (tmux >= 2.1)
10. configurable new windows and panes behavior (optionally retain current path)
11. SSH aware split pane (reconnects to remote server, expermental)
12. copy to OS clipboard (needs **reattach-to-user-namespace** on macOS, xsel or xclip on Linux)
13. Urlview integration if available 

The "maximize any pane to a new window with <prefix> +" feature is different from builtin **resize-pane -Z** as it allows you to further split a maximzed pane. It's also more flexible by allowing you to maximize a pane to a new window, then change window, then go back and the pane is still in maximized state in its own window. You can then minimize a pane by using **<prefix> +** either from the source window or the maximized window.

**Mouse mode** allows you to set the active window, set the active pane, resize panes and automatically switches to copy-mode to select text. 

### Bindings

tmux may be controlled from an attached client by using a key combination of a prefix key, followed by a command key. This configuration uses C-a as a secondary prefix while keeping C-b as the default prefix. In the following list of key bindings: 

1. <prefix> means you have to either hit **Ctrl + a** or **Ctrl + b**
2. <prefix> c means you have to hit **Ctrl + a** or **Ctrl + b** followed by **c**
3. <prefix> C-c means you have to hit **Ctrl + a** or **Ctrl + b** followed by **Ctrl + c**

This configuration uses the following bindings:

1. <prefix> e opens **~/.tmux.conf.local** with the editor defined by the $EDITOR environment variables (defaults to vim when empty)
2. **<prefix> r** reloads the configuration
3. **C-l** clears both the screen and the tmux history 
4. <prefix> C-c creates a new session 
5. <prefix> C-f lets you switch another session by name 
6. <prefix> C-h and <prefix> C-l let you navigate windows (default <prefix> n and <prefix> p are unbound)
7. <prefix> Tab brings you to the last active window 
8. <prefix> - splits the current pane vertically 
9. <prefix> | splits the current pane horizontally 
10. <prefix> h, <prefix> j, <prefix> k and <prefix> l let you navigate panes ala Vim 
11. <prefix> H, <prefix> J, <prefix> K, <prefix> L let you resize panes
12. <prefix> < and <prefix> > let you swap panes 
13. <prefix> + maximizes the current pane to a new window 
14. <prefix> U launches Urlview (if availabele)
15. <prefix> F launches Facebook PathPicker (if available)
16. <prefix> Enter enters copy-mode 
17. <prefix> b lists the paste-buffers 
18. <prefix> p pastes from the top paste-buffer 
19. <prefix> P lets you choose the paste-buffer to paste from 

Bindings for **copy-mode-vi**

	1. **v** begins selection / visual mode 
	2. **C-v** toggles between blockwise visual mode and visual mode 
	3. **H** jumps to the start of line 
	4. **L** jumps to the end of line 
	5. **y** copies the selection to the top paste-buffer 
	6. Escape cancels the current operation

### Configuration 

Instead of altering the **~/.tmux.conf** file and diverging from upstream, the proper way is to edit the **~/.tmux.conf.local** file. 

Pressing **<prefix> e** will open **~/.tmux.conf.local** with the editor defined by the **$EDITOR** environment variable (defaults to vim when empty)

**Enabling the Powerline look**

To make use of these symbols, use you preferred font along with the Powerline font. Then edit the **~/.tmux.conf.local** file (<prefix> e) and adjust the following variables:

```
tmux_conf_theme_left_separator_main = 
tmux_conf_theme_left_separator_sub = 
tmux_conf_theme_right_separator_main = 
tmux_conf_theme_right_separator_sub = 
```
**Configuring the status line**

Edit the **~/.tmux.conf.local** file (<prefix> e) and adjsut the **tmux_conf_theme_status_left** and **tmux_conf_theme_status_right** variables to your own preferences.

This is configuration supports the following buitin variables:

```
#{battery_bar} : horizontal battery charge bar 
#{battery_percentage} : battery percentage 
#{battery_status}: is battery charging or discharging 
#{battery_vbar}: vertical battery charge bar 
#{circle_session_name}: circled session number, up to 20 
#{hostname}: SSH aware hostname information 
#{hostname_ssh}: SSH aware hostname information, blank when no SSH connection detected 
#{loadavg}: load average 
#{pairing}: is session attached to more than one client
#{prefix}: is prefix being depressed 
#{root}: is current user root
#{synchronzied}: are the panes synchronized
#{uptime_d}: uptime days 
#{uptime_h}: uptime hours
#{uptime_m}: uptime minutes
#{uptime_s}: uptime seconds 
#{username}: SSH aware username information 
#{username_ssh}: SSH aware username information, blank when no SSH connection detected
```

**Accessing the macOS clipboard from with tmux sessions**

Chris johnsen created the [**reattach-to-user-namespace** utility](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard) that makes **pbcopy** and **pbpaste** work again within tmux.

To install **reattach-to-user-namespace**, Once installed, reattach-to-usernamespace will be automatically detected.
```
$ brew install reattach-to-user-namespace 
```

### tmux shortcuts & cheatsheet 

```
$ tmux					# start new  
$ tmux new -s name		# start new with session name 
$ tmux a				# attch 
$ tmux a -t myname		# attach to named 
$ tmux ls				# list sessions 
$ tmux kill-session -t myname # kill session 
$ tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill  # kill all the tmux sessions 

Sessions 
:new <CR> new session 
<prefix> s	# list sessions 
<prefix> $ name session 

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

- [.tmux.conf](/root/ilikeit/Vim+Tmux/tmux.conf)
- [.tmux.conf.local](/root/ilikeit/Vim+Tmux/tmux.conf.local)
- [tmux-spotify-info](/root/ilike/Vim+Tmux/tmux-spotify-info)
- [tmux-spotify-info](/root/ilike/Vim+Tmux/tmux-itunes-info)
![tmux music info](/imgs/ilikeit/Vim+Tmux/tmux-itunes-info.png?raw=true)


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
