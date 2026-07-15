import requests
from bs4 import BeautifulSoup
import math

urls = {
    
    "Emag":{
        "CPU": 'https://www.emag.ro/procesor-amd-ryzentm-5-5600-4-4ghz-35mb-socket-am4-box-100-100000927box/pd/DRFWDSMBM/',
        "GPU": 'https://www.emag.ro/placa-video-asus-amd-radeontm-rx-6600-v2-dual-8gb-gddr6-128-bit-dual-rx6600-8g-v2/pd/D1H11HYBM/?ref=hdr-favorite_products',
        "RAM": 'https://www.emag.ro/memorie-kingston-fury-beast-16gb-ddr4-3200mhz-cl16-dual-channel-kit-kf432c16bbk2-16/pd/DJ2BSHMBM/',
        "Storage": 'https://www.emag.ro/ssd-wd-blue-sn580-1tb-m-2-2280-pcie-gen4-x4-nvme-tlc-read-write-4150-4150-mbps-iops-600k-750k-tb-w-600-wds100t3b0e/pd/DDPY1TYBM/',
        "Motherboard": 'https://www.emag.ro/placa-de-baza-msi-socket-am4-b550-a-pro/pd/DZB3J3MBM/',
        "PSU": 'https://www.emag.ro/sursa-corsair-rm650-650-watt-80-plus-gold-certified-fully-modular-cp-9020280-eu/pd/DHWSG3YBM/',
        "Case": 'https://www.emag.ro/carcasa-montech-xr-black-camtxrblack/pd/DQPSV6YBM/'
    },
    "PC Garage":{
        "CPU": 'https://www.pcgarage.ro/procesoare/amd/ryzen-5-5600-35ghz-box/',
        "GPU": 'https://www.pcgarage.ro/placi-video/asus/radeon-rx-6600-dual-8g-8gb-gddr6-128-bit/',
        "RAM": 'https://www.pcgarage.ro/memorii/kingston/fury-beast-16gb-ddr4-3200mhz-cl16-dual-channel-kit/',
        "Storage": 'https://www.pcgarage.ro/ssd/western-digital/blue-sn580-1tb-pci-express-40-x4-m2-2280/',
        "Motherboard": 'https://www.pcgarage.ro/placi-de-baza/msi/b550-a-pro/',
        "PSU": 'https://www.pcgarage.ro/surse/corsair/rm650-80-plus-gold-650w/',
        "Case": 'https://www.pcgarage.ro/carcase/montech/xr-black/'
    },
    "CEL":{
        "CPU": 'https://www.cel.ro/procesor-amd-ryzen-5-5600-4-4ghz-35mb-socket-am4-box-cooler-amd-wraith-stealth-pNCo0PTQpMw-l/?gad_source=1&gclid=Cj0KCQiAvvO7BhC-ARIsAGFyToWFgdBOP7tQ-7DUgR3pLmdGOD7gHD2VB9Hn4Gbu8VpE-Vg87GYsQnUaAouDEALw_wcB',
        "GPU": 'https://www.cel.ro/placa-video-asus-radeon-rx-6600-dual-v3-8gb-gddr6-128-bit-pOCswPDEuMw-l/',
        "RAM": ' ',
        "Storage": 'https://www.cel.ro/ssd-wd-blue-sn580-1tb-pci-express-4-0-x4-m-2-2280-wds100t3b0e-pOSc0NzYqMg-l/',
        "Motherboard": ' ',
        "PSU": 'https://www.cel.ro/sursa-corsair-rm650-80plus-gold-650w-full-modulara-pOSUyMDUqMQ-l/',
        "Case": ' '
    },
    "ForIT":{
        "CPU": 'https://www.forit.ro/procesoaree/amd/399105-ryzen-5-5600-3-5ghz-box/?2pau=a7c80ffd2&2ptt=quicklink&2ptu=d3e4a1c14&2pdlst=Cj0KCQiAvvO7BhC-ARIsAGFyToUdprfz61KzXIkY_F-e-f3pnRNaBP96Iw_rVfujj9op3Ng-g1PatWIaAt7_EALw_wcB&gad_source=1&gclid=Cj0KCQiAvvO7BhC-ARIsAGFyToUdprfz61KzXIkY_F-e-f3pnRNaBP96Iw_rVfujj9op3Ng-g1PatWIaAt7_EALw_wcB',
        "GPU": 'https://www.forit.ro/placi-videoo/asus/337655-radeon-rx-6600-dual-8gb-gddr6-128-bit/',
        "RAM": 'https://www.forit.ro/memorii-ram/kingston/304581-fury-beast-16gb-ddr4-3200mhz-cl16-dual-channel-kit/',
        "Storage": 'https://www.forit.ro/ssd-urii/wd/461189-blue-sn580-1tb-pci-express-4-0-x4-m-2-2280/',
        "Motherboard": 'https://www.forit.ro/placi-de-baza-/msi/285337-b550-a-pro/',
        "PSU": 'https://www.forit.ro/surse-pc/corsair/486973-rm650-80-plus-gold-650w/',
        "Case": 'https://www.forit.ro/carcase-pc/montech/573583-xr-black/'
    },
    "Evomag":{
        "CPU": 'https://www.evomag.ro/componente-pc-gaming-procesoare/amd-procesor-amd-ryzen-5-5600-3.5ghz-am4-32mb-65w-box-4028536.html',
        "GPU": 'https://www.evomag.ro/componente-pc-gaming-placi-video/asus-placa-video-asus-dual-radeon-rx-6600-v2-8gb-gddr6-128bit-2491mhz-boost-clock-1x-hdmi-2.1-3x-displayport-1.4a-pci-e-4.0-4107775.html',
        "RAM": 'https://www.evomag.ro/componente-pc-gaming-memorii/kingston-memorii-kingston-fury-beast-16gb-2x8gb-ddr4-2666mhz-cl16-dual-channel-kit-3820127.html',
        "Storage": 'https://www.evomag.ro/componente-pc-gaming-solid-state-drive-ssd/western-digital-ssd-western-digital-blue-sn580-1tb-m.2-pcie-gen4-x4-nvme-1.4b-4116714.html',
        "Motherboard": 'https://www.evomag.ro/componente-pc-gaming-placi-de-baza/msi-placa-de-baza-msi-b550-a-pro-amd-b550-am4-atx-3793226.html',
        "PSU": 'https://www.evomag.ro/componente-pc-gaming-surse-de-alimentare-pc/corsair-sursa-corsair-rm650-650-watt-80-plus-gold-certified-fully-modular-4129127.html',
        "Case": ' '
    },
} 

part_prices = {
    "CPU": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "GPU": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "RAM": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "Storage": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "Motherboard": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "PSU": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
    "Case": {
        "Emag": None,
        "PC Garage": None,
        "CEL": None,
        "ForIT": None,
        "Evomag": None,
    },
}

total_prices = {
    "Emag": 0,
    "PC Garage": 0,
    "CEL": 0,
    "ForIT": 0,
    "Evomag": 0,
}

def check_emag():
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

def check_pcgarage():
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


def check_cel():
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

def check_forit():
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

def check_evomag():
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


def check():
    check_emag()
    check_pcgarage()
    check_cel()
    check_forit()
    check_evomag()

def part_check(part):
    print()
    print(f"__________{part} prices__________")
    for key, value in part_prices[part].items():
        print(f"{key}: {value}")
    print()

def part_check_all():
    print()
    print(f"__________Individual prices__________")
    print()
    for key_, value_ in part_prices.items():
        print(f"__________{key_} prices__________")
        for key, value in part_prices[key_].items():
            print(f"{key}: {value}")
        print()
    print()

def list():
    x = 0
    for key, value in total_prices.items():
        if value != 0:
            print(f"The total price of parts available at {key} is : {value:.2f}")
            x += 1
    if(x == 0):
        print("You don't seem to have run any checks. To be able to list the prices run at least one check!")
    
def unknown():
    print("Unknown command. Check for typing mistakes!")

commands = {
    "check all": check,
    "check emag": check_emag,
    "check pcgarage": check_pcgarage,
    "check cel": check_cel,
    "check forit": check_forit,
    "check evomag": check_evomag,
    "cpu price": lambda: part_check("CPU"),
    "gpu price": lambda: part_check("GPU"),
    "ram price": lambda: part_check("RAM"),
    "storage price": lambda: part_check("Storage"),
    "motherboard price": lambda: part_check("Motherboard"),
    "psu price": lambda: part_check("PSU"),
    "case price": lambda: part_check("Case"),
    "all price": part_check_all,
    "list": list
}

while(1):
    com = input("Enter a command: ").lower()

    if com == "exit":
        print("Exiting...")
        break
    command = commands.get(com, unknown)
    command()