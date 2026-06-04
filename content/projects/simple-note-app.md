# Simple Note App

A command-line note-taking application built in Ruby. Add, edit, delete and view notes — all stored persistently on disk.

## Features

- Add notes
- Edit existing notes
- Delete notes with confirmation prompt
- View all notes with timestamps
- Notes persist between sessions using PStore

```
########## Simple Note Application ##########
a) Add
b) Edit
d) Delete
s) Show All
q) Quit

> a
Note: Buy groceries

> s
------------------------ 1 ------------------------
Date: 2026-06-03 12:00:00
Note: Buy groceries
------------------------------------------------------

> b
Enter Index Number to edit: 1
Note: Buy groceries and cook dinner
********************Entry Updated********************

> d
Enter Index Number to delete: 1
Are you sure? (y/n): y
********************Entry Deleted********************

> q
#################### Goodbye! ####################
```

## Tech Stack

- Ruby 2.7+
- Ruby built-in `PStore` for persistence

## Project Structure

- `main.rb` - Entry point
- `application.rb` - Main application loop
- `menu.rb` - User interaction and menu actions
- `manager.rb` - Business logic layer
- `database.rb` - PStore persistence layer
- `note.rb` - Note model


[Full project on GitHub](https://github.com/lillysilly3/simple-note-app)

[← Back to Portfolio](/)
