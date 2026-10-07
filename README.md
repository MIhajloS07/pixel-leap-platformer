# Pixel Leap Platformer

A retro-inspired 2D pixel-art platformer built with **Python** and **Pygame**.

Navigate through a medieval-themed level, avoid dangerous obstacles and enemies, collect coins, and reach the goal before losing all your lives.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2D%20Game%20Development-green?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎮 Features

* Player movement and jumping
* Physics-based movement with gravity and velocity
* Static platforms
* Moving platforms
* Enemy entities with horizontal movement
* Collectible coins and scoring system
* Spike obstacles
* Three-life system
* Goal and win condition
* Lose condition when all lives are lost
* Level and player reset functionality
* Sound effects for gameplay events
* Retro-inspired pixel-art aesthetic
* 800×600 game window running at 60 FPS

---

## 🕹️ Controls

| Key                 | Action        |
| ------------------- | ------------- |
| `A` / `←`           | Move left     |
| `D` / `→`           | Move right    |
| `W` / `↑` / `SPACE` | Jump          |
| `C`                 | Show controls |
| `R`                 | Reset level   |
| `ESC`               | Quit          |

---

## Screenshots

| Game GUI | Controls |
|---|---|
| <img width="793" height="623" alt="image" src="https://github.com/user-attachments/assets/9adf3793-8bfb-434b-95e9-72c5e47e2b7c" /> | <img width="792" height="618" alt="image" src="https://github.com/user-attachments/assets/0e815568-c765-4511-8d59-89e3aeb61786" /> |
| Win screen | Lose screen |
|---|---|
| <img width="793" height="623" alt="image" src="https://github.com/user-attachments/assets/5642c5f7-4940-42be-81a2-0bb5136df938" /> | <img width="792" height="621" alt="image" src="https://github.com/user-attachments/assets/1f8c200e-8246-49f8-ba00-cc888a3d1cd6" /> |

## 🏆 How to Play

Your goal is to reach the level's **green goal** while collecting as many coins as possible.

Be careful — touching an enemy or spike costs one life and resets the player's position.

### Scoring

Coins increase your score when collected.

### Lives

The player starts with **3 lives**.

* Enemy collision → lose a life
* Spike collision → lose a life
* `0` lives → game over

### Winning

Reach the goal to complete the level.

After winning, press `ENTER` to restart the game.

---

## 🛠️ Tech Stack

* **Python**
* **Pygame**
* **Object-oriented programming**
* **2D collision detection**
* **Basic game physics**
* **Vector-based movement**
* **Game loop architecture**

---

## 📁 Project Structure

```text
pixel-leap-platformer/
│
├── pixelleap_models/
│   └── ...                 # Game entity/model definitions
│
├── sfx/
│   └── ...                 # Sound effects
│
├── constants.py            # Game configuration and constants
├── game.py                 # Main game logic and game loop
├── .gitignore
├── LICENSE
└── README.md
```

### Main Files

#### `game.py`

Contains the main gameplay implementation, including:

* Player movement
* Jumping and gravity
* Collision detection
* Platform handling
* Moving platforms
* Enemy movement
* Coin collection
* Spike collisions
* Win/lose states
* Rendering
* Input handling
* Game reset logic

#### `constants.py`

Centralizes important game configuration such as:

* Screen dimensions
* FPS
* Player speed
* Gravity
* Jump speed
* Colors
* Starting player position
* Entity colors

Keeping these values separate makes gameplay tuning easier without modifying the core game logic.

#### `pixelleap_models/`

Contains the models/entities used by the game.

#### `sfx/`

Contains the sound effects used for gameplay events such as jumping, collecting coins, taking damage, winning, and losing.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed.

You can check your Python version with:

```bash
python --version
```

### 1. Clone the repository

```bash
git clone https://github.com/MIhajloS07/pixel-leap-platformer.git
```

### 2. Enter the project directory

```bash
cd pixel-leap-platformer
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python game.py
```

---

## 🧠 Technical Overview

The game uses a traditional real-time game loop built with Pygame.

Each update cycle handles:

1. Input processing
2. Moving platform updates
3. Enemy movement
4. Player movement
5. Gravity and jumping
6. Platform collision detection
7. Enemy and spike collisions
8. Coin collection
9. Win/lose state checks
10. Rendering

The player uses velocity-based movement, with gravity continuously affecting vertical velocity while collision detection prevents the player from passing through platforms.

Moving platforms reverse their velocity when reaching their configured movement boundaries.

---

## Game Design

Pixel Leap Platformer combines a simple retro platforming gameplay loop with a **dark medieval-inspired atmosphere**.

The gameplay focuses on:

> **Move → Jump → Avoid → Collect → Reach the Goal**

The intentionally simple mechanics make the project a compact example of implementing fundamental 2D game-development concepts with Pygame.

---

## Learning Goals

This project was developed as a practical exercise in Python and game development.

It focuses on understanding:

* Game loops
* Event handling
* Keyboard input
* 2D coordinates
* Velocity and gravity
* Collision detection
* Entity-based game logic
* Rendering with Pygame
* Game states
* Audio integration
* Organizing a small game project

---

## Possible Future Improvements

Potential improvements for future versions include:

* [ ] Multiple levels
* [ ] More enemy types
* [ ] Improved enemy AI
* [ ] Animated player sprites
* [ ] More advanced pixel-art assets
* [ ] Background music
* [ ] Main menu
* [ ] Pause menu
* [ ] High-score system
* [ ] Additional collectibles
* [ ] More environmental hazards
* [ ] Level progression system
* [ ] Improved UI
* [ ] Save/load functionality

---

## License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for the complete license text.

---

## 👨‍💻 Author

**Mihajlo Stoiljković**

GitHub: [@MIhajloS07](https://github.com/MIhajloS07)

---

⭐ If you like the project, consider giving the repository a star!
