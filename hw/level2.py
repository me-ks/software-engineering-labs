def main():
    with open("level1_output.txt", "r") as f:
        data = f.read()

    
    result = data.upper()

    with open("level2_output.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()