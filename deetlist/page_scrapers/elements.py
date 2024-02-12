from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
import httpx

class ElementsPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/elements/"

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_element(self, element_selector: Tag) -> dict:
        name = (element_selector
            .text
            .strip()
            .lower())

        image_url = (element_selector
            .select_one(".elm_hold img")
            .attrs["src"]
            .replace("../", f"{self._base_url}/"))

        return {
            "name": name,
            "image_url": image_url
        }

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_table_image(self, image_selector: Tag) -> str:
        image_url = image_selector.attrs["src"].replace("../", f"{self._base_url}/")
        return image_url

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

    def scrape(self) -> dict:
        response = httpx.get(self._url)
        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        element_selectors = soup.select(".emel")
        table_image_selector = soup.select_one(".big-im")
        current_events_header_selector = soup.find("h3", class_ = "see_ev ev_evs")
        upcoming_events_header_selector = soup.find("h3", class_ = "see_ev ev_upc")
        current_event_selectors = current_events_header_selector.find_next_siblings("a", attrs = { "class": "eata" })
        upcoming_event_selectors = upcoming_events_header_selector.find_next_siblings("a", attrs = { "class": "eata" })

        active_events = [ self._parse_event(event_selector) for event_selector in current_event_selectors ]
        upcoming_events = [ self._parse_event(event_selector) for event_selector in upcoming_event_selectors ]

        active_events = list(
            filter(lambda event: not event in upcoming_events, active_events)
        )

        return {
            "elements": [ self._parse_element(element_selector) for element_selector in element_selectors ],
            "table_image_url": self._parse_table_image(table_image_selector),
            "events": {
                "actives": active_events,
                "upcoming": upcoming_events
            }
        }