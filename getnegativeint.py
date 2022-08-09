def main():

    n = get_negative()

    print(f"{n:.2f}")
    exit("Program went successful")

def get_negative():
    while True:
        try:
            i = int(input("Give me a negative integer: "))
            if i >= 0:
                continue
        except ValueError:
            print("That's not a number: ")
        else:
            return i
main()