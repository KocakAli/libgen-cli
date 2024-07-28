import typer
from typing_extensions import Annotated
from rich.console import Console
from rich.tree import Tree
from libgen_cli.api.libgen_search import LibgenSearch
from .utils import download_file, print_table
from . import constants

api = LibgenSearch()
console = Console()
results = None

# Download book with the given ID
def main(
        search_term: Annotated[str, typer.Argument(help="Search term, minumum 3 characters")],
        fiction: Annotated[bool, typer.Option(help="Search in fictional books category")] = False,
        only_links: Annotated[int, typer.Option(help="Gives only download links of the selected book and does not download it")] = None,
        d: Annotated[int, typer.Option(help="Download book with the given ID ")]=None,
        a: Annotated[bool, typer.Option(help="Search in author fields. Not possible with --fiction.")] = False,
        p: Annotated[bool, typer.Option(help="Search in publisher fields. Not possible with --fiction")] = False,
        y: Annotated[bool, typer.Option(help="Search in year fields. Not possible with --fiction")] = False,
    ):

    total_option = sum([a, p, y])
    if total_option > 1:
        console.print(
            "You can only use one of the options --t, --a or --y", style="bold on red")
        raise typer.Exit(code=1)

    
    search_type = None
    search_category = 1

    if a:
        search_type = "author"
    elif p:
        search_type = "publisher"
    elif y:
        search_type = "year"

    if fiction:
        search_category = 2
        cols_name = constants.FICT_TABLE_COLS
    else:
        cols_name = constants.NON_FICT_TABLE_COLS
    
    results = api.get_search_result(
        search_term, search_type=search_type, search_category=search_category)
    
    if d:
        download_links = api.resolve_download_links(results[d-1])
        download_file(download_links["GET"], results[d-1]["Title"], results[d-1]["Extension"])
        return
    elif only_links:
        download_links = api.resolve_download_links(results[only_links-1])
        for key, value in download_links.items():
            console.print(f"{key}: {value}")
        return
    else:
        console.rule(f"[red]Query: {search_term}")
        print_table(results, cols_name, search_category)
        return

def run():
    typer.run(main)

if __name__  == "__main__":
    run()


    
