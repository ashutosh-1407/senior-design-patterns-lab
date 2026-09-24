# Senior Design Pattern Lab

A learning project that evolves a small Dragon Arena game while applying SOLID principles and practical design patterns.

## Versions

- Terminal game — Python domain/application code and tests.
- Browser game — static HTML, CSS, and JavaScript under `web/`, suitable for GitHub Pages.

## Run the terminal game

    python3 -m dungeon_arena

Run tests:

    python3 -m pytest

## Run the browser game locally

From the `web/` directory:

    python3 -m http.server 8000

Open http://localhost:8000.

The browser version includes themed battlefield artwork, weapon-specific attack animations, Dragon health, undo, statistics, Fire/Ice themes, and a battle-complete state.

## Design patterns covered

Strategy, Factory Method, Abstract Factory, Adapter, Decorator, Observer, State, Command, Chain of Responsibility, Builder, Facade, Composite, Proxy, Singleton, and Template Method.

## GitHub Pages

Publish the `web/` directory as the Pages source, or configure a Pages workflow that deploys that directory. The browser version has no server-side dependency.