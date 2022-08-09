def main():
    
    x = get_int()
    print(f"X is {x}")
    

def get_int():
    
    while True:
        try:
            n = int(input("Type a integer: "))
        except ValueError:
            print("n is not an integer: ")
        else:
            return n


main()
