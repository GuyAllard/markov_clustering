from .mcl import *

try:
    from .drawing import *
except ImportError:
    print("Visualization not supported to missing libraries.")

__version_info__ = ("0", "0", "3", "dev")
__date__ = "28 Sep 2017"

__version__ = ".".join(__version_info__)
__author__ = "Guy Allard"
__contact__ = "guyallard01@gmail.com"
__homepage__ = "https://github.com/guyallard/markov_clustering.git"
