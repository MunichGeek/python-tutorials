import timeit
def getSpendingForCategory(lines_read, category_type):
    return list(map(lambda x: {"Date": x[0].strip(), "Amount": x[2].strip()},
                filter(lambda x: x[1].strip() == category_type,
                    map(lambda x: x.split(","), filter(lambda x: x, lines_read)))))


if __name__ == "__main__":
    with open("spending.csv") as file:
        lines_read = file.read().splitlines()
        time_to_run = timeit.timeit('getSpendingForCategory(lines_read, "Groceries")', number=int(1e6), globals=globals())
        print(time_to_run)
        print(getSpendingForCategory(lines_read, "Groceries"))
