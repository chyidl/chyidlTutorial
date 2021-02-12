VIM
===
> Vim a highly configurable text editor for effieciently creating and changing any kind of text. It is included as "vi" with most UNIX systems and with Apple OS X.
> Vim is rock stable and is continuously being developed to become even better. Among its features are:

```
# 1. Why vim?
    highly customizable
    runs everywhere
    works with many programming language
    scriptable

(macOS)
$ brew install macvim --with-override-system-vim --with-python3 --with-lua

```

Getting Started
---------------

* Search and replace
```
https://vim.fandom.com/wiki/Search_and_replace

Vim provides the :s (substitute) command for search and replace.
The :substitute command searches for a text pattern, and replaces it with a text string.
    :%s/foo/bar/g
        - Find each occurrence of 'foo' (in all lines), and replace it with 'bar'.
    :s/foo/bar/g
        - Find each occurrence of 'foo' (in the current line only), and replace it with 'bar'.
    :%s/foo/bar/gc
        - Change each 'foo' to 'bar', but ask for confirmation first.
    :%s/\<foo\>/bar/gc
        - Change only whole words exactly matching 'foo' to 'bar'; ask for confirmation
    :%s/foo/bar/gci
        - Change each 'foo' (case insensitive due to the i flag) to 'bar';ask for confirmation.
    :%s/foo/bar/gcI
        - Change each 'foo'(case sensitive due to the I flag) to 'bar';ask for confirmation
    The g flag means global - each occurrence in the line is changed
```

VIM Tips
--------
- [Entering special characters in VIM](/root/ilikeit/vim/VimTipsWiki/Tip_51_Entering_special_characters.md)
- [Insert current date or time in VIM](/root/ilikeit/vim/VimTipsWiki/Tip_97_Insert_current_date_or_time.md)

Install Vim 8 with Python Ruby Lua
----------------------------------
```
# remove current vim
sudo apt-get remove --purge vim vim-runtime vim-tiny

# removes current link for vim
sudo rm -rf /usr/local/share/vim /usr/bin/vim

# installs everything needed to make/configure/build vim
sudo apt-get -y install python3-dev

# so vim cam be uninstalled again via 'dpkg -r vim'
sudo apt-get install checkinstall

# clones vim repository so we can build it from scratch
cd ~
git clone https://github.com/vim/vim
cd vim
git pull && git fetch

# In case Vim was already installed. This can throw an error if not installed.
# it's the normal behaviour. That's no need to worry about it
cd src
make distclean
cd ..

# update to use the correct python3.x config path also change
./configure \
--enable-multibyte \
--enable-perlinterp=dynamic \
--enable-python3interp \
--with-python3-config-dir=/usr/bin/python3 \
--enable-fontset \
--enable-largefile \ 
--enable-fail-if-missing

# this is the compilation step. It should also create the symlink of the binary one /usr/bin folder
make && sudo make install

# To be able to access the new vim instaltion we need to refresh bash/zsh/fish
```
