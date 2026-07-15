from config.commands_dict import execute_command

def main():
    while(1):
        com = input("Enter a command: ").strip()

        if com.lower() == "exit":
            print("Exiting...")
            break
        if not com:
            print("Please enter a command.")
            print()
            continue

        execute_command(com)

if __name__ == "__main__":
    main()