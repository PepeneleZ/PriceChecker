import random
import re
import requests
from bs4 import BeautifulSoup


def normalize_price(price_text):
    cleaned = re.sub(r"[^0-9,.\s]", "", price_text).replace(" ", "")

    last_comma = cleaned.rfind(",")
    last_dot = cleaned.rfind(".")

    if last_comma == -1 and last_dot == -1:
        return float(cleaned)

    if last_comma == -1 and last_dot != -1:
        parts = cleaned.split(".")
        if all(part.isdigit() for part in parts):
            if len(parts[-1]) == 2:
                whole = "".join(parts[:-1]) or "0"
                return float(f"{whole}.{parts[-1]}")
            if len(parts[-1]) == 3:
                return float("".join(parts))

    if last_comma > last_dot:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    else:
        cleaned = cleaned.replace(",", "")
        if cleaned.count(".") > 1:
            whole, fraction = cleaned.rsplit(".", 1)
            cleaned = whole.replace(".", "") + "." + fraction

    return float(cleaned)


def prepare_site_run(site_name, part_prices, total_prices):
    total_prices[site_name] = 0
    for prices in part_prices.values():
        prices[site_name] = None


def has_url(url):
    return bool(url.strip())


def get_page(url):
    try:
        return requests.get(url, headers=get_headers(), timeout=15)
    except requests.exceptions.RequestException:
        return None


def extract_price_text(soup, store_config):
    price_selector = store_config.get("price_selector")
    if not price_selector:
        return None

    price_element = soup.select_one(price_selector)
    if not price_element:
        return None

    main_price = None
    for child in price_element.children:
        if isinstance(child, str):
            candidate = child.strip()
            if candidate:
                main_price = candidate
                break

    if main_price is None:
        main_price = price_element.get_text(strip=True)

    fraction_selector = store_config.get("fraction_selector")
    if fraction_selector:
        fraction_element = soup.select_one(fraction_selector)
        if not fraction_element:
            return None
        return f"{main_price},{fraction_element.get_text(strip=True)}"

    return main_price


def check_store(store_name, urls, total_prices, part_prices, store_configs):
    store_config = store_configs.get(store_name)
    if not store_config:
        print(f"{store_name} has no scraping configuration. Add one with 'add store'.")
        print()
        return

    prepare_site_run(store_name, part_prices, total_prices)
    lines = []
    request_failed = False

    for part_name, url in urls[store_name].items():
        if not has_url(url):
            continue

        response = get_page(url)
        if response is None:
            request_failed = True
            continue

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        price_text = extract_price_text(soup, store_config)
        if not price_text:
            continue

        lines.append(f"{part_name} price: {price_text}")
        parsed_price = normalize_price(price_text)
        part_prices[part_name][store_name] = parsed_price
        total_prices[store_name] += parsed_price

    if lines:
        print(f"__________From {store_name}__________")
        for line in lines:
            print(line)
    elif request_failed:
        print(f"{store_name} did not respond. Skipping results.")
    else:
        print(f"No prices found for {store_name}.")
    print()


def check_all(urls, total_prices, part_prices, store_configs):
    for store_name in urls.keys():
        check_store(store_name, urls, total_prices, part_prices, store_configs)


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]


def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS)
    }
