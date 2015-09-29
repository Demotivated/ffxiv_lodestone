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
      "stats": {
        "tp": 1000,
        "mp": 4566,
        "hp": 4583
      },
      "level": 50,
      "properties": {
        "offensive": {
          "accuracy": 378,
          "critical_hit_rate": 432,
          "determination": 251
        },
        "physical": {
          "skill_speed": 341,
          "attack_power": 112
        },
        "defensive": {
          "parry": 341,
          "magic_defense": 543,
          "defense": 317
        },
        "mental": {
          "healing_magic_potency": 527,
          "attack_magic_potency": 210,
          "spell_speed": 442
        }
      },
      "resistances": {
        "physical": {
          "slashing": 100,
          "blunt": 100,
          "piercing": 100
        },
        "elemental": {
          "lightning": 267,
          "water": 271,
          "wind": 269,
          "ice": 269,
          "fire": 269,
          "earth": 270
        },
        "status": {
          "sleep": 0,
          "heavy": 0,
          "blind": 0,
          "bind": 0,
          "silence": 0,
          "stun": 0,
          "slow": 0,
          "poison": 0
        }
      },
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
  "ilevel": 90,
  "lodestone_id": "d19447e548d",
  "name": "Thyrus Zenith",
  "stats": {
    "auto_attack": 52.74,
    "delay": 3.44,
    "damage": 69
  },
  "type": "Two-handed Conjurer's Arm"
}
```
