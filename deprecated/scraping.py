import requests
from bs4 import BeautifulSoup


def check_emag(urls, total_prices, part_prices):
    print()
    print(f"__________From Emag__________")
    for key, value in urls["Emag"].items():

        if value == ' ':
            print(f"{key} price: n/a")
            continue

        response = requests.get(value)

        if response.status_code == 200:

            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            price_element = soup.find('p', class_='product-new-price')

            if price_element:
                price = price_element.get_text(strip=True)
                print(f"{key} price: {price}")

                cleaned_price = price.replace("Lei", "").strip()
                cleaned_price = cleaned_price.replace(".", "").strip()
                cleaned_price = cleaned_price.replace(",", ".")
                part_prices[key]["Emag"] = cleaned_price
                total_prices["Emag"] += float(cleaned_price)
            else:
                print("Price not found on the page")
        else:
            print(f"Failed to retrieve page, status code: {response.status_code}")
    print()

def check_pcgarage(urls, total_prices, part_prices):
    print()
    print(f"__________From PC Garage__________")
    for key, value in urls["PC Garage"].items():

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        response = requests.get(value, headers=headers)

        if response.status_code == 200:

            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            price_element = soup.find('p', class_='product-new-price')

            if price_element:
                price = price_element.get_text(strip=True)
                print(f"{key} price: {price}")

                cleaned_price = price.replace("Lei", "").strip()
                cleaned_price = cleaned_price.replace(".", "").strip()
                cleaned_price = cleaned_price.replace(",", ".")
                part_prices[key]["PC Garage"] = cleaned_price
                total_prices["PC Garage"] += float(cleaned_price)
            else:
                print("Price not found on the page")
        else:
            print(f"Failed to retrieve page, status code: {response.status_code}")
    print()


def check_cel(urls, total_prices, part_prices):
    print()
    print(f"__________From CEL__________")
    for key, value in urls["CEL"].items():

        if value == ' ':
            print(f"{key} price: n/a")
            continue

        response = requests.get(value)

        if response.status_code == 200:

            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            price_element = soup.find('span', id='product-price')

            if price_element:
                price = price_element.get_text(strip=True)
                print(f"{key} price: {price}")

                part_prices[key]["CEL"] = price
                total_prices["CEL"] += float(price)
            else:
                print("Price not found on the page")
        else:
            print(f"Failed to retrieve page, status code: {response.status_code}")
    print()

def check_forit(urls, total_prices, part_prices):
    print(f"__________From ForIT__________")
    for key, value in urls["ForIT"].items():

        if value == ' ':
            print(f"{key} price: n/a")
            continue
                
        response = requests.get(value)

        if response.status_code == 200:

            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            price_element = soup.find('h3', class_='price-value')

            if price_element:
                price = price_element.get_text(strip=True)
                print(f"{key} price: {price}")

                cleaned_price = price.replace("lei", "").strip()
                cleaned_price = cleaned_price.replace(".", "").strip()
                cleaned_price = cleaned_price.replace(",", ".")
                part_prices[key]["ForIT"] = cleaned_price
                total_prices["ForIT"] += float(cleaned_price)
            else:
                print("Price not found on the page")
        else:
            print(f"Failed to retrieve page, status code: {response.status_code}")
    print()

def check_evomag(urls, total_prices, part_prices):
    print(f"__________From Evomag__________")
    for key, value in urls["Evomag"].items():

        if value == ' ':
            print(f"{key} price: n/a")
            continue
                
        response = requests.get(value)

        if response.status_code == 200:

            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            price_element = soup.find('div', class_='pret_rons')

            if price_element:
                main_price = soup.find('div', class_='pret_rons').contents[0].strip()
                fractional_part = soup.find('sup', class_='price_sup').text.strip()
                price = main_price + ',' + fractional_part + 'lei'
                print(f"{key} price: {price}")


                cleaned_price = price.replace("lei", "").strip()
                cleaned_price = cleaned_price.replace(".", "").strip()
                cleaned_price = cleaned_price.replace(",", ".")
                part_prices[key]["Evomag"] = cleaned_price
                total_prices["Evomag"] += float(cleaned_price)
            else:
                print("Price not found on the page")
        else:
            print(f"Failed to retrieve page, status code: {response.status_code}")
    print()


def check(urls, total_prices, part_prices):
    check_emag(urls, total_prices, part_prices)
    check_pcgarage(urls, total_prices, part_prices)
    check_cel(urls, total_prices, part_prices)
    check_forit(urls, total_prices, part_prices)
    check_evomag(urls, total_prices, part_prices)