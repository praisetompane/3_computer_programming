"""This makes the combine folder a package(module)"""

from combine.functions.number_funcs import *
from combine.functions.string_funcs import *

#generate unified interface for the combine package
__all__ = (functions.number_funcs.__all__ + functions.string_funcs.__all__)