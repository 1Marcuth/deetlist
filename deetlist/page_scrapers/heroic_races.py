from dcutils.dc_config import DRAGON_ELEMENTS_TYPES
from datetime import timedelta, datetime
from bs4 import BeautifulSoup, Tag
from pydantic import validate_call
import httpx

SECONDS_PER_DAY = timedelta(days = 1).total_seconds()
SECONDS_PER_MINUTE = timedelta(minutes = 1).total_seconds()
SECONDS_PER_HOUR = timedelta(hours = 1).total_seconds()
MINUTES_PER_HOUR = SECONDS_PER_HOUR / 60

class HeroicRacesPageScraper:
    VALIDATE_CONFIG = dict(arbitrary_types_allowed = True)

    @validate_call(config = VALIDATE_CONFIG)
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._url = f"{base_url}/events/race/"

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
    def _parse_spawn_time(self, pool_time: str) -> int:
        pool_time = pool_time.lower()

        if pool_time == "instant" or pool_time == "no minimum":
            return 0
        
        if "minutes" in pool_time:
            if "60" in pool_time:
                return int(60 * SECONDS_PER_MINUTE)
                
            minutes = datetime.strptime(pool_time, "%M minutes").minute
            return int(minutes * SECONDS_PER_MINUTE)

        elif "hours" in pool_time:
            hours = datetime.strptime(pool_time, "%H hours").hour
            return int(hours * SECONDS_PER_HOUR)

        elif "hr" in pool_time and "min" in pool_time:
            hours_and_minutes = datetime.strptime(pool_time, "%Hhr %Mmin")
            hours = hours_and_minutes.hour
            minutes = hours_and_minutes.minute

            return int((hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE))

        elif "day" in pool_time:
            days_and_hours = datetime.strptime(pool_time, "%d day %H hrs")
            days = days_and_hours.day
            hours = days_and_hours.hour
            return int((days * SECONDS_PER_DAY) + (hours * MINUTES_PER_HOUR))

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_mission_type(self, mission_title: str) -> str:
        mission_types = {
            "Feed Dragons": "feed",
            "Collect Food": "food",
            "Collect Gold": "gold",
            "Battle Dragons": "fight",
            "Breed Dragons": "breed",
            "Hatch Eggs": "hatch",
            "League Battles": "pvp"
        }

        if mission_title in mission_types:
            return mission_types[mission_title]

        return mission_title

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_mission(self, mission_selector: Tag) -> dict:
        mission_type = self._parse_mission_type(mission_selector.select_one(".mh").text)
        goal_points = int(mission_selector.select_one(".mz:nth-child(1) .m2").text)
        pool_size = int(mission_selector.select_one(".mz:nth-child(2) .m2").text)

        collect_chance = int(mission_selector.select_one(".mz:nth-child(4) .m2").text.removesuffix("%")) / 100
        spawn_time_for_one = self._parse_spawn_time(mission_selector.select_one(".mz:nth-child(3) .m2").text)
        spawn_time_for_all = self._parse_spawn_time(mission_selector.select_one(".mz:nth-child(5) .m2").text)

        return {
            "type": mission_type,
            "goal_points": goal_points,
            "pool_size": pool_size,
            "spawn_time": {
                "one": spawn_time_for_one,
                "all": spawn_time_for_all
            },
            "collect_chance": collect_chance
        }

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_node(self, node_selector: Tag) -> list[dict]:
        mission_selectors = node_selector.select(".ml")
        missions = [ self._parse_mission(mission_selector) for mission_selector in mission_selectors ]
        return missions

    @validate_call(config = VALIDATE_CONFIG)
    def _parse_lap(self, lap_selector: Tag) -> dict:
        node_selectors = lap_selector.select(".nn")

        return {
            "nodes": [ self._parse_node(node_selector) for node_selector in node_selectors ]
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

        dragon_selectors = soup.select(".over")
        lap_selectors = soup.select(".hl")
        duration_selector = soup.select_one(".dur_text")

        duration = self._parse_duration(duration_selector)

        return {
            "duration": duration,
            "dragons": [ self._parse_dragon(dragon_selector) for dragon_selector in dragon_selectors ],
            "laps": [ self._parse_lap(lap_selector) for lap_selector in lap_selectors ]
        }