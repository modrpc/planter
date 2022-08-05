" ignore case when searching
set ic 

" tab 
set tabstop=2 noexpandtab

" pathogen
" execute pathogen#infect()

" turn on syntax highlighting
syntax on

" syntax highlighting
" au BufRead,BufNewFile *.svh,*.sv,*.vh,*.v set filetype=verilog_systemverilog
" au BufRead,BufNewFile *.scala set filetype=java

" disable auto comment
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" set mouse=a

