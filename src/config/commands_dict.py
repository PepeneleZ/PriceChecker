from commands.check_commands import check_all, check_store
from commands.part_commands import part_check, part_check_all
from commands.util_commands import list_prices, list_commands, help_commands, unknown
from commands.cheap_commands import cheap, cheap_all, cheap_build
from commands.manage_commands import add_store, set_url, list_stores
from config.data import urls, total_prices, part_prices, store_configs, get_store_key, get_part_key


def execute_command(command_text):
    command_text = command_text.strip()
    command_lower = command_text.lower()

    if command_lower == "check all":
        check_all(urls, total_prices, part_prices, store_configs)
        return

    if command_lower.startswith("check "):
        store_input = command_text[6:].strip()
        store_key = get_store_key(store_input)
        if not store_key:
            print("Store not found.")
            print()
            return
        check_store(store_key, urls, total_prices, part_prices, store_configs)
        return

    if command_lower == "price all":
        part_check_all(part_prices)
        return

    if command_lower.startswith("price "):
        part_input = command_text[6:].strip()
        part_key = get_part_key(part_input)
        if not part_key:
            print("Part not found.")
            print()
            return
        part_check(part_key, part_prices)
        return

    if command_lower == "cheap all":
        cheap_all(part_prices)
        return

    if command_lower == "cheap build":
        cheap_build(part_prices)
        return

    if command_lower.startswith("cheap "):
        part_input = command_text[6:].strip()
        part_key = get_part_key(part_input)
        if not part_key:
            print("Part not found.")
            print()
            return
        cheap(part_key, part_prices)
        return

    if command_lower == "list prices":
        list_prices(total_prices)
        return

    if command_lower == "list stores":
        list_stores()
        return

    if command_lower == "list commands":
        list_commands()
        return

    if command_lower == "help":
        help_commands()
        return

    if command_lower.startswith("help "):
        help_commands(command_text[5:].strip())
        return

    if command_lower.startswith("add store "):
        add_store(command_text[10:].strip())
        return

    if command_lower.startswith("set url "):
        set_url(command_text[8:].strip())
        return

    if command_lower.startswith("add url "):
        set_url(command_text[8:].strip())
        return

    unknown()
