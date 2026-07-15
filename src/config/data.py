import json
import os

urls = {}
part_prices = {}
total_prices = {}
store_configs = {}

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = os.path.dirname(script_dir)

# Construct the relative path to the JSON file
file_path = os.path.join(script_dir, 'resources', 'urls_prices.json')

with open(file_path, 'r') as file:
    data = json.load(file)

urls = data["urls"]
part_prices = data["part_prices"]
total_prices = data["total_prices"]
store_configs = data.get("store_configs", {})


def save_data():
    payload = {
        "urls": urls,
        "part_prices": part_prices,
        "total_prices": total_prices,
        "store_configs": store_configs,
    }
    with open(file_path, "w") as file:
        json.dump(payload, file, indent=4)


def get_store_key(store_name):
    for key in urls.keys():
        if key.lower() == store_name.lower():
            return key
    return None


def get_part_key(part_name):
    for key in part_prices.keys():
        if key.lower() == part_name.lower():
            return key
    return None


def add_store(store_name, price_selector, fraction_selector=None):
    if get_store_key(store_name):
        raise ValueError("Store already exists.")

    urls[store_name] = {part: "" for part in part_prices.keys()}
    total_prices[store_name] = 0

    for part in part_prices.keys():
        part_prices[part][store_name] = None

    store_configs[store_name] = {
        "price_selector": price_selector,
        "fraction_selector": fraction_selector,
    }

    save_data()


def set_store_url(store_name, part_name, url):
    store_key = get_store_key(store_name)
    if not store_key:
        raise ValueError("Store not found.")

    part_key = get_part_key(part_name)
    if not part_key:
        raise ValueError("Part not found.")

    urls[store_key][part_key] = url
    save_data()
