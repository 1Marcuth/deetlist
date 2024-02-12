from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
import httpx

class AllDragonsPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/all-dragons/"

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_dragon(self, dragon_selector: Tag) -> dict:
        name = dragon_selector.select_one(".drag").text

        page_url = (dragon_selector
            .attrs["href"]
            .replace("../", f"{self._base_url}/")
            .replace(" ", "%20"))

        image_url = (dragon_selector
            .attrs["href"]
            .replace("../", f"{self._base_url}/img/")
            .lower()
            .replace(" ", "%20")) + ".png"

        return {
            "name": name,
            "page_url": page_url,
            "image_url": image_url
        }

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

        dragon_selectors = soup.select("a:has(.drag)")
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
            "dragons": [ self._parse_dragon(dragon_selector) for dragon_selector in dragon_selectors ],
            "events": {
                "actives": active_events,
                "upcoming": upcoming_events
            }
        }