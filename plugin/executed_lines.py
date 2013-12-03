import re

gcov_line_re = re.compile('^\s*([^:]+):\s*(\d+):(.*)')


def executed_line_numbers_generator(src_pathname):
    def gcov_filename(src_pathname):
        " convert pathname as per --preserve-paths gcov option. "
        return re.sub('/', '#', src_pathname)+'.gcov'

    was_line_executed = False
    for line in open(gcov_filename(src_pathname)):
        execution_count, line_number, line_text = gcov_line_re.match(line).groups()

        if line_text.strip():  # XXX ideally test if line contains executable statements, not just that it is not blank
            was_line_executed = (False if execution_count == '#####'
                                 else
                                 was_line_executed if execution_count == '-' # handle multi-line statement, for which execution count is output only for first line
                                 else
                                 # assume execution_count is a number
                                 True)

            if was_line_executed:
                yield int(line_number)  # XXX consider returning "runs" of executed line numbers... e.g. (1,4) instead of 1, 2, 3, 4
