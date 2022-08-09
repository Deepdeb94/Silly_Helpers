from sys import argv
from cs50 import get_string, get_int

def main():
   
    try:
        n = int(input("No. of scores: "))
    except ValueError:
        exit("Value Error")
    scores = []
    for i in range(n):
        score = int(input("score: "))
        scores += [score]
    average = sum(scores) / len(scores)
    print(f"Average: {average}")
    

main()