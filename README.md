# Magic Fight

A two-player local battle game written in Python with Pygame Zero. Two wizards share one keyboard on a tile-based arena, firing spells at each other until one runs out of health. The in-game text is in Turkish; the how-to-play screen inside the game explains the controls.

## Features

- Tile-based arena drawn from a 2D map array
- Two players with four-directional movement and projectile attacks
- Health bars that change as players take damage
- A shield pickup that blocks damage for a limited time, then respawns in the center
- Game screens: title, how-to-play, battle and winner

## Controls

| Action | Player 1 | Player 2 |
|---|---|---|
| Move | W A S D | Arrow keys |
| Fire spell | X + direction | Right Ctrl + direction |
| Use shield (after picking it up) | Z | Right Shift |
| Start / restart | Space | Space |

## Running

```
pip install pgzero kivy
python oyunsu.py
```

Images are loaded from the `images/` folder, so run the game from the project directory.
