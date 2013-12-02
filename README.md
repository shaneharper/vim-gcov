vim-gcov
========

Show executed statements ("coverage") of C/C++ programs.

vim-gcov may help to write high quality software quickly. It could be used with TDD ("Test Driven Development"), e.g.
* write a test case
* run test case
* if test failed, then the coverage information will highlight where a change may need to be made to fix a bug (or to add a missing feature).

("Program slicing" may be more useful - the output from gcov may include lines that had no effect on the program's output for a particular test run.)

Often people think of running a coverage tool to determine how comprehensive their test suite is. vim-gcov can also be used for this purpose.


vim-gcov is easy to install using Vundle.
