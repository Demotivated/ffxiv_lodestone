[![Build Status](https://travis-ci.org/Demotivated/ffxiv_lodestone.svg?branch=master)](https://travis-ci.org/Demotivated/ffxiv_lodestone) [![Coverage Status](https://coveralls.io/repos/Demotivated/ffxiv_lodestone/badge.svg?branch=master&service=github)](https://coveralls.io/github/Demotivated/ffxiv_lodestone?branch=master)

# Tools for FFXIV Lodestone

### Goal

Provide interesting statistics pulled from lodestone

### Dev

Example API response:

`GET /scrape/character/{lodestone_id}/`

```
{
    "free_company": "Zanarkand",
    "name": "Mina Loriel",
    "classes": {
        "armorer": {
            "level": 15
        },
        "pugilist": {
            "level": 0
        },
        "carpenter": {
            "level": 50
        }
        ...
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