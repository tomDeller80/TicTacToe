# ❌ Tic-Tac-Toe Pro ⭕

A modern, terminal-based Tic-Tac-Toe game built with **Python**, powered by **NumPy** for grid logic and **Rich** for a beautiful, interactive user interface.

---

## ✨ Features

* **Beautiful UI:** Uses `Rich` for stylized panels, rules, centering, and colored emoji tokens (❌ and ⭕).
* **Smart Input:** Utilizes `IntPrompt` to ensure players only select valid, unoccupied cells.
* **Robust Game Logic:** Leverages `NumPy` matrices to calculate wins across axes and diagonals efficiently.
* **Score Tracking:** Persistent scoring across multiple rounds.
* **Dynamic ASCII Art:** Includes custom logos and victory trophies.
* **"Cats Game" Detection:** Automatically identifies and handles draw scenarios.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.7+
* NumPy
* Rich

### Installation
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/yourusername/tictactoe-pro.git](https://github.com/yourusername/tictactoe-pro.git)
   cd tictactoe-pro
   ```

2. **Install the required dependencies:**
    ```bash
   pip install numpy rich
   ```
---

## 🛠️ Project Structure

- `main.py`: The entry point and primary game loop controller.
- `game.py`: Contains the Game class, managing players, rounds, and game states.
- `matrix.py`: The "engine" of the game. Uses a $3 \times 3$ NumPy array to handle token placement and win-condition math.
- `player.py`: Defines the Player class to track names, tokens, and scores.
- `art.py`: A collection of ASCII art strings including the game logo, trophy, and draw screen.

---

## 🎮 How to Play

1. **Run the game:**
```bash
    python main.py
```
2. **Setup:** Enter player names and choose whether Player 1 wants to be X or O.
3. **Gameplay:** The board is mapped to numbers 1-9:

```
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9
```
4. Selection: When prompted, type the number of an available square and press `Enter`.
5. Winning: Get three in a row (horizontal, vertical, or diagonal) to win the round and claim the 🏆!

---

## 🧠 Technical Highlights

**The Matrix Engine**
The game converts a single integer input (1-9) into matrix coordinates $(x, y)$ using floor division and modulo operators:

- **Row index:** $(n - 1) // 3$
- **Column index:** $(n - 1) \% 3$

**Win Validation**

```
# Example of checking an axis
if len(np.unique(row)) == 1 and row[0] != ' ':
    return True
```

---

## 📝 License

This project is open-source and available under the MIT License.
