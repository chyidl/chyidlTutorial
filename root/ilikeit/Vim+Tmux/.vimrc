" #  >> Copyright 2018- chyidl (@Chyi Yaqing)

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
Plugin 'vim-scripts/mru.vim'    " Plugin to manage Most Recently Used (MRU) files 
Plugin 'scrooloose/nerdtree'    " A Tree explore plugin for Vim
Plugin 'Xuyuanp/nerdtree-git-plugin'    " A Plugin of NERDTree showing git status 
Plugin 'junegunn/goyo.vim'      " Distraction-free writing in Vim 
Plugin 'mileszs/ack.vim'        " Vim Plugin for the Perl module / CLI script 'ack'
Plugin 'ctrlpvim/ctrlp.vim'     " Active fork of kien/ctrlp.vim—Fuzzy file, buffer, mru, tag, etc finder. 
Plugin 'itchyny/lightline.vim'  " A light and configurable statusline/tabline plugin for Vim
Plugin 'MarcWeber/vim-addon-mw-utils' "
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'    " snipMate.vim aims to be a concise vim script that implements some of TextMate's snippets features in Vim 
Plugin 'w0rp/ale'               " Asynchronous linting/fixing for Vim and Language Server Protocol (LSP) integration
Plugin 'vim-syntastic/syntastic' " Syntax checking hacks for vim
Plugin 'keith/swift.vim'        " Vim runtime files for Swift


call vundle#end()               " required

"
"  Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" BASIC  
" Sections:
" 	-> General 
" 	-> VIM user interface 
" 	-> Colors and Fonts
" 	-> Files and backups
" 	-> Text, Tab and indent related 
" 	-> Visual mode related 
" 	-> Moving around, tabs and buffers
" 	-> Status line
" 	-> Editong mappings
" 	-> vimgrep searching and cope displaying 
" 	-> Spell checking 
" 	-> Misc 
" 	-> Helper functions 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Sets how many lines of history VIM has to remember 
set history=500

" Set number line 
set nu

" Enable filetype plugins 
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on

" Set to auto read when a file is changed from the outside 
set autoread 

" With a map leader it's possible to do extra key combinations 
" like <leader>w saves the current file 
let mapleader = ","

" Fast saving 
nmap <leader>w :w!<cr>

" :W sudo saves the file 
" (useful for handling the permission-denied error)
command W w !sudo tee % > /dev/null


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => VIM user interface 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Set 7 lines to the cursor - when moving vertically using j/k 
set so=7


" Avoid grabled characters in Chinese Language windows OS
let $LANG='en'
set langmenu=en
source $VIMRUNTIME/delmenu.vim 
source $VIMRUNTIME/menu.vim 

" Turn on the Wild menu 
set wildmenu 

" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
	set wildignore+=.git\*,.hg\*,.svn\*
else
	set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif

" Always show current position 
set ruler

" Height of the command bar 
set cmdheight=2

" A buffer becomes hidden when it is abandoned
set hid 

" Configure backspace so it acts as it should act 
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" Ignore case when searching 
set ignorecase 

" Highlight search results 
set hlsearch 

" Makes search act like search in modern browsers
set incsearch 

" Don't redraw while executing macros (good performance config)
set lazyredraw 

" For regular expressions turn magic on 
set magic 

" Show matching brackets when text indicator is over them 
set showmatch 

" How many tenths of a second to blink when matching brackets
set mat=2

" No annoying sound on errors 
set noerrorbells
set novisualbell 
set t_vb=
set tm=500

" Properly disable sound on errors on MacVim 
if has("gui_macvim")
	autocmd GUIEnter * set vb t_vb=
endif

" Add a bit extra margin to the left 
set foldcolumn=1


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Enable syntax highlighting 
syntax enable 

" Enable 256 colors palette in Gnome Terminal 
if !has('gui_running')
	set t_Co=256
endif

set background=dark

" Set extra options when running in GUI mode 
if has("gui_running")
	set guioptions-=T
	set guioptions-=e
	set t_Co=256
	set guitablabel=%M\ %t
endif

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8

" Use Unix as the standard file type
set ffs=unix,dos,mac

try
    color desert
    " highlight the current line and the cursor
    
    set cursorline
    set cursorcolumn

    highlight CursorColumn guibg=lightblue ctermbg=lightgray
    highlight CursorLine cterm=NONE ctermbg=lightgray ctermfg=NONE
catch
endtry

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Files, backups and undo
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Turn backup off, since most stuff is in SVN, git et.c anyway...
set nobackup
set nowb
set noswapfile


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Use spaces instead of tabs 
set expandtab 

" Be smart when using tabs ;)
set smarttab

" 1 tab == 4 spaces 
set shiftwidth=4
set tabstop=4

" Linebreak on 500 characters 
set lbr
set tw=500

set ai "Auto indent 
set si "Smart indent 
set wrap "Wrap lines


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Visual mode related 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Visual mode pressing * or # searches for the current selection 
" Super useful! From an idea by Michael Naumann 
vnoremap <silent> * :<C-u>call VisualSelection('', '')<CR>/<C-R>=@/<CR><CR>
vnoremap <silent> # :<C-u>call VisualSelection('', '')<CR>?<C-R>=@/<CR><CR>


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Moving around, tabs, windows and buffers 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Map<Space> to / (search) and Ctrl-<Space> to ? (backwards search)
map <space> /
map <c-space> ?

" Disable highlight when <leader><cr> is pressed 
map <silent> <leader><cr> :noh<cr>

" Smart way to move between windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" Close the current buffer 
map <leader>bd :Bclose<cr>:tabclose<cr>gT 

" Close all the buffers 
map <leader>ba :bufdo bd<cr>
map <leader>l :bnext<cr>
map <leader>h :bprevious<cr>

" Useful mappings for managing tabs 
map <leader>tn :tabnew<cr>
map <leader>to :tabonly<cr>
map <leader>tc :tabclose<cr>
map <leader>tm :tabmove
map <leader>t<leader> :tabnext

" Let 'tl' toggle between this and the last accessed tab 
let g:lasttab = 1
nmap <leader>tl :exe "tabn ".g:lasttab<CR>
au TabLeave * let g:lasttab = tabpagenr() 

" Opens a new tab with the current buffer's path 
" Super useful when editing files in the same directory 
map <leader>te :tabedit <c-r>=expand("%:p:h")<cr>/

" Switch CWD to the directory of the open buffer 
map <leader>cd :cd %:p:h<cr>:pwd<cr>

" Specify the behavior when switching between buffers 
try
    set switchbuf=useopen,usetab,newtab
    set stal=2
catch
endtry

" Return to the last edit position when opening files (You want this!)
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif 


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Status line
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Always show the status line 
set laststatus=2

" Format the status line 
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l\ \ Column:\ %c


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Editing mappings
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Remap VIM 0 to first non-blank character 
map 0 ^

" Move a line of text using ALT+[jk] or Command+[jk] on mac 
nmap <M-j> mz:m+<cr>`z
nmap <M-k> mz:m-2<cr> `z 
vmap <M-j> :m'>+<cr>`<my`>mzgv`yo`z
vmap <M-k> :m'<-2<cr>`>my`<mzgv`yo`z

if has("mac") || has("macunix")
    nmap <D-j> <M-j>
    nmap <D-k> <M-k>
    vmap <D-j> <M-j>
    vmap <D-k> <M-k>
endif 

" Delete trailing white space on save, useful for some filetype ;)
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun 

if has("autocmd")
    autocmd BufWritePre *.txt,*.js,*.py,*.wiki,*.sh,*.coffee :call CleanExtraSpaces()
endif 


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Spell checking 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Pressing ,ss will toggle and untoggle spell checking 
map <leader>ss :setlocal spell!<cr>

" Shortcuts using <leader>
map <leader>sn ]s 
map <leader>sp [s
map <leader>sa zg 
map <leader>s? z= 


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Misc
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Removing the Windows ^M - when the encodings gets messed up 
noremap <Leader>m mmHmt:%s/<C-V><cr>//get<cr>'tzt'm

" Quickly open a buffer for scribble 
map <leader>q :e ~/buffer<cr>

" Quickly open a markdown buffer for scribble 
map <leader>x :e ~/buffer.md<cr>

" Toggle paste mode on and off 
map <leader>pp :setlocal paste!<cr>


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Helper functions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Returns true if paste mode is enabled 
function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    endif
    return ''
endfunction

" Don't close window, when deleting a buffer 
command! Bclose call <SID>BufcloseCloseIt()
function! <SID>BufcloseCloseIt()
    let l:currentBufNum = bufnr("%")
    let l:alternateBufNum = bufnr("#")

    if buflisted(l:alternateBufNum)
        buffer #
    else
        bnext
    endif

    if bufnr("%") == l:currentBufNum
        new
    endif

    if buflisted(l:currentBufNum)
        execute("bdelete! ".l:currentBufNum)
    endif
endfunction 

function! CmdLine(str)
    call feedkeys(":" . a:str)
endfunction

function! VisualSelection(direction, extra_filter) range 
    let l:saved_reg = @"
    execute "normal! vgvy"

    let l:pattern = escape(@", "\\/.*'$^~[]")
    let l:pattern = substitute(l:pattern, "\n$", "", "")

    if a:direction == 'gv'
        call CmdLine("Ack '" . l:pattern . "' ")
    elseif a:direction == 'replace'
        call CmdLine("%s" . '/'. l:pattern . '/')
    endif

    let @/ = l:pattern 
    let @" = l:saved_reg
endfunction


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => FILETYPES
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Shell Section 
if exists('$TMUX')
    if has('mvim')
        set termguicolors
    else
        set term=screen-256color
    endif
endif

" Python section 



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => PLUGINS CONFIG
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" MRU Plugin Config 
"
" The Most Recently Used (MRU) plugin provides an easy access to a list of
" recently opened/edited files in Vim. This plugin automatically stores the 
" file names as you open/edit them in Vim. 
"
" To list and edit files from the MRU list, you can use the ':MRU' command.
" The ':MRU' command displays the MRU file list in a temporary Vim Window.
map <leader>f :MRU<CR>
"
" By default, the plugin will remember the names of the last 100 used files.
" You can set the 'MRU_Max_Entries' variable to remember more file namess.
let MRU_Max_Entries = 100

" NERDTree Plugin Config
"
" The NERDTree is a file system explorer for the Vim editor. Using this 
" plugin, users can visually browse complex directory hierarchies
" quickly open files for reading or editing, and perform basic file system
" operations.
" 
" Open NERDTree when start vim with no command line arguments
autocmd StdinReadPre * let s:std_in=1
autocmd vimenter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
"
" Open and Close NERDTree 
map <leader>nn :NERDTreeToggle<cr>
"
" Quickly perform operations with NERDTreeFind
map <leader>nf :NERDTreeFind<cr>
"
" automatically close NERDTree When you open a file
let NERDTreeQuitOnOpen = 1
"
" automatically delete the buffer of the file just deleted with NERDTree
let NERDTreeAutoDeleteBuffer = 1
let g:NERDTreeWinPos = "left"
let NERDTreeShowHidden=0
let NERDTreeIgnore = ['\.pyc$','__pycache__']
let g:NERDTreeWinSize=35

" NERDTree-git Plugin Config 
"
" A plugin of NEERDTree showing git status flags.
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ 'Ignored'   : '☒',
    \ "Unknown"   : "?"
    \ }

" CTRL-P Plugin Config 
" Full path fuzzy file, buffer, mru, tag,...finder for Vim 
"
" mapping command to invoke CtrlP
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
"
" CtrlP working directory according to this variable
let g:ctrlp_working_path_mode = 0   " disable this feature 
let g:ctrlp_max_height = 20
"
" open it again in a new pane instead of switching to the existing pane 
let g:ctrlp_switch_buffer = 'et'
"
" if custom listing command is being used, exclusions are ignored
set wildignore+=*/tmp/*,*.so,*.swp,*.zip    " MacOSX/Linux 
set wildignore+=*\\tmp\\*,*.swp,*.zip,*.exe " Windows 
let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn)$'
let g:ctrlp_custom_ignore = {
    \   'dir':  '\v[\/]\.(git|hg|svn)$',
    \   'file': '\v\.(exe|so|dll)$',
    \   'link': 'some_bad_symbolic_clinks',
    \   }

" lightline Plugin Config 
"
" A light and configurable statusline/tabline plugin for Vim 
"
" Colorscheme configuration. using wombat colorscheme
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ }
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ ['mode', 'paste'],
      \             ['fugitive', 'readonly', 'filename', 'modified'] ],
      \   'right': [ [ 'lineinfo' ], ['percent'] ]
      \ },
      \ 'component': {
      \   'readonly': '%{&filetype=="help"?"":&readonly?"🔒":""}',
      \   'modified': '%{&filetype=="help"?"":&modified?"+":&modifiable?"":"-"}',
      \   'fugitive': '%{exists("*fugitive#head")?fugitive#head():""}'
      \ },
      \ 'component_visible_condition': {
      \   'readonly': '(&filetype!="help"&& &readonly)',
      \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
      \   'fugitive': '(exists("*fugitive#head") && ""!=fugitive#head())'
      \ },
      \ 'separator': { 'left': ' ', 'right': ' ' },
      \ 'subseparator': { 'left': ' ', 'right': ' ' }
      \ }

" snipMate Plugin Config 
"
" snipMate.vim aims to be a concise vim script that implements some of TextMate's snippets features in Vim 
" SnipMate aims to provide support for textual snippets, similar to TextMate or other Vim Plugins like UltiSnips.
"
" show available snips by default bound to <C-R><Tab>in insert model
ino <c-j> <c-r>=snipMate#TriggerSnippet()<cr>
snor <c-j> <esc>i<right><c-r>=snipMate#TriggerSnippet()<cr>

" ALE (Asynchronous Lint Engine) Plugin Config 
"
" Asynchronous Lint Engine is a plugin for providing linting in Vim 8 while you edit your text files,
" and acts as a Vim Language Server Protocol client.
"
" By default, all available tools for all supported languages will be run.
" If you want to only select a subset of the tools, you can define. g:ale_linters globally
"

" Syntastic Plugin Config 
" Syntax checking hacks for vim 
" Recommanded settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" swift.vim Plugin Config 
" Vim runtime files for Swift 
let g:syntastic_swift_checkers = ['swiftpm', 'swiftlint']

" Using template files in Vim 
if has("autocmd")
    augroup templates
        autocmd BufNewFile *.* silent! execute '0r ~/.vim/templates/skeleton.'.expand("<afile>:e")
        autocmd BufNewFile * %substitute#\[:VIM_EVAL:\]\(.\{-\}\)\[:END_EVAL:\]#\=eval(submatch(1))#ge 
    augroup END
endif
