""" Usage: call with <filename>
"""
import sys
import platform
from os import path
sys.path.append(path.dirname(__file__))
from clang import cindex40
from clang import utils

cindex = cindex40
ClangUtils = utils.ClangUtils
filename = path.abspath(path.join(path.dirname(__file__), "test.cpp"))
clang_dir = ClangUtils.find_libclang_dir("clang++")
if not cindex.Config.loaded:
    cindex.Config.set_library_path(clang_dir)
print("Clang directory = ", clang_dir)
print("Platform: ", platform.architecture())
print("Python version: ", platform.python_version())
