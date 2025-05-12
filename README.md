# Python Games Documentation

## Overview
This project contains three Python games implemented using Pygame:
1. Snake Game
2. Pong Game
3. Combined Menu System

## Installation Requirements
```
pygame==2.6.1
```

## How to Run
1. Make sure you have Python and Pygame installed
2. Run the combined menu: `python3 combined_games.py`
3. Or run individual games:
   - Snake Game: `python3 snake_game.py`
   - Pong Game: `python3 pong_game.py`

## Game Controls

### Main Menu
- Use UP/DOWN arrow keys or number keys (1, 2, 3) to select
- Press ENTER to start selected game
- Press 3 or close window to quit

### Snake Game
- Controls:
  - ↑ (Up Arrow): Move Up
  - ↓ (Down Arrow): Move Down
  - ← (Left Arrow): Move Left
  - → (Right Arrow): Move Right
  - ESC: Return to main menu
- Objective:
  - Eat food (red squares) to grow
  - Avoid hitting yourself
  - Score increases with each food eaten

### Pong Game
- Controls:
  - Left Paddle:
    - W: Move Up
    - S: Move Down
  - Right Paddle:
    - ↑ (Up Arrow): Move Up
    - ↓ (Down Arrow): Move Down
  - ESC: Return to main menu
- Objective:
  - Hit the ball with your paddle
  - Score when opponent misses
  - First to reach agreed score wins

## Code Structure

### combined_games.py
- Main menu system
- Integrates both games
- Handles game switching
- Features:
  - Clean menu interface
  - Easy navigation
  - Seamless game transitions

### snake_game.py
- Classes:
  - Snake: Handles snake movement and growth
  - Food: Manages food spawning
- Features:
  - Score display
  - Collision detection
  - Wrap-around walls
  - Progressive difficulty

### pong_game.py
- Classes:
  - Paddle: Manages paddle movement
  - Ball: Handles ball physics
- Features:
  - Score tracking
  - Ball physics
  - Two-player gameplay
  - Center line display

## Game Features

### Snake Game Features
1. Growing snake mechanics
2. Random food spawning
3. Score tracking
4. Wall wrapping
5. Self-collision detection
6. Smooth controls

### Pong Game Features
1. Two-player gameplay
2. Score display for both players
3. Ball physics
4. Paddle collision detection
5. Center line visualization
6. Smooth paddle movement

## Technical Implementation
- Built with Pygame
- Object-oriented design
- Modular code structure
- Clean separation of concerns
- Event-driven architecture
- Consistent frame rate (60 FPS)
- Efficient collision detection
