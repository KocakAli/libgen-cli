from .search_request import SearchRequest
import requests
from bs4 import BeautifulSoup
from typing import List

MIRROR_SOURCES = ["GET", "Cloudflare", "IPFS.io", "Infura"]


class LibgenSearch:

    def __init__(self) -> None:
        pass

    def get_search_result(self, query, search_type="title", search_category=1, result_count=25):
        """
            Search for a query in the specified search_type.

            search_type can be:
                - title
                - author
                - publisher
                - series
                - year
                - ISBN
                - language
        """
        search_request = SearchRequest(query, search_type=search_type, search_category=search_category, result_count=result_count)

        return search_request.aggregate_request_data(search_category=search_category)
    
    

    def search_filtered(self, query, filters, search_type, exact_match=True):
        search_request = SearchRequest(query, search_type=search_type)
        results = search_request.aggregate_request_data()
        filtered_results = filter_results(
            results=results, filters=filters, exact_match=exact_match
        )
        return filtered_results
    
    def resolve_download_links(self, item):
        mirror_1 = item["Mirror_1"]
        page = requests.get(mirror_1)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", string=MIRROR_SOURCES)
        download_links = {link.string: link["href"] for link in links}
        return download_links


def filter_results(results, filters, exact_match):
    """
    Returns a list of results that match the given filter criteria.
    When exact_match = true, we only include results that exactly match
    the filters (ie. the filters are an exact subset of the result).

    When exact-match = false,
    we run a case-insensitive check between each filter field and each result.

    exact_match defaults to TRUE -
    this is to maintain consistency with older versions of this library.
    """

    filtered_list = []
    if exact_match:
        
        for result in results:
            # check whether a candidate result matches the given filters
            if filters.items() <= result.items():
                filtered_list.append(result)

    else:
        filter_matches_result = False
        for result in results:
            for field, query in filters.items():
                if query.casefold() in result[field].casefold():
                    filter_matches_result = True
                else:
                    filter_matches_result = False
                    break
            if filter_matches_result:
                filtered_list.append(result)
    return filtered_list

    
