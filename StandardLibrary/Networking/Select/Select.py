'''
- provides accessto platform-specifc I/O monitoring functions,
- The most protable interface isthe POSIX function select(), which is available
on Unix and Windows.
- The module also includes poll(), a Unix-only API, and several options that
work only with specific variants of Unix.
'''