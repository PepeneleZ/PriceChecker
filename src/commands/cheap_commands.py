def cheap(part, part_prices):

    filtered_prices = {key: value for key, value in part_prices[part].items() if value is not None}

    if filtered_prices:
        key, value = min(filtered_prices.items(), key=lambda item: float(item[1]))
        print(f"The cheapest {part} is {value} and can be found at {key}.")
    else:
        print("You don't seem to have run any checks. You have to run checks so there are prices to be compared!")
    print()

def cheap_all(part_prices):
    for key_, value_ in part_prices.items():

        filtered_prices = {key: value for key, value in value_.items() if value is not None}

        if filtered_prices:
            key, value = min(filtered_prices.items(), key=lambda item: float(item[1]))
            print(f"The cheapest {key_} is {value} and can be found at {key}.")
        else:
            print("You don't seem to have run any checks. You have to run checks so there are prices to be compared!")
    print()

def cheap_build(part_prices):
    total = 0
    priced_parts = 0
    for key_, value_ in part_prices.items():

        filtered_prices = {key: value for key, value in value_.items() if value is not None}

        if filtered_prices:
            _, value = min(filtered_prices.items(), key=lambda item: float(item[1]))
            total += float(value)
            priced_parts += 1
        else:
            print("You don't seem to have run any checks. You have to run checks so there are prices to be compared!") 
            break
    if priced_parts == len(part_prices):
        print(f"The cheapest build would cost {total:.2f}.")   
    print()