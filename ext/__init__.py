# Adapted from https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
# Allows Python files to be dropped in here
# This is not secure, and it's not meant to be. Don't let people write arbitrary code in this directory!

# TODO: refactor

from .actions.tplink import switch_state
from .actions.misc import wait_seconds

funcs = {
    "tplink.switch_state": switch_state,
    "wait_seconds": wait_seconds
}

# from os.path import dirname, basename, isfile, join
# from inspect import getmembers, isfunction, ismodule
# from itertools import chain
# lchain = lambda x: list(chain(x))

# import glob

# def recursive_function_find(mod) -> list[callable]:
#     mods, fns = getmembers(mod, ismodule), getmembers(mod, isfunction)
#     print(mods, fns)
#     fns = lchain([recursive_function_find(nxt_mod) for nxt_mod in mods])
    
#     return fns



# module_paths = glob.glob(join(dirname(__file__), "*.py"))



# import importlib.util
# import sys

# def load_mod(path):
#     spec = importlib.util.spec_from_file_location("module.name", path)
#     foo = importlib.util.module_from_spec(spec)
#     sys.modules["module.name"] = foo
#     return foo

# modules = [load_mod(path) for path in module_paths]

# funcs = lchain([recursive_function_find(mod) for mod in modules])
# print(funcs)

# # __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

