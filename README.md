[![Build Status](https://travis-ci.org/Demotivated/fxiv_lodestone.svg?branch=master)](https://travis-ci.org/Demotivated/fxiv_lodestone) [![Coverage Status](https://coveralls.io/repos/Demotivated/fxiv_lodestone/badge.svg?branch=master&service=github)](https://coveralls.io/github/Demotivated/fxiv_lodestone?branch=master)

# Tools for XXIV Lodestone

### Goal

Provide interesting statistics pulled from lodestone

### Dev

Example API response:

`GET {server_url}/scrape/character/{lodestone_id}`

```
{
  "name": "Mina Loriel",
  "free_company": "Zanarkand",
  "lodestone_id": "8774791",
  "species": "Miqo'te",
  "grand_company": "Order of the Twin Adder/Second Serpent Lieutenant",
  "city_state": "Gridania",
  "classes": {
    "carpenter": 50,
    "goldsmith": 50,
    "marauder": 0,
    "gladiator": 0,
    "conjurer": 50,
    "botanist": 20,
    "blacksmith": 18,
    "weaver": 50,
    "leatherworker": 16,
    "astrologian": 0,
    "culinarian": 37,
    "arcanist": 50,
    "rogue": 0,
    "dark_night": 0,
    "armorer": 15,
    "archer": 9,
    "miner": 0,
    "thaumaturge": 26,
    "machinist": 0,
    "pugilist": 0,
    "alchemist": 16,
    "fisher": 0,
    "lancer": 6
  },
  "server": "Zalera"
}
```

### Production

Dev site is publicly available at [academic-bias](https://academic-bias.herokuapp.com/).