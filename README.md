[![Build Status](https://travis-ci.org/Demotivated/fxiv_lodestone.svg?branch=master)](https://travis-ci.org/Demotivated/fxiv_lodestone) [![Coverage Status](https://coveralls.io/repos/Demotivated/fxiv_lodestone/badge.svg?branch=master&service=github)](https://coveralls.io/github/Demotivated/fxiv_lodestone?branch=master)

# Tools for XXIV Lodestone

### Goal

Provide interesting statistics pulled from lodestone

### Dev

Example API response:

`GET {server_url}/scrape/character/{lodestone_id}`

```
{
    "free_company": "Zanarkand",
    "name": "Mina Loriel",
    "classes": {
        "armorer": {
            "level": 15
        },
        "alchemist": {
            "level": 16
        },
        "leatherworker": {
            "level": 16
        },
        "pugilist": {
            "level": 0
        },
        "carpenter": {
            "level": 50
        },
        "culinarian": {
            "level": 37
        },
        "arcanist": {
            "level": 50
        },
        "fisher": {
            "level": 0
        },
        "machinist": {
            "level": 0
        },
        "conjurer": {
            "level": 50
        },
        "blacksmith": {
            "level": 18
        },
        "astrologian": {
            "level": 0
        },
        "thaumaturge": {
            "level": 26
        },
        "gladiator": {
            "level": 0
        },
        "miner": {
            "level": 0
        },
        "lancer": {
            "level": 6
        },
        "rogue": {
            "level": 0
        },
        "marauder": {
            "level": 0
        },
        "botanist": {
            "level": 20
        },
        "weaver": {
            "level": 50
        },
        "archer": {
            "level": 9
        },
        "darknight": {
            "level": 0
        },
        "goldsmith": {
            "level": 50
        }
    },
    "species": "Miqo'te",
    "grand_company": "Order of the Twin Adder/Second Serpent Lieutenant",
    "server": "Zalera",
    "lodestone_id": "8774791",
    "city_state": "Gridania"
}
```

### Production

Dev site is publicly available at [academic-bias](https://academic-bias.herokuapp.com/).