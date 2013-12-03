#!/usr/bin/env python

# Test executed_lines.executed_line_numbers_generator()


import unittest
import subprocess
import executed_lines


class TestBase(unittest.TestCase):
    def assert_coverage(self,
                        annotated_source_code # a list of 2-tuples:
                        # 1st element of each tuple indicates whether the line is expected to be executed or not,
                        # 2nd element is the line text (without new-line).
                       ):
        def expected_executed_line_numbers():
            return {line_number for line_number, annotated_line in enumerate(annotated_source_code, start=1) if annotated_line[0]}
        def line_numbers_to_ignore():
            return {line_number for line_number, annotated_line in enumerate(annotated_source_code, start=1) if annotated_line[0] is None}

        with open('test.cpp', 'w') as f:
            f.write('\n'.join([line for cov, line in annotated_source_code]))

        subprocess.call(['g++ -g -O0 -fprofile-arcs -ftest-coverage test.cpp -o test && rm -f test.gcda && ./test && gcov -o. --relative-only --preserve-paths test.cpp'], shell=True)

        self.assertEqual(expected_executed_line_numbers(),
                         {line_number for line_number in executed_lines.executed_line_numbers_generator('test.cpp')} - line_numbers_to_ignore())


class Test(TestBase):
    def test_multi_line_statement(self):
        # Rationale: gcov outputs a count for only the first line of a multi-line statement.
        self.assert_coverage([
            (True,  "int main(int argc, char**)"),
            (True,  "{"),
            (True,  "    if ("),
            (True,  "        argc"),
            (True,  "        > 0"),
            (True,  "    )"),
            (True,  "    {"),
            (True,  "        return 0;"),
            (None,  "    }"),
            (False, "    return -1;"),
            (None,  "}")
        ])

    # XXX test_optimised_away_statement
        # Rationale: gcov won't output a count for, e.g. "if (1 + 1 == 2)"


if __name__ == "__main__":
    unittest.main()
