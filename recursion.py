
def main():
    brick(5)
    
def brick(n):
    if n <= 0:
        return
    brick(n - 1)
    for i in range(n):
        print("#", end="")
    print()
        
main()