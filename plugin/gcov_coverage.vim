highlight ExecutedLineSignText ctermbg=Blue ctermfg=Black guibg=#0000EA guifg=Black

 " linehl can also be specified when defining a sign to highlight entire line, however, other syntax highlighting will then not be applied to the line.
sign define executed text=>> texthl=ExecutedLineSignText

let s:this_plugin_directory = escape(expand('<sfile>:p:h'), '\"')
exe 'python import sys; sys.path += ["' . s:this_plugin_directory . '"]'


python <<
import executed_lines

def highlight_executed_lines():
    import os

    for sign_id, line_number in enumerate(executed_lines.executed_line_numbers(os.path.basename(vim.current.buffer.name))): # XXX can basename always be used? What happens if source file is in a sub-directory?
        vim.command('exe ":sign place '+str(sign_id+1)+' line='+str(line_number)+' name=executed file=".expand("%:p")')
.


autocmd FileType c,cpp python highlight_executed_lines()
