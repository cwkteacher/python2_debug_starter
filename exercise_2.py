def main():
    counter = 0
    index = 0
    list_of_10s = []
    while counter <= 100:
        list_of_10s.insert(index, counter)
        counter = counter + 5
    # should print: "0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100"
    print(list_of_10s)


if __name__ == "__main__":
    main()
