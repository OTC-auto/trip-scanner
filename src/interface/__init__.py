from time import sleep


def main():
    while True:
        query = input("Type 'scan' and a CSV with trips data will be created on your Desktop.")
        if query.lower() == 'scan':
            pass  # run program
            print(f"File created. Shutting down this program.")
            sleep(2)
            break
        else:
            print(f"You typed: {query}. Please type 'scan'.")


if __name__ == '__main__':
    main()
