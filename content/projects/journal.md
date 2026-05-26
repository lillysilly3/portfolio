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

journal/
├── main.py                    # App entry point
├── app/
│   ├── screens/
│   │   ├── login.py           # Login screen
│   │   ├── setup.py           # Password setup screen
│   │   └── journal.py         # Main journal screen
│   ├── components/
│   │   ├── calendar_widget.py # Calendar component
│   │   └── moods.py           # Mood definitions
│   └── utils/
│       ├── database.py        # SQLite database client
│       └── theme.py           # App color theme
├── assets/                    # Reserved for future assets
├── requirements.txt
├── LICENSE
└── .gitignore


[🐙 View on GitHub](https://github.com/lillysilly3/journal)

[← Back to Portfolio](/)