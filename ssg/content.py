import re 
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
    
    # @classmethod
    # def load(cls, string):
        