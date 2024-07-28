import requests
from bs4 import BeautifulSoup
from .constants import * 
from typing import List

# WHY
# The SearchRequest module contains all the internal logic for the library.
#
# This encapsulates the logic,
# ensuring users can work at a higher level of abstraction.

# USAGE
# req = search_request.SearchRequest("[QUERY]", search_type="[title]")


class SearchRequest:

    def __init__(self, query, search_type="title", search_category=1, result_count=25):
        self.query = query
        self.search_type = search_type
        self.search_category = search_category
        self.result_count = result_count

        if len(self.query) < 3:
            raise Exception("Query is too short")

    def strip_i_tag_from_soup(self, soup):
        subheadings = soup.find_all("i")
        for subheading in subheadings:
            subheading.decompose()



    ## fix that shit for fiction books add new function or something
    def get_search_page(self):
        
        if self.search_category == 1:
            query_parsed = "%20".join(self.query.split(" "))
            search_url = str(LINKS[self.search_category]).format(query_parsed, self.result_count, self.search_type)
        elif self.search_category ==2:
            query_parsed = "+".join(self.query.split(" "))
            search_url = str(LINKS[self.search_category]).format(query_parsed)
        search_page = requests.get(search_url)
        return search_page

    def scrape_non_fiction(self,soup) -> List[dict]:
        """
            scrap all rows data from soup non-fiction category
            and return a list of dictionaries
        """
        raw_data = []
        information_table = soup.find_all("table")[2]

        for row in information_table.find_all("tr")[1:]:
            row_data = []
            
            for td in row.find_all("td"):
                if td.find("a") and td.find("a").has_attr("title") and td.find("a")["title"] != "":
                    row_data.append(td.a["href"])
                else:
                    row_data.append("".join(td.stripped_strings))
                
            raw_data.append(row_data)

        output_data = [dict(zip(NON_FICTION_COLS, row)) for row in raw_data]
        return output_data

    def scrape_fiction_page(self,soup) -> List[dict]:
        """
            scrap all rows data from soup fiction category
            and return a list of dictionaries
        """
        raw_data = []
        information_table = soup.find_all("table")[0]

        for row in information_table.find_all("tr")[1:]:
            row_data = []
            
            for td in row.find_all("td"):
                if td.find("ul", {"class": "record_mirrors_compact"}):
                    for a in td.find("ul", {"class": "record_mirrors_compact"}).find_all("a"):
                        row_data.append(a["href"])
                elif td.find("ul") and td.find("ul").has_attr("class"):
                    row_data.append(",".join([a.text for a in td.find_all("a")]))
                elif td.has_attr("title"):
                    extension = td.text.split("/")[0]
                    size = td.text.split("/")[1]
                    row_data.append(extension)
                    row_data.append(size)
                else:                    
                    row_data.append("".join(td.stripped_strings))

            raw_data.append(row_data)

        output_data = [dict(zip(FICTION_COLS, row)) for row in raw_data]
        return output_data
    
    
    def aggregate_request_data(self,search_category):
        search_page = self.get_search_page()
        soup = BeautifulSoup(search_page.text, "html.parser")
        self.strip_i_tag_from_soup(soup)
        
        if search_category == 1:
            return self.scrape_non_fiction(soup=soup)
        elif search_category == 2:
            return self.scrape_fiction_page(soup=soup)
            
            
        return None