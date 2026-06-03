# Friend List App

A Ruby on Rails web application for managing your personal friend list. Users can sign up, log in, and manage their own private contacts.

**Live app:** [friend-list-app-0a3b2c1a2f33.herokuapp.com](https://friend-list-app-0a3b2c1a2f33.herokuapp.com)

## Features

- User authentication with Devise (sign up, log in, sign out)
- Add, view, edit, and delete friends
- Each user has their own private, secured friends' list
- Authorization — users can only view and edit their own friends
- Responsive UI with Bootstrap

![Friend list](/images/ror_list.png)
![Add friend](/images/ror_add.png)
![Show friend](/images/ror_show.png)
![Edit friend](/images/ror_edit.png)

## Tech Stack

- Ruby on Rails 8.1
- PostgreSQL
- Devise
- Hotwire (Turbo + Stimulus)
- Bootstrap

## Project Structure

- `app/models/` - Friend and User models with associations
- `app/controllers/` - Friends and Home controllers
- `app/views/` - ERB templates with Bootstrap styling
- `config/` - Routes, database, and environment configuration
- `test/` - Model and controller tests

[Full project on GitHub](https://github.com/lillysilly3/friend_list_app)

[← Back to Portfolio](/)
