from dcutils.dc_config import DRAGON_ELEMENTS_TYPES
from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
import httpx

class BreedableLegendaryDragonsPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/dragons/report/leg_breedable.php"

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_event(self, event_selector: Tag) -> dict:
        title_selector = event_selector.select_one(".ei")
        icon_selector = event_selector.select_one("img")
        icon_src = icon_selector.attrs["src"]

        title = title_selector.text.strip()
        icon_url = f"{self._base_url}/{icon_src}"
        page_url = f"{self._base_url}/{event_selector.attrs['href']}"

        return {
            "title": title,
            "icon_url": icon_url,
            "page_url": page_url
        }

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_dragon(self, dragon_selector: Tag) -> dict:
        name = dragon_selector.select_one(".nnam").text.strip()

        rarity = (dragon_selector
            .select_one(".img_rar")
            .attrs["class"][0]
            .removeprefix("img_rp_")
            .upper())

        elements = [
            DRAGON_ELEMENTS_TYPES[element_selector.attrs["id"].removeprefix("tb_")]
            for element_selector in dragon_selector.select(".typ_i")
        ]

        image_url = (dragon_selector
            .parent
            .attrs["href"]
            .replace("../../", f"{self._base_url}/img/")
            .lower()
            .replace("_", "%20")
            .replace(" ", "%20")) + ".png"

        page_url = (dragon_selector
            .parent
            .attrs["href"]
            .replace("../../", f"{self._base_url}/"))

        return {
            "name": name,
            "rarity": rarity,
            "elements": elements,
            "image_url": image_url,
            "page_url": page_url
        }

    def scrape(self) -> dict:
        response = httpx.get(self._url)
        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        dragon_selectors = soup.select(".over")
        
        return {
            "dragons": [ self._parse_dragon(dragon_selector) for dragon_selector in dragon_selectors ]
        }