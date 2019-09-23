Mastering GNU Emacs
===================

> Emacs first written by Richard Stallman as a set of macros on top of another editor, called TECO, back in 1976.
> Emacs pulls you in. Once you start using Emcas for the editing, you realize that using Emcas for IRC, email, database access, command-line shells, compiling your code or surfing the Internet is just as easy as editing text - and you get to keep your key bindings, theme and all the power of Emacs and elisp to configure or alter the behavior of everything.
> Emacs is powered by its own LISP implementation called Emacs Lisp or just elisp. Every part of Emacs can be inspected, evaluated or modified because the editor is approximately 95 percent elisp and 5 percent C code.

* EMacs as an Operating System
```
When you run Emacs you are in fact launching a tiny C core responsible for the low-level interactions with your operating system's ABI. That includes mundane things like file-system and network access; drawing things to the screen or printing control codes to the terminal.

The cornerstons of Emacs though is the elisp interpreter -- without it, there is no Emacs.The interpreter is creaky and old; it's struggling. Modern Emacs users expect a lot from their humble interpreter: speed and asynchrony are the two main issues. The interpreter runs in a single thread and intensive tasks will lock the UI thread.

Emacs is a hacker's dream because it is one giant, mutable state. 

# A speech interface for the blind
    For 20 years, Emacs-peak has offered blind or visually impaired Emacs users a way of interacting with Emacs, and the world, through a speech interface that understands the content of what appears on your screen.

# Remote file editing
    Emacs's TRAMP seamlessly lets you edit remote files using a variety of network protocols, including SSH, FTP, rsync, and more, as though the files were local.

# Shell access
    Emacs has a built-in ANSI-capable Terminal emulator: an Emacs wrapper around shells, such as bash; and a full-blown shell called Eshell written entirely in elisp.

# ORG mode
    A to-do, agenda, project planner, literate programming, note-tasking (and more!) application. It is widely considered the best text-based organizer ever -- a feat only surpassed by the fact that people switch to Emacs just to use it.

# The Buffer
    In Emacs, all files are buffers, but not all buffers are files. The buffer will exist in Emacs and only Emacs. You have to explicitly save it to a file on disk to make it persist. In Emacs, the buffer is the data structure.

# The Window and the Frame
    In Emacs, a window is just a tiled portion of the frame. Each frame can have one or more windows, and each window can have exactly one buffer. so, a buffer must be viewed in a window in order to be displayed to the user, and for the window to be visible to the user it must be in a frame.

# The Point and Mark 
    The point is just another word for the _caret_ or _cursor_.

# Killing, Yanking and CUA 
    Killing is cutting, yanking is pasting, and copying is awkwardly known as saving to the kill ring (or just copy, informally.)

# .emacs.d, init.el, and .emacs 
    A favorite pastime of Emacs users is sharing with other Emacs hackers little snippets of code or customizations that make their lives easier.
    settings file: .emacs
    customizations in ~/.emacs.d/init.el; Since Emacs now writes several more files to your file system, they are kept in a directory called .emacs.d to avoid cluttering your home directory.

# Major Modes and Minor Modes 
    Major modes in Emacs control how buffers behave.
    Font Locking is the correct term for syntax high-lighting in Emacs, and in turn is made up of faces of properties (color, font, text size, and so on) that the font locking engines use to pretty-print the text.
```

* Getting started with Emacs 
```
# Checking Emacs's version 
$ emacs --version 

# Starting Emacs 
$ emacs -nw         # Forces Emacs to run in terminal mode 
$ emacs --help      # Display the help 
$ emacs -q          # Do not load an init file (such as init.el)
$ emacs -Q          # Does not load the site-wide startup file, your init file, nor X resources 
$ emacs --daemon    # run Emacs as a daemon

# Starting Emacsclient 
$ emacsclient --help 
$ emacsclient -c    # Creates a graphical frame (if X is available) or a terminal frame if X is unavailable.
$ emacsclient -nw   # Creates a terminal frame 
$ emacsclient -n    # The client will return immediately instead of waiting for you to save your changes

    The Emacs way is to keep it running and do all your edit-ing in a dedicated Emacs instance. Emacs will typically start slower than other editors(as it has a lot more packages and features) as it's designed for long-running sessions and not quick edits.

# Emacs Client-Server architecture 
    1. The Myriad advantages of Emacs's server mode:
        A persistent session: means Emacs will re-use the same session instead of spawning a new, distinct copy of Emacs every time.
        It works well with $EDITOR: opening the files in your shared Emacs session and automatically signalling the calling program when the session finishes.
        Fast file opening: from the command line using the _emacsclient_ binary. The Emacs client will connect to the local Emacs server instance and instruct it to open the file.

# A older joke is that Emacs stands for "Escape Meta Alt Control Shift"
# In Emacs, there are several modifier keys
C-      : Control 
M-      : Meta ("Alt" on most keyboards)
S-      : Shift
s-      : Super (not shift)
H-      : Hyper 
A-      : Alt(redundant and not used)
C-d     : calls a command named delete-char. To invoke it, hold down control and press d. As the key is a complete key, it will call the command delete-char and immediately delete the character next to point.
C-x     : prefix key 
C-x C-f : find-file 
C-x 8 P : insert the paragraph symbol ❡ 
C-M-%   : 
C-x #   : Save buffer 
F10     : access the menu bar 
```

* Discovering Emacs 

* Movement 

* Editing 

* Productivity 

* 
