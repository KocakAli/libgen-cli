# Libgen Ebook Downloader

A CLI tool to search and download ebooks from Libgen.


## Description

Libgen Ebook Downloader is a command-line tool that allows users to search for and download ebooks from the Library Genesis (Libgen) website. It simplifies the process of finding and retrieving digital books.

This project uses a combination of Python's `requests` and `BeautifulSoup` libraries for web scraping to gather data from the Library Genesis (Libgen) website. Specifically, it employs a modified version of the [libgen-api](https://github.com/harrison-broadbent/libgen-api) library.


## Installation
```bash
    pip3 install libgen-downloader
```
or
```bash
    pip install libgen-downloader
```

## Usage

```
$ libgen-cli --help

Usage: libgen-cli [OPTIONS] SEARCH_TERM

Arguments: 
    *    search_term [required] TEXT        Search term, minumum 3 characters   


Options: 

    --fiction --no-fiction                  Search in fictional books category

    --only-links    INTEGER                 Gives only download links of the selected book 
                                            and does not download it
    
    -d              INTEGER                 Download book with the given ID
    
    -a                                      Search in author fields. Not possible with --fiction
    
    -p                                      Search in publisher fields. Not possible with --fiction
    
    -y                                      Search in year fields. Not possible with --fiction
    
    --help                                  show help
```

## Examples

Search and Download Example 
![Search and Download Example ](https://github.com/KocakAli/libgen-cli/blob/main/Images/example.gif)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

