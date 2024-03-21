# 2048Game
Simple CLI implementation of the 2048 game
This was an interview question I got at a certain company. I thought it was interesting enough to do as a side project.

# How to play
Clone the repo and `cd` to the folder. Then run: 
```python3 game.py```

# Todo
- Make a frontend so that it can be played in the browser. Maybe an opportunity to try out some wasm since this was made in python. 
- Pretty print with borders and with consistent spacing
    - If we get 16, the numbers aren't aligned anymore. 
- Game over screen. No way to lose right now :p
- Replace output instead of having the game history in the terminal
- Undo last move 