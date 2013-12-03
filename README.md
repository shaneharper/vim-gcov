vim-gcov
========

VIM plugin to show executed statements ("coverage") of C/C++ programs.

vim-gcov may aid writing high quality software quickly. It can be used with TDD ("Test Driven Development"):
* write a test case
* run test case
* if test failed, then the coverage information will aid the developer to see where a change may need to be made to fix a bug (or add a missing feature).

([Wikipedia](http://http://en.wikipedia.org/wiki/Program_slicing) ("Program slicing") may be more useful - the output from gcov may include lines that had no effect on the program's output for a particular test run.)

Often people run a coverage tool to determine how comprehensive their test suite is. vim-gcov can also be used for this purpose.


vim-gcov is easy to install using Vundle.
