# Pokedex CLI

A command-line application built in Go that lets you explore and catch Pokémon from the terminal.

## Features

- Browse Pokémon locations with pagination
- Explore areas to discover creatures
- Catch mechanics based on base experience
- View and inspect caught Pokémon
- Response caching for performance

![Pokedex screenshot 1](/images/pokedex1.png)

![Pokedex screenshot 2](/images/pokedex2.png)

## Tech Stack

- Go 1.21+
- REST API integration with PokeAPI
- Go routines for concurrency

## Project Structure

- `main.go` - Entry point
- `repl.go` - Read-Eval-Print Loop logic
- `commands.go` - CLI command implementations
- `repl_test.go` - Test suite
- `internal/pokeapi/` - PokéAPI client with caching

## How to Run

go build -o pokedex && ./pokedex

[🐙 View on GitHub](https://github.com/lillysilly3/pokedex)

[← Back to Portfolio](/)