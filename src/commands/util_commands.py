def list_prices(total_prices):
    x = 0
    for key, value in total_prices.items():
        if value != 0:
            print(f"The total price of parts available at {key} is : {value:.2f}")
            x += 1
    if(x == 0):
        print("You don't seem to have run any checks. To be able to list the prices run at least one check!")
    print()
    
def unknown():
    print("Unknown command. Check for typing mistakes! Use 'help' for command usage.")
    print()


HELP_TOPICS = {
    "check all": {
        "description": "Checks all configured stores and refreshes scraped prices.",
        "syntax": ["check all"],
        "examples": ["check all"],
        "notes": [
            "Use this before running price/cheap commands if your data is outdated.",
            "Stores that do not respond are skipped from displayed results.",
        ],
    },
    "check <store>": {
        "description": "Checks one store only.",
        "syntax": ["check <store>"],
        "examples": ["check emag", "check PC Garage"],
        "notes": [
            "Store name matching is case-insensitive.",
            "The store must exist in configured stores.",
        ],
    },
    "price all": {
        "description": "Shows all available prices grouped by part.",
        "syntax": ["price all"],
        "examples": ["price all"],
        "notes": [
            "Only available values are shown.",
        ],
    },
    "price <part>": {
        "description": "Shows prices for one part across all stores.",
        "syntax": ["price <part>"],
        "examples": ["price cpu", "price motherboard"],
        "notes": [
            "Part name matching is case-insensitive.",
        ],
    },
    "list prices": {
        "description": "Shows total build cost for each store with valid results.",
        "syntax": ["list prices"],
        "examples": ["list prices"],
        "notes": [],
    },
    "cheap all": {
        "description": "Shows the cheapest store for each part.",
        "syntax": ["cheap all"],
        "examples": ["cheap all"],
        "notes": [],
    },
    "cheap <part>": {
        "description": "Shows the cheapest store for a specific part.",
        "syntax": ["cheap <part>"],
        "examples": ["cheap gpu", "cheap ram"],
        "notes": [],
    },
    "cheap build": {
        "description": "Calculates the cheapest full build using best price per part.",
        "syntax": ["cheap build"],
        "examples": ["cheap build"],
        "notes": [
            "Requires at least one valid price for every part.",
        ],
    },
    "add store": {
        "description": "Adds a new store and its scraping CSS selectors.",
        "syntax": [
            "add store <store name> | <price css selector>",
            "add store <store name> | <price css selector> | <fraction css selector>",
        ],
        "examples": [
            "add store DemoShop | span.price",
            "add store DemoShop | div.price-main | sup.price-fraction",
        ],
        "notes": [
            "Use the third selector when integer and decimal parts are split in HTML.",
            "After adding a store, set URLs per part using add url / set url.",
        ],
    },
    "add url": {
        "description": "Sets the URL for one store and one part.",
        "syntax": ["add url <store name> | <part> | <url>"],
        "examples": [
            "add url DemoShop | CPU | https://example.com/cpu",
            "add url PC Garage | GPU | https://www.pcgarage.ro/...",
        ],
        "notes": [
            "set url is an alias of this command.",
            "Part must be one of the configured parts (CPU, GPU, RAM, Storage, Motherboard, PSU, Case).",
        ],
    },
    "set url": {
        "description": "Alias of add url.",
        "syntax": ["set url <store name> | <part> | <url>"],
        "examples": ["set url DemoShop | RAM | https://example.com/ram"],
        "notes": [],
    },
    "list stores": {
        "description": "Lists stores with selector and URL coverage per part.",
        "syntax": ["list stores"],
        "examples": ["list stores"],
        "notes": [],
    },
    "help": {
        "description": "Shows command index or detailed help for one command.",
        "syntax": ["help", "help <command>"],
        "examples": ["help", "help add store", "help cheap build"],
        "notes": [
            "Use full command names for best results (for example: help check all).",
        ],
    },
    "list commands": {
        "description": "Alias of help.",
        "syntax": ["list commands"],
        "examples": ["list commands"],
        "notes": [],
    },
    "exit": {
        "description": "Closes the application.",
        "syntax": ["exit"],
        "examples": ["exit"],
        "notes": [],
    },
}


HELP_ALIASES = {
    "check": "check <store>",
    "price": "price <part>",
    "cheap": "cheap <part>",
    "add store <store name> | <price css selector> [| <fraction css selector>]": "add store",
    "add url <store name> | <part> | <url>": "add url",
    "set url <store name> | <part> | <url>": "set url",
}


def _normalize_topic(topic):
    return " ".join(topic.strip().lower().split())


def _print_topic(topic_key):
    topic = HELP_TOPICS[topic_key]
    print()
    print(f"Help: {topic_key}")
    print(f"Description: {topic['description']}")
    print()
    print("Syntax:")
    for syntax in topic["syntax"]:
        print(f"  {syntax}")
    print()
    print("Examples:")
    for example in topic["examples"]:
        print(f"  {example}")

    if topic["notes"]:
        print()
        print("Notes:")
        for note in topic["notes"]:
            print(f"  - {note}")
    print()


def help_commands(topic=None):
    if topic is not None and topic.strip():
        normalized = _normalize_topic(topic)
        resolved_topic = HELP_ALIASES.get(normalized, normalized)
        if resolved_topic in HELP_TOPICS:
            _print_topic(resolved_topic)
            return

        print()
        print(f"No detailed help found for '{topic}'.")
        print("Try one of these:")
        for key in HELP_TOPICS.keys():
            print(f"  {key}")
        print()
        return

    print()
    print("Available commands (use 'help <command>' for details):")
    print()
    for key in HELP_TOPICS.keys():
        print(f"  {key}")
    print()


def list_commands():
    help_commands()