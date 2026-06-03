# Pokedex CLI

A command-line application built in Go that lets you explore and catch Pokémon from the terminal.

## Features

- Browse Pokémon locations with pagination
- Explore areas to discover creatures
- Catch mechanics based on base experience
- View and inspect caught Pokémon
- Response caching for performance

```
Pokedex > help
Welcome to the Pokedex!
Usage:
help: Displays a help message
map: Displays the names of next 20 location areas
mapb: Displays the names of previous 20 location areas
explore: Displays the names of pokemon in given area
catch: Attemps to catch a pokemon and add it to your Pokedex
inspect: Takes the name of a Pokemon and prints the name, height, weight, stats and type(s) of the Pokemon
pokedex: Prints a list of all the names of the Pokemon that were caught
exit: Exit the Pokedex
Pokedex > map
canalave-city-area
eterna-city-area
pastoria-city-area
sunyshore-city-area
sinnoh-route-204-south
...
Pokedex > explore pastoria-city-area
Exploring pastoria-city-area...
Found Pokemon:
 - shellos
 - floatzel
 - buizel
 - wingull
Pokedex > catch pikachu
Throwing a Pokeball at pikachu...
pikachu was caught!
You may now inspect it with the inspect command.
Pokedex > inspect pikachu
Name: pikachu
Height: 4
Weight: 60
Stats:
 -hp: 35
 -attack: 55
 -defense: 40
 -special-attack: 50
 -special-defense: 50
 -speed: 90
Types:
 -electric
Pokedex > pokedex
Your Pokedex:
 -pikachu
Pokedex > exit
Closing the Pokedex... Goodbye!
```

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


[Full project on GitHub](https://github.com/lillysilly3/pokedex)

[← Back to Portfolio](/)