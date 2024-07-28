import requests
from tqdm import tqdm
from rich.table import Table
from rich.console import Console

# Example usage
# download_file("https://example.com/file", "myfile", "txt")
def download_file(url, filename, extension):
    """
    Downloads a file from a given URL.
    """
    try:
        full_filename = filename + "." + extension
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        total_size = int(response.headers.get('content-length', 0))

        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(full_filename.strip(), "wb") as file:
                for data in response.iter_content(1024):
                    progress_bar.update(len(data))
                    file.write(data)
        
        print("Download completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the download: {e}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
# print_table(results, cols_name, search_category)
def print_table(results, cols_name, search_category):
    """
    Prints a table of search results.
    """
    table = Table(show_lines=True, style="white")
    for col_data in cols_name:
        table.add_column(col_data[0], max_width=col_data[1], style="green")

    if search_category == 1:
        for index, item in enumerate(results):
            item_list = list(item.values())
            new_list = [str(index + 1)] + item_list[1:3] + item_list[4:9]
            table.add_row(*new_list)
    else:
        for index, item in enumerate(results):
            item_list = list(item.values())
            new_list = [str(index + 1)] + item_list[0:6]
            table.add_row(*new_list)
    
    console = Console()
    console.print(table)


