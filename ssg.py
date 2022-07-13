import typer
from ssg.site import Site

def main():
    config = {
        "source" : "source", 
        "dest": "dest",
    }

    Site(**config).build()
    typer.run()
    
if __name__ == "__main__":
    main()