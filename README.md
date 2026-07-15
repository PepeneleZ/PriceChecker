# PriceChecker

PriceChecker is a Python command-line app for scraping and comparing PC component prices across multiple online stores.

It can:

- check current prices for all configured stores or a single store
- show prices by part
- find the cheapest store for a part
- estimate the cheapest full build
- add new stores and URLs

## Features

- Interactive CLI
- Store-specific scraping selectors
- Persisted price/store configuration in JSON
- Support for multiple PC parts:
  - CPU
  - GPU
  - RAM
  - Storage
  - Motherboard
  - PSU
  - Case

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

## Installation

```bash
pip install requests beautifulsoup4
```

## Run

From the project root:

```bash
python src/main.py
```

## Commands

### Price checks

- `check all` - check all configured stores
- `check <store>` - check one store
- `price all` - show all prices grouped by part
- `price <part>` - show prices for one part

### Cheapest options

- `cheap all` - show the cheapest store for each part
- `cheap <part>` - show the cheapest store for one part
- `cheap build` - calculate the cheapest full build

### Store management

- `add store <store name> | <price css selector>`
- `add store <store name> | <price css selector> | <fraction css selector>`
- `add url <store name> | <part> | <url>`
- `set url <store name> | <part> | <url>`
- `list stores`

### Help and exit

- `help`
- `help <command>`
- `list commands`
- `exit`

## Data files

- `src/resources/urls_prices.json` stores the configured URLs, scraped prices, totals, and scraper selectors.

## Notes

- Command matching is case-insensitive.
- The scraper depends on the current HTML structure of each store page.
- Some stores may not have URLs for every part.
