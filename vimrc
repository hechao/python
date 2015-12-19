:set noswapfile

set nocompatible " required
filetype off " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin("~/some/path/here")

" let Vundle manage Vundle, required
Bundle "gmarik/Vundle.vim"

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)

"set nu

Bundle "scrooloose/syntastic"
Bundle "nvie/vim-flake8"
Bundle "Valloric/YouCompleteMe"
Bundle "vim-scripts/indentpython.vim"

let python_highlight_all=1
syntax on

set background=dark
set foldmethod=indent
set foldlevel=99
 
" press space to fold/unfold code
nnoremap <space> za
vnoremap <space> zf


" All of your Plugins must be added before the following line
call vundle#end() " required
filetype plugin indent on " required
