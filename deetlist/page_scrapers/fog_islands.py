from dcutils.dc_config import DRAGON_ELEMENTS_TYPES
from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
from datetime import timedelta
import httpx

class FogIslandsPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/events/fog/"

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_dragon(self, dragon_selector: Tag) -> dict:
        name = (dragon_selector
            .select_one(".pan_ic")
            .text
            .strip())

        rarity = (dragon_selector
            .select_one(".img_rar")
            .attrs["class"][0]
            .removeprefix("img_rp_")
            .upper())
        
        elements = [
            DRAGON_ELEMENTS_TYPES[element_selector.attrs["class"][1].removeprefix("tb_")]
            for element_selector in dragon_selector.select(".typ_i")
        ]

        image_url = (dragon_selector
            .select_one(".pan_img")
            .attrs["src"]
            .replace(" ", "%20")
            .replace("../../", f"{self._base_url}/"))

        page_url = (dragon_selector
            .select_one(".aitm a")
            .attrs["href"]
            .replace(" ", "%20")
            .replace("../../", f"{self._base_url}/"))

        return {
            "name": name,
            "rarity": rarity,
            "elements": elements,
            "image_url": image_url,
            "page_url": page_url
        }

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_duration(self, duration_selector: Tag) -> int:
        duration = int(
            int(duration_selector
                .text
                .strip()
                .removeprefix("This event lasts ")
                .removesuffix(" days")
            ) * timedelta(days = 1).total_seconds()
        )

        return duration

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

        max_points_per_collection = max_points_per_collection = int(soup.select_one(".tkn_hold div b").text)

        dragon_selectors = soup.select(".over")
        duration_selector = soup.select_one(".dur_text")
        current_events_header_selector = soup.find("h3", class_ = "see_ev ev_evs")
        upcoming_events_header_selector = soup.find("h3", class_ = "see_ev ev_upc")
        current_event_selectors = current_events_header_selector.find_next_siblings("a", attrs = { "class": "eata" })
        upcoming_event_selectors = upcoming_events_header_selector.find_next_siblings("a", attrs = { "class": "eata" })

        active_events = [ self._parse_event(event_selector) for event_selector in current_event_selectors ]
        upcoming_events = [ self._parse_event(event_selector) for event_selector in upcoming_event_selectors ]

        active_events = list(
            filter(lambda event: not event in upcoming_events, active_events)
        )

        duration = self._parse_duration(duration_selector)

        pool_time = int(timedelta(hours = 8).total_seconds())

        pool_size = int(
            (max_points_per_collection / (duration / timedelta(days = 1).total_seconds())) *
            (pool_time / timedelta(days = 1).total_seconds())
        )

        return {
            "duration": duration,
            "pool": {
                "size": pool_size,
                "time": pool_time
            },
            "dragons": [ self._parse_dragon(dragon_selector) for dragon_selector in dragon_selectors ],
            "events": {
                "actives": active_events,
                "upcoming": upcoming_events
            }
        }