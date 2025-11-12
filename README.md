# Authors
Pavlo Vysotin, Brice Moeller

# Pig Dice Game
This is a game made with:
Python
HTML \ CSS
Flask 
SQLite3
Containerized with Docker

# Run Locally
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Run in Docker
docker build -t pig-game .
docker run -p 5000:5000 pig-game
