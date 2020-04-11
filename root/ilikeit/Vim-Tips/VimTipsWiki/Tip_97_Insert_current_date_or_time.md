Insert current date or time
---------------------------

> There are a variety of ways to insert a data/time stamp. You can even have Vim automatically update an existing 'last modified' data/time when writing the file.

* Using strftime()
```
    Vim's internal strftime() function(:help strftime()) returns a data/time string formatted in a way you specify with a format string.Most systems support strftime(), but some don't.
    To insert a timestamp in the default strftime format "%c", type either of the following commands:
        :put = strftime(\"%c\")
        :put = strftime('%c')
        Mon Sep 23 15:39:34 2019
    To store the return value of the function, the "= register (:help "=) is used.
    Press F6 in normal or in insert mode to insert the current datestramp :help i_CTRL-R 
        add below command to ~/.vimrc 
            nnoremap <F6> "=strftime("%c")<CR>P         // The uppercase P at the end inserts before the current character, which allows datestramps inserted at the beginning of an existing of an existing line. Other 'put' commands may be more userful for you:help p :help P :help gp :help gP
            inoremap <F6> <C-R>=strftime("%c")<CR>
    Type dts in insert mode to expand to a datestamp :help abbreviations using an expression :help :map-expression 
        iab <expre> dts strftime("%c")
    To replace text with the current date in a substitute command:
        :s/text to replace/\=strftime("%c")/
```

* Using external tools
```
    On Unix-based systems, enter the following in Vim to read the output from running the date utility, inserting the result after the current line:
        :r !date
    Under Windows, use:
        :r !date /t 
    The above commands insert the output of the date program after the current line. If wanted, the !! command can be used to filter the current line, replacing it with the output of date.
```
