from config.data import add_store as add_store_data
from config.data import set_store_url
from config.data import urls, part_prices, store_configs


def add_store(raw_args):
    parts = [part.strip() for part in raw_args.split("|")]
    if len(parts) not in (2, 3):
        print("Usage: add store <store name> | <price css selector> [| <fraction css selector>]")
        print()
        return

    store_name = parts[0]
    price_selector = parts[1]
    fraction_selector = parts[2] if len(parts) == 3 and parts[2] else None

    if not store_name or not price_selector:
        print("Store name and price selector are required.")
        print()
        return

    try:
        add_store_data(store_name, price_selector, fraction_selector)
    except ValueError as error:
        print(error)
        print()
        return

    print(f"Store '{store_name}' added.")
    print()


def set_url(raw_args):
    parts = [part.strip() for part in raw_args.split("|")]
    if len(parts) != 3:
        print("Usage: set url <store name> | <part> | <url>")
        print()
        return

    store_name, part_name, url = parts
    if not store_name or not part_name or not url:
        print("Store name, part and URL are required.")
        print()
        return

    try:
        set_store_url(store_name, part_name, url)
    except ValueError as error:
        print(error)
        print()
        return

    print(f"URL set for {store_name} - {part_name}.")
    print()


def list_stores():
    print()
    if not urls:
        print("No stores configured.")
        print()
        return

    print("Configured stores:")
    for store_name in urls.keys():
        configured_urls = sum(1 for value in urls[store_name].values() if value.strip())
        selector = store_configs.get(store_name, {}).get("price_selector", "n/a")
        print(f"- {store_name} ({configured_urls}/{len(part_prices)} URLs, selector: {selector})")
    print()
