from commands import commands 
from commands import unknown

def main():
    while(1):
        com = input("Enter a command: ").lower()

        if com == "exit":
            print("Exiting...")
            break
        command = commands.get(com, unknown)
        command()

if __name__ == "__main__":
    main()