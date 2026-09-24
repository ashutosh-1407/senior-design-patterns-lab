# Dungeon Arena

A hands-on project for learning SOLID principles and design patterns by evolving a small battle system.

## Run the application

```bash
python3 -m dungeon_arena
```

## Run the graphical game

```bash
python3 -m dungeon_arena.gui
```

## Run the tests

```bash
python3 -m unittest discover -s tests
```

## Learning agreement

- Start with the smallest design that satisfies the current requirements.
- Introduce a pattern only after identifying the problem it solves.
- You implement the domain classes; your guide reviews them and introduces the next requirement.

## Project structure

```text
dungeon_arena/domain/
├── combat/       # Damage, attack input, and attack outcomes
├── weapons/      # Weapon strategy and its implementations
└── characters/   # Player and enemy entities
```

## Current quest

Create `dungeon_arena/domain/characters/dragon.py` containing the Dragon entity.

Requirements:

- It starts with provided health and rejects negative health.
- Its armor reduces physical damage by 3.
- Magical damage ignores armor.
- Its health never falls below zero.
- It reports whether it is alive.
