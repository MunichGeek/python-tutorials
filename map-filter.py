def getSpendingForCategory(lines_read, category_type):
    return list(map(lambda x: {"Date": x[0].strip(), "Amount": x[2].strip()},
                filter(lambda x: x[1].strip() == category_type,
                    map(lambda x: x.split(","), filter(lambda x: x, lines_read)))))


if __name__ == "__main__":
    with open("spending.csv") as file:
        print(getSpendingForCategory(file.read().splitlines(), "Groceries"))
