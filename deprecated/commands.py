from scraping import check, check_cel, check_emag, check_evomag, check_forit, check_pcgarage
from data import urls, total_prices, part_prices

def part_check(part, part_prices):
    print()
    print(f"__________{part} prices__________")
    for key, value in part_prices[part].items():
        print(f"{key}: {value}")
    print()

def part_check_all(part_prices):
    print()
    print(f"__________Individual prices__________")
    print()
    for key_, value_ in part_prices.items():
        print(f"__________{key_} prices__________")
        for key, value in part_prices[key_].items():
            print(f"{key}: {value}")
        print()
    print()

def list(total_prices):
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
    "check all": lambda: check(urls, total_prices, part_prices),
    "check emag": lambda: check_emag(urls, total_prices, part_prices),
    "check pcgarage": lambda: check_pcgarage(urls, total_prices, part_prices),
    "check cel": lambda: check_cel(urls, total_prices, part_prices),
    "check forit": lambda: check_forit(urls, total_prices, part_prices),
    "check evomag": lambda: check_evomag(urls, total_prices, part_prices),
    "cpu price": lambda: part_check("CPU", part_prices),
    "gpu price": lambda: part_check("GPU", part_prices),
    "ram price": lambda: part_check("RAM", part_prices),
    "storage price": lambda: part_check("Storage", part_prices),
    "motherboard price": lambda: part_check("Motherboard", part_prices),
    "psu price": lambda: part_check("PSU", part_prices),
    "case price": lambda: part_check("Case", part_prices),
    "all price": lambda: part_check_all(part_prices),
    "list": lambda: list(total_prices)
}