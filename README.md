# Deetlist Scraper

The `deetlist` library is a Web Scraping library that works on the website "https://deetlist.com/dragoncity/" to extract data about Dragon City, such as events, dragons and game releases.

---

## Installation

### Using pypi:

```
pip install deetlist
```

### Using GitHub repository:

```
pip install git+https://github.com/1marcuth/deetlist.git
```

---

## Using

---

### Scraping Home page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_home_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'events': {'actives': [{'title': 'Starcrossedlovers Fog Island is now on!', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/fi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/fog/Starcrossedlovers'}, {'title': 'Heroic Race is now on!', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/hr.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/race/'}], 'upcoming': [{'title': 'Star-crossed  Maze Island coming soon', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/mi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/maze/star-crossed-'}, {'title': 'Arctic Tower Island coming soon', 'icon_url': 
'https://www.deetlist.com/dragoncity/img/event/ti.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/tower/Arctic'}, {'title': 'Puzzle Island coming soon', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/pi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/puzzle/star-crossed-'}]}}
```

---

### Scraping Events page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_events_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'events': {'actives': [{'title': 'Starcrossedlovers Fog Island is now on!', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/fi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/fog/Starcrossedlovers'}, {'title': 'Heroic Race is now on!', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/hr.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/race/'}], 'upcoming': [{'title': 'Star-crossed  Maze Island coming soon', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/mi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/maze/star-crossed-'}, {'title': 'Arctic Tower Island coming soon', 'icon_url': 
'https://www.deetlist.com/dragoncity/img/event/ti.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/tower/Arctic'}, {'title': 'Puzzle Island coming soon', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/pi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/puzzle/star-crossed-'}], 'past': [{'title': 'Runner Island has finished', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/ri.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/runner/Aquatic'}, {'title': 'Sweetrevenge Grid Island has finished', 'icon_url': 'https://www.deetlist.com/dragoncity/img/event/gi.png', 'page_url': 'https://www.deetlist.com/dragoncity/events/grid/Sweetrevenge'}]}}
```

---

### Scraping All Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_all_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'Nature Dragon', 'page_url': 'https://deetlist.com/dragoncity/dragon/Nature', 'image_url': 'https://deetlist.com/dragoncity/img/dragon/nature.png'}, {'name': 'Firebird Dragon', 'page_url': 'https://deetlist.com/dragoncity/dragon/Firebird', 'image_url': 'https://deetlist.com/dragoncity/img/dragon/firebird.png'}, {'name': 'Mercury Dragon', 'page_url': 'https://deetlist.com/dragoncity/dragon/Mercury', 'image_url': 'https://deetlist.com/dragoncity/img/dragon/mercury.png'}, {'name': 'Gummy Dragon', 'page_url': 'https://deetlist.com/dragoncity/dragon/Gummy', 'image_url': 'https://deetlist.com/dragoncity/img/dragon/gummy.png'}, {'name': 'Lantern Fish Dragon', 'page_url': 'https://deetlist.com/dragoncity/dragon/Lantern%20Fish', 'image_url': 'https://deetlist.com/dragoncity/img/dragon/lantern%20fish.png'}, {'name': 'Tropical Dragon', 'page_url': 'https://deetlist.com/dragonc
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/922262554087137341/1206587546025459752/data.json?ex=65dc8d38&is=65ca1838&hm=ba0f1d847a1ed3622e86c1bf453c573155c7250b12750f903e799b42a722447f&)

---

### Scraping New Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_new_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'Larimar Dragon', 'rarity': 'L', 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/larimar.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/larimar', 'released': 1707423}, {'name': 'Lotus Dragon', 'rarity': 'L', 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/lotus.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/lotus', 'released': 1707423}, {'name': 'Voyager Dragon', 'rarity': 'L', 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/voyager.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/voyager', 'released': 
1707423}, {'name': 'High Passion Dragon', 'rarity': 'H', 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high_passion.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/high_passion', 'released': 1707423}, {'name': 'Gigaguard Dragon', 'rarity': 'L', 'image_url': '
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/922262554087137341/1206587296665571369/data.json?ex=65dc8cfc&is=65ca17fc&hm=be1e1ff7a77572f0c049c352fb8fecda3687ca4b4fe21bb71cfe2cccaa2c19d7&)

---

### Scraping Heroic Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_all_heroic_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'High Fenrir Dragon', 'rarity': 'H', 'elements': ['ice', 'pure', 'war', 'electric'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20fenrir.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/high_fenrir'}, {'name': 'High Nucleus Dragon', 'rarity': 'H', 'elements': ['pure', 'metal', 'terra', 'nature'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20nucleus.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/high_nucleus'}, {'name': 'High Tension Dragon', 'rarity': 'H', 'elements': ['electric', 'war', 'metal', 'dark'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20tension.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/high_tension'}, {'name': 'High Guardian Dragon', 'rarity': 'H', 'elements': ['pure', 'ice', 'electric', 'dark'], 'image_url': 'https://www.deetlist.com/dra
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206606329498828821/data.json?ex=65dc9eb6&is=65ca29b6&hm=897637d24ea8003b5d8c2e1a03618d4c59d83b7e15398a949ea4e071bb830a95&)

---

### Scraping Breedable Legendary Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_breedable_legendary_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'Apocalypse Dragon', 'rarity': 'L', 'elements': ['flame', 'ice', 'light', 'dark'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/apocalypse.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/apocalypse'}, {'name': 'Millennium Dragon', 'rarity': 'L', 'elements': ['sea', 'war', 'terra', 'metal'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/millennium.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/millennium'}, {'name': 'Forge Dragon', 'rarity': 'L', 'elements': ['metal', 'terra', 'ice', 'flame'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/forge.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/forge'}, {'name': 'Promethium Dragon', 'rarity': 'L', 'elements': ['light', 'dark', 'nature', 'electric'], 
'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/promethium.png', 'page_
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206616555350401166/data.json?ex=65dca83c&is=65ca333c&hm=0a8402a2b50ce2435437e1af5999f2ebfbfaa9823be55b8e838b2917cd6c8d92&)

---

### Scraping Breedable Category 5 Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_breedable_category_5_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'Dujur Dragon', 'rarity': 'V', 'elements': ['flame', 'electric', 'ice'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/dujur.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/dujur'}, {'name': 'Master Dragon', 'rarity': 'E', 'elements': ['flame', 'sea', 'war'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/master.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/master'}, {'name': 'Greenfluid Dragon', 'rarity': 'E', 'elements': ['nature', 'sea', 'electric'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/greenfluid.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/greenfluid'}, {'name': 'Sylvan Dragon', 'rarity': 'E', 'elements': ['nature', 'war'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/sylvan.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/sylvan'}, {
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206618617542877284/data.json?ex=65dcaa28&is=65ca3528&hm=66eaa499a1a0c26d3e042789c05b6f91dfd413f374f2084acba9fb32e3d5b4a9&)

---

### Scraping Breedable Category 9 Dragons page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_breedable_category_9_dragons_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'Decay Dragon', 'rarity': 'L', 'elements': ['dark', 'terra', 'primal', 'metal'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/decay.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/decay'}, {'name': 'Quasar Dragon', 'rarity': 'L', 'elements': ['soul', 'electric', 'light', 'pure'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/quasar.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/quasar'}, {'name': 'Shapeshifter Dragon', 'rarity': 'L', 'elements': ['chaos', 'sea', 'dark', 'flame'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/shapeshifter.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/shapeshifter'}, {'name': 'Morpheus Dragon', 'rarity': 'L', 'elements': ['dream', 'pure', 'ice', 'sea'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/morpheus.png', 'page_url': 'http
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206618617542877284/data.json?ex=65dcaa28&is=65ca3528&hm=66eaa499a1a0c26d3e042789c05b6f91dfd413f374f2084acba9fb32e3d5b4a9&)

---

### Scraping Heroic Dragons Categorized by Attacks page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_heroic_dragons_categorized_by_attacks_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'dragons': [{'name': 'High Reborn Dragon', 'rarity': 'H', 'elements': ['pure', 'nature', 'light', 'sea'], 'attack': {'power': 0, 'rank': 1}, 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20reborn.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/High_Reborn'}, {'name': 'High Virago Dragon', 'rarity': 'H', 'elements': ['light', 'war', 'nature', 'electric'], 'attack': {'power': 0, 'rank': 2}, 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20virago.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/High_Virago'}, {'name': 'High Arcane Dragon', 'rarity': 'H', 'elements': ['magic', 'pure', 'electric', 'flame'], 'attack': {'power': 0, 'rank': 3}, 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20arcane.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/High_Arcane'}, {'name': 'High Frozen Dragon', 'rari
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206632276671336548/data.json?ex=65dcb6e0&is=65ca41e0&hm=d7de0b662b4ded423ce38683ed7bad8e9f781baa978556103c69517389db0642&)

---

### Scraping Elements page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_elements_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'elements': [{'name': 'terra', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/terra.png'}, {'name': 'flame', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/flame.png'}, {'name': 'sea', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/sea.png'}, {'name': 'nature', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/nature.png'}, {'name': 'electric', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/electric.png'}, {'name': 'ice', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/ice.png'}, {'name': 'metal', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/metal.png'}, {'name': 'dark', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/dark.png'}, {'name': 'light', 'image_url': 'https://www.deetlist.com/dragoncity/img/types/light.png'}, {'name': 'war', 'image_url': 'https://www.deetlist.com/dragoncity/img
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206637939199713300/data.json?ex=65dcbc26&is=65ca4726&hm=6d0f943a1363b1af456655b9c15d9a41bd1532c4fafc9ed8449d3440e52de6a4&)

---

### Scraping Element Tokens page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_element_tokens_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'element_tokens': [{'name': 'terra', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Terra_Token.png'}, {'name': 'flame', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Flame_Token.png'}, {'name': 'sea', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Sea_Token.png'}, {'name': 'nature', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Nature_Token.png'}, {'name': 'electric', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Electric_Token.png'}, {'name': 'ice', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Ice_Token.png'}, {'name': 'metal', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Metal_Token.png'}, {'name': 'dark', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Dark_Token.png'}, {'name': 'light', 'image_url': 'https://www.deetlist.com/dragoncity/img/tokens/Light_Token.png'},
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206643087447818292/data.json?ex=65dcc0f2&is=65ca4bf2&hm=8cd82fc6fba1d1b24a95d459525b99cd2f07026b5f4156003b723c4592db2d65&)

---

### Scraping Fog Islands page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_fog_islands_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'duration': 259200, 'pool': {'size': 666, 'time': 28800}, 'dragons': [{'name': 'Equinox Dragon', 'rarity': 'C', 'elements': ['dark', 'light'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/equinox.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/equinox'}, {'name': 'Fairy Dragon', 'rarity': 'R', 'elements': ['nature', 'ice'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/fairy.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/fairy'}, {'name': 'Vibrant Dragon', 'rarity': 'V', 'elements': ['electric', 'sea', 'flame'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/vibrant.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/vibrant'}, {'name': 'Side-t Dragon', 'rarity': 'E', 'elements': ['terra', 'sea', 'pure'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/side-t.png', 'page_url': 'https://www.d
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206657968406536192/data.json?ex=65dccece&is=65ca59ce&hm=db57a0b1037fe5e2b2eadc1ae0152e6bb5417668760f196c710cb83573c75415&)

---

### Scraping Heroic Races page data:

```python
from deetlist import Deetlist

deetlist = Deetlist()

data = deetlist.scrape_heroic_races_page()

print(data)
```

#### Running the code, you will get something like this:

```python
{'duration': 950400, 'dragons': [{'name': 'High Passion Dragon', 'rarity': 'H', 'elements': ['beauty', 'flame', 'electric', 'chaos'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/high%20passion.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/high_passion'}, {'name': 'Magicienne Dragon', 'rarity': 'L', 'elements': ['magic', 'dark', 'sea', 'nature'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/magicienne.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/magicienne'}, {'name': 'Rideable Dragon', 'rarity': 'E', 'elements': ['metal', 'ice', 'electric'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/rideable.png', 'page_url': 'https://www.deetlist.com/dragoncity/dragon/rideable'}, {'name': 'Wave Dragon', 'rarity': 'V', 'elements': ['sea', 'electric', 'light'], 'image_url': 'https://www.deetlist.com/dragoncity/img/dragon/
...}
```

[See complete example in json file](https://cdn.discordapp.com/attachments/917481610243354624/1206668207113510982/data.json?ex=65dcd857&is=65ca6357&hm=d1e2cb3c11a2c5edc0e95237c733666e52be4fd8315fd048d8754df26902909a&)

---

## Possible problems

- Some URLs of dragon images or pages may vary their word separators between `_` and `%20`, as I was unable to find a standard to correct this, it will be your role to carry out this validation when getting the image from the URL: If it doesn't work with one tab, try the other, but please be careful not to overload the Deetlist server!

## How to Contribute

If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a branch for your feature (`git checkout -b feature/MyFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/MyFeature`).
5. Create a new Pull Request.

## Author

Marcuth [@1marcuth](https://github.com/1marcuth)

## License

This project is licensed under the MIT License.