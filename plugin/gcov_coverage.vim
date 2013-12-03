highlight ExecutedLineSignText ctermbg=Blue ctermfg=Black guibg=#0000EA guifg=Black

 " linehl can also be specified when defining a sign to highlight entire line, however, other syntax highlighting will then not be applied to the line.
sign define executed text=>> texthl=ExecutedLineSignText

let s:this_plugin_directory = escape(expand('<sfile>:p:h'), '\"')
exe 'python import sys; sys.path += ["' . s:this_plugin_directory . '"]'


python <<
import executed_lines

def highlight_executed_lines():
    import os

    def create_fold_if_needed(last_line_number, line_number):
        if line_number > last_line_number + 2:
            vim.command(':'+str(last_line_number+1)+','+str(line_number)+'fold')

    last_line_number = 0
    for sign_id, line_number in enumerate(executed_lines.executed_line_numbers_generator(os.path.basename(vim.current.buffer.name)), start=1): # XXX can basename always be used? What happens if source file is in a sub-directory?
        vim.command('exe ":sign place '+str(sign_id)+' line='+str(line_number)+' name=executed file=".expand("%:p")')
        create_fold_if_needed(last_line_number, line_number-1)
        last_line_number = line_number

    create_fold_if_needed(last_line_number,
                          int(vim.eval("line('$')"))  # (last line number of buffer)
                          )
.


autocmd FileType c,cpp python highlight_executed_lines()
