def main():
    a, b, c = map(int, input().split())
    if b - a == c - b:
        print(f'secret {b - a}')
    else:
        print("not secret")

if __name__ == "__main__":
    main()