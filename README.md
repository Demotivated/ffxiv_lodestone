[![Build Status](https://travis-ci.org/Demotivated/ffxiv_lodestone.svg?branch=master)](https://travis-ci.org/Demotivated/ffxiv_lodestone) [![Coverage Status](https://coveralls.io/repos/Demotivated/ffxiv_lodestone/badge.svg?branch=master&service=github)](https://coveralls.io/github/Demotivated/ffxiv_lodestone?branch=master)

# Tools for FFXIV Lodestone

Example APIs:

`GET /scrape/character/{lodestone_id}/`

```
{
  "server": "Zalera",
  "lodestone_id": "8774791",
  "grand_company": {
    "name": "Order of the Twin Adder",
    "rank": "Second Serpent Lieutenant"
  },
  "city_state": "Gridania",
  "jobs": [
    {
      "level": 50,
      "items": [
        {
          "lodestone_id": "d19447e548d",
          "name": "Thyrus Zenith"
        },
        {
          "lodestone_id": "fa0a11eb218",
          "name": "Platinum Circlet of Healing"
        },
        {
          "lodestone_id": "cada9ec7074",
          "name": "Arachne Robe"
        },
        ...
      ],
      "job": "White Mage"
    }
  ],
  "name": "Mina Loriel",
  "free_company": "Zanarkand",
  "species": "Miqo'te",
  "classes": {
    "conjurer": {
      "level": 50
    },
    "astrologian": {
      "level": 0
    },
    ...
  }
}
```

`GET /scrape/item/{lodestone_id}`

```
{
    "lodestone_id": "d19447e548d",
    "name": "Thyrus Zenith"
}
```
