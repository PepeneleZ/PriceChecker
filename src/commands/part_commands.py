def part_check(part, part_prices):
    print()
    print(f"__________{part} prices__________")
    found_prices = False
    for key, value in part_prices[part].items():
        if value is not None:
            print(f"{key}: {value}")
            found_prices = True
    if not found_prices:
        print("No available prices to show.")
    print()

def part_check_all(part_prices):
    print()
    print(f"__________Individual prices__________")
    print()
    for key_, value_ in part_prices.items():
        print(f"__________{key_} prices__________")
        found_prices = False
        for key, value in part_prices[key_].items():
            if value is not None:
                print(f"{key}: {value}")
                found_prices = True
        if not found_prices:
            print("No available prices to show.")
        print()
    print()