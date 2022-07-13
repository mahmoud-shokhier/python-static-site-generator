import typer
from ssg.site import Site

def main():
    config = {
        "source" : "source", 
        "dest": "dest",
    }

    Site(**config).build()
    
    
if __name__ == "__main__":
    typer.run(main)