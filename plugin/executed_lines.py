import re


def executed_line_numbers(src_pathname):
    def was_executed(gcov_file_line):
        return bool(re.match('^\s*\d+:', gcov_file_line))

    def source_line_number(gcov_file_line):
        return int(re.match('^\s*\d+:\s*(\d+):', gcov_file_line).group(1))

    def source_line_text(gcov_file_line):
        return re.match('^\s*\d+:\s*\d+:(.*)', gcov_file_line).group(1)

    def gcov_filename(src_pathname):
        " convert pathname as per --preserve-paths gcov option. "
        return re.sub('/', '#', src_pathname)+'.gcov'

    def executed_lines_from_gcov_file(src_pathname):
        return [line for line in open(gcov_filename(src_pathname))
                if was_executed(line)
                and source_line_text(line) != '}' # I've seen gcov 4.7.3 claim such lines are executed (even at the end of functions that were never called)
                ]

    return [source_line_number(gcov_file_line) for gcov_file_line in executed_lines_from_gcov_file(src_pathname)]
