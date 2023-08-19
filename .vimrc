" set relative line numbers for easier vim motions
set relativenumber

" syntax highlighting
syntax on

" highlight line under cursor horizontally
set cursorline

" set shift width to 2 spaces
set shiftwidth=2

" set tab width to 2 spaces
set tabstop=2

" use spaces instead of tabs
set expandtab

" incremental search highlighting
set incsearch

" set highlighting when searching
set hlsearch

" autocompletion mode when pressing tab
set wildmenu

" Clear status line when vimrc is reloaded.
set statusline=

" Status line left side.
set statusline+=\ %F\ %M\ %Y\ %R

" Use a divider to separate the left side from the right side.
set statusline+=%=

" Status line right side.
set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%

" Show the status on the second to last line.
set laststatus=2
