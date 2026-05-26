# Journal App

A personal desktop journaling application built with Python.

![Journal screenshot 2](/images/journal2.png)

## Features

- Password protection set up and reset. Reseting password deletes all entries
- Daily journal entries with mood tracking
- Color-coded calendar to browse entries
- Mood tags: Happy, Neutral, Sad, Angry, Tired, Energetic


![Journal screenshot 1](/images/journal1.png)

![Journal screenshot 3](/images/journal3.png)

## Tech Stack

- Python with CustomTkinter
- SQLite3 database
- bcrypt for password security

## Project Structure

- `main.py` - Application entry point
- `login.py` - Login screen
- `setup.py` - First-time password setup
- `journal.py` - Main journal screen
- `calendar_widget.py` - Calendar component
- `database.py` - SQLite database client
- `moods.py` - Mood definitions and color mappings
- `theme.py` - Application color theme

## How to Run

pip install -r requirements.txt
python main.py

[🐙 View on GitHub](https://github.com/lillysilly3/journal)

[← Back to Portfolio](/)