from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
import httpx

class ElementTokensPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/tokens/"

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_element_token(self, element_selector: Tag) -> dict:
        name = (element_selector
            .text
            .strip()
            .lower()
            .removesuffix(" tokens"))

        image_url = (element_selector
            .select_one(".elm_hold img")
            .attrs["src"]
            .replace("../", f"{self._base_url}/"))

        return {
            "name": name,
            "image_url": image_url
        }

    def scrape(self) -> dict:
        response = httpx.get(self._url)
        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        element_token_selectors = soup.select(".emel")

        return {
            "element_tokens": [ self._parse_element_token(element_token_selector) for element_token_selector in element_token_selectors ]
        }