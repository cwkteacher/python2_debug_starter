def main():
    s = "Debugging is hard but is fun!"
    first_half = s[2:15]
    second_half = s[23:28]
    final_str = first_half + second_half
    # should print: "Debugging is fun!"
    print(final_str)


if __name__ == "__main__":
    main()
