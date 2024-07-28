# Libgen Ebook Downloader

A CLI tool to search and download ebooks from Libgen.

## Table of Contents
- [Libgen Ebook Downloader](#libgen-ebook-downloader)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Run Locally](#run-locally)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)


## Description

Libgen Ebook Downloader is a command-line tool that allows users to search for and download ebooks from the Library Genesis (Libgen) website. It simplifies the process of finding and retrieving digital books.

This project uses a combination of Python's `requests` and `BeautifulSoup` libraries for web scraping to gather data from the Library Genesis (Libgen) website. Specifically, it employs a modified version of the [libgen-api](https://github.com/harrison-broadbent/libgen-api) library.


## Features

- Search in non-fiction and fiction books
- Download books
- Search in fields(Default *Title*) *Author*, *Publisher*, *Year* 


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


## Run Locally

Clone the project

```bash
  git clone https://github.com/KocakAli/libgen-cli.git
```

Go to the project directory

```bash
  cd libgen-cli
```

Install dependencies

```bash
  pip install .
```

Start the cli

```bash
  libgen-cli --help
```

## Contributing

Contributions are always welcome!

Whether you're fixing bugs, adding new features, improving documentation, or providing feedback, your help is appreciated.

## Authors

- [@kocakali](https://github.com/kocakali)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

