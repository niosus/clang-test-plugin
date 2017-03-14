""" Usage: call with <filename>
"""
import sys
import platform
from os import path
sys.path.append(path.dirname(__file__))
from clang import cindex38
from clang import cindex40_old
from clang import cindex40_new
from clang import utils

# cindex = cindex38      # works
# cindex = cindex40_new  # works
cindex = cindex40_old  # fails

ClangUtils = utils.ClangUtils
filename = path.abspath(path.join(path.dirname(__file__), "test.cpp"))

if len(sys.argv) > 1:
  clang_binary = sys.argv[1]
else:
  clang_binary = 'clang++'

clang_dir = ClangUtils.find_libclang_dir(clang_binary)
if not cindex.Config.loaded:
    cindex.Config.set_library_path(clang_dir)
print("Clang directory = ", clang_dir)
print("libclang lib = ", path.join(cindex.Config.library_path,
                                   ClangUtils.libclang_name))
print("Platform: ", platform.architecture())
print("Python version: ", platform.python_version())
clang_flags = ['-x', 'c++', '-std=c++11']
index = cindex.Index.create()
index.parse(path=filename, args=clang_flags)
del index
