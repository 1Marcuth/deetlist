from .page_scrapers.home import HomePageScraper
from .page_scrapers.events import EventsPageScraper
from .page_scrapers.all_dragons import AllDragonsPageScraper
from .page_scrapers.new_dragons import NewDragonsPageScraper
from .page_scrapers.all_heroic_dragons import AllHeroicDragonsPageScraper
from .page_scrapers.breedable_legendary_dragons import BreedableLegendaryDragonsPageScraper
from .page_scrapers.breedable_category_5_dragons import AllBreedableCategory5DragonsPageScraper
from .page_scrapers.breedable_category_9_dragons import AllBreedableCategory9DragonsPageScraper
from .page_scrapers.heroic_dragons_categorized_by_attacks import HeroicDragonsCategorizedByAttacksPageScraper
from .page_scrapers.elements import ElementsPageScraper
from .page_scrapers.element_tokens import ElementTokensPageScraper
from .page_scrapers.fog_islands import FogIslandsPageScraper
from .page_scrapers.heroic_races import HeroicRacesPageScraper

class Deetlist:
    _base_url = "https://www.deetlist.com/dragoncity"

    def __init__(self) -> None:
        ...

    def scrape_home_page(self) -> dict:
        scraper = HomePageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_events_page(self) -> dict:
        scraper = EventsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_all_dragons_page(self) -> dict:
        scraper = AllDragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_new_dragons_page(self) -> dict:
        scraper = NewDragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_all_heroic_dragons_page(self) -> dict:
        scraper = AllHeroicDragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_breedable_legendary_dragons_page(self) -> dict:
        scraper = BreedableLegendaryDragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_breedable_category_5_dragons_page(self) -> dict:
        scraper = AllBreedableCategory5DragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_breedable_category_9_dragons_page(self) -> dict:
        scraper = AllBreedableCategory9DragonsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_heroic_dragons_categorized_by_attacks_page(self) -> dict:
        scraper = HeroicDragonsCategorizedByAttacksPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_elements_page(self) -> dict:
        scraper = ElementsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_element_tokens_page(self) -> dict:
        scraper = ElementTokensPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_fog_islands_page(self) -> dict:
        scraper = FogIslandsPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_heroic_races_page(self) -> dict:
        scraper = HeroicRacesPageScraper(self._base_url)
        data = scraper.scrape()
        return data

    def scrape_maze_islands_page(self) -> dict:
        ...

    def scrape_grid_islands_page(self) -> dict:
        ...

    def scrape_runner_islands_page(self) -> dict:
        ...

    def scrape_tower_islands_page(self) -> dict:
        ...

    def scrape_puzzle_islands_page(self) -> dict:
        ...

    def scrape_dragon_page(self, url_or_name: str) -> dict:
        ...