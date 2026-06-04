# Cryptocurrency Converter

A command-line cryptocurrency converter built in Ruby. Convert BTC, ETH, XRP, DASH and LTC to USD or EUR using live prices from the CryptoCompare API.

## Features

- Convert cryptocurrency amounts to USD or EUR
- Live prices fetched from CryptoCompare API
- Supports decimal amounts (e.g. 0.5 BTC)
- Graceful error handling for network failures

```
########## Cryptocurrency Converter ##########
a) Convert to USD
b) Convert to EUR
q) Quit
Action: a

-----------Available Coins-----------
BTC, ETH, XRP, DASH, LTC
Coin: BTC
Amount: 0.5
--------------------------------------------------
            0.5 BTC = 31245.75 USD
--------------------------------------------------
```

## Tech Stack

- Ruby 2.7+
- CryptoCompare API
- Ruby built-in `net/http` and `json`

## Project Structure

- `main.rb` - Entry point and menu loop
- `manager.rb` - Business logic and API fetching
- `coin.rb` - Coin model


[Full project on GitHub](https://github.com/lillysilly3/cryptocurrency_converter)

[← Back to Portfolio](/)
