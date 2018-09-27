from .mcl import *
from .modularity import *

try:
    from .drawing import *
except ImportError:
    print("Visualization not supported to missing libraries.")

__version_info__ = ("0", "0", "4", "dev")
__date__ = "28 Sep 2017"

__version__ = ".".join(__version_info__)
__author__ = "Guy Allard, Jona Harris, Mounir Mallek"
__contact__ = "guyallard01@gmail.com"
__homepage__ = "https://github.com/guyallard/markov_clustering.git"
