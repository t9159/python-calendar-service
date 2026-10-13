# Interactive Games Platform

A lightweight, frontend-only web application designed to host multiple interactive mini-games and educational tools within a centralized dashboard.

## Project Structure

```plaintext
games-platform/
├── dashboard/                      # Central hub and navigation
│   ├── index.html                  # Main dashboard interface
│   ├── style.css                   # Dashboard styling
│   └── script.js                   # Dashboard logic & routing
├── games/                          # Interactive game modules
│   ├── number_game/                # Numbers Challenge (Grid and timer logic)
│   ├── canvas_challenge/           # Shape Catcher (HTML5 Canvas logic)
│   └── memory_game/                # Memory Game (Pair matching logic)
├── dictionary/                     # Educational applications
│   └── index.html                  # Interactive Dictionary (HTML/CSS/JS in one file)
├── auth/                           # User authentication layer
│   ├── index.html                  # Login & Registration interface
│   ├── style.css                   # Authentication styling
│   └── script.js                   # Form validation logic
└── README.md                       # Project documentation