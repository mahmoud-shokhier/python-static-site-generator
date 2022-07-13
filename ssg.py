# import typer
from ssg.site import Site

config = {
    "source" : "source", 
    "dest": "dest",
}

Site(**config).build()