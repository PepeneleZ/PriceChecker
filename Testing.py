import requests
from bs4 import BeautifulSoup

urls = {
    
    "Vexio":{
        "CPU": 'https://www.forit.ro/procesoaree/amd/399105-ryzen-5-5600-3-5ghz-box/?2pau=a7c80ffd2&2ptt=quicklink&2ptu=d3e4a1c14&2pdlst=Cj0KCQiAvvO7BhC-ARIsAGFyToUdprfz61KzXIkY_F-e-f3pnRNaBP96Iw_rVfujj9op3Ng-g1PatWIaAt7_EALw_wcB&gad_source=1&gclid=Cj0KCQiAvvO7BhC-ARIsAGFyToUdprfz61KzXIkY_F-e-f3pnRNaBP96Iw_rVfujj9op3Ng-g1PatWIaAt7_EALw_wcB',
        "GPU": 'https://www.forit.ro/placi-videoo/asus/337655-radeon-rx-6600-dual-8gb-gddr6-128-bit/',
        "RAM": 'https://www.forit.ro/memorii-ram/kingston/304581-fury-beast-16gb-ddr4-3200mhz-cl16-dual-channel-kit/',
        "Storage": 'https://www.forit.ro/ssd-urii/wd/461189-blue-sn580-1tb-pci-express-4-0-x4-m-2-2280/',
        "Motherboard": 'https://www.forit.ro/placi-de-baza-/msi/285337-b550-a-pro/',
        "PSU": 'https://www.forit.ro/surse-pc/corsair/486973-rm650-80-plus-gold-650w/',
        "Case": 'https://www.forit.ro/carcase-pc/montech/573583-xr-black/'
    }
}
total_prices = {
    "Vexio": 0
}

print()
for key_, value_ in urls.items():
    if key_ == 'Vexio':
        print(f"__________From {key_}__________")
        for key, value in value_.items():

            
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
                    total_prices[key_] += float(cleaned_price)
                else:
                    print("Price not found on the page")
            else:
                print(f"Failed to retrieve page, status code: {response.status_code}")
        print()

for key, value in total_prices.items():
    print(f"The total price of parts available at {key} is : {value:.2f}")