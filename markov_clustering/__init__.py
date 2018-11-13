import sys
from .mcl import *
from .modularity import *

try:
    from .drawing import *
except ImportError:
    sys.stderr.write("Visualization not supported to missing libraries.\n")

__version_info__ = ("0", "0", "5", "dev")
__date__ = "13 Nov 2018"

__version__ = ".".join(__version_info__)
__author__ = "Guy Allard, Jona Harris, Mounir Mallek"
__contact__ = "guyallard01@gmail.com"
__homepage__ = "https://github.com/guyallard/markov_clustering.git"
