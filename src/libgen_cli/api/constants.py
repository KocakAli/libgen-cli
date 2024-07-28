CATEGORIES = {
    1 : 'non-fiction',
    2 : 'fiction'
}


LINKS = {
    1 : 'https://libgen.is/search.php?req={}&res{}&column={}',
    2 : 'https://libgen.is/fiction/?q={}'
}

NON_FICTION_COLS = [
    "ID",
    "Author",
    "Title",
    "Publisher",
    "Year",
    "Pages",
    "Language",
    "Size",
    "Extension",
    "Mirror_1",
    "Mirror_2",
    "Mirror_3",
    "Mirror_4",
    "Mirror_5",
    "Edit",  
]

FICTION_COLS = [
    "Author",
    "Series",
    "Title",
    "Language",
    "Extension",
    "Size",
    "Mirror_1",
    "Mirror_2",
    "Mirror_3",
    "Mirror_4",
    "Mirror_5",
    "Edit"
]
# print(LINKS['default'].format('python'))