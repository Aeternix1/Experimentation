"This is my vimrc file

"================== PLUGINS ======================================

set nocompatible
filetype plugin indent on

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim  
call vundle#begin()

"let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

"Added nerdtree
Plugin 'scrooloose/nerdtree'

"Added Nerd Commenter
Plugin 'scrooloose/nerdcommenter'

"Installing Goyo
Plugin 'junegunn/goyo.vim'

"Lightline Plugin
Plugin 'itchyny/lightline.vim'

"Vim Table Mode <leader>tm
Plugin 'dhruvasagar/vim-table-mode'

"Vim Indent Guides
Plugin 'nathanaelkane/vim-indent-guides'

"Vim Git Gutter
Plugin 'airblade/vim-gitgutter'

"Vim EasyMotion <leader><leader>w
Plugin 'easymotion/vim-easymotion'

"Control P Fuzzy File Finder
Plugin 'ctrlpvim/ctrlp.vim'

"Colorschemes for vim
"Plugin 'flazz/vim-colorschemes'

"Multiple cursors
Plugin 'terryma/vim-multiple-cursors'

"HTML and Javascript line completer
Plugin 'mattn/emmet-vim'

"Autosave for vim
Plugin 'vim-scripts/vim-auto-save'

"YoucompleteMe
"Plugin 'Valloric/YouCompleteMe'

"Gruvbox
Plugin 'morhetz/gruvbox'


"All of your Plugins must be added before the following line 
call vundle#end()
filetype plugin indent on 


"========================= SETTINGS ================================


"System Administration
:let mapleader = "," "Change the leader to , 

"Colors
syntax enable "enable syntax processing
set t_Co=256
set background=dark
set relativenumber
colorscheme gruvbox

"Spaces & Tabs 
set tabstop=4 "number of visual spaces per TAB
set shiftwidth=4 "when indenting with >, use 4 space width
set softtabstop=4 "allows for backspacing TABS
set expandtab "tabs are spaces
set textwidth=80
set wrap linebreak
set autoindent

"Tab settings for different Filetypes
autocmd FileType html setlocal shiftwidth=2 softtabstop=2 tabstop=2 expandtab

"UI Configs
set number "show line number"
set showcmd "show command in bottom bar
set cursorline "highlight current line
set laststatus=2 "status line is always on

set wildmenu "visual autocomplete for command menu
set wildmode=longest:full,full "
set showmatch "highlight matching [{()}]
set spelllang=en_us "sets spell checking to English

"/search\c - search case insensitive
"/search\C - search case sensitive 

set incsearch "search characters as entered
set hlsearch "hl search
set ignorecase "searching is not case specific
set smartcase "When a search has an uppercase don't be case specific
"Close down the search
nnoremap <leader><SPACE> :nohlsearch<CR>  
"Copying from the outside
set clipboard=unnamed
:se mouse+=a

"Rebinding easymotion to <leader>w
map <Leader> <Plug>(easymotion-prefix)

"Needed to make YouComplete Me Work with C
let g:ycm_global_ycm_extra_conf = 'path to .ycm_extra_conf.py'

"Open nerdtree on opening vim
"autocmd VimEnter * NERDTree

"Open nerdTree to bookmarks when opening vim 
let NERDTreeShowBookmarks=1

"Enable indent guides on vim startup
let g:indent_guides_enable_on_vim_startup = 1  
let g:indent_auto_colors = 1 
let g:indent_guides_guide_size = 1
let g:indent_guides_start_level = 2

" Autosave when text is changed
autocmd TextChanged,TextChangedI <buffer> silent write


"Change the default mapping and the default command to invoke CtrlP
let g:ctrlp_map = '<c-p>' 
let g:ctrlp_cmd = 'CtrlP'
let g:ctrlp_working_path_mode = 'ra'
"Enable Autosave on Vim startup
let g:auto_save = 1 



"Important Vim Commands
"Folding -> zf 

"Search and replace
":l1,l2s/two/VIM/gc <between lines l1, l2>
":l1,l2s/two/VIM/gic <between lines l1, l2, case insensitive> 
":%s/two/VIM/gc in the entire document
":%s/two/VIM/gic <the entire document, case insensitive> 
":%s//replace/g  replace the last search

"l1,l2s/\<to\>/XX/gic <only finds the two in the doc>

