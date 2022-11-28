import timeit
def getSpendingForCategory(lines_read, category_type):
    result = []
    for line_i in lines_read:
        if not line_i:
            continue
        line_entries = line_i.split(",")
        if line_entries[1].strip() == category_type:
            result.append(
                {"Date": line_entries[0].strip(), "Amount": line_entries[2].strip()}
            )
    return result


if __name__ == "__main__":
    with open("spending.csv") as file:
        lines_read = file.read().splitlines()
        time_to_run = timeit.timeit('getSpendingForCategory(lines_read, "Groceries")', number=int(1e6), globals=globals())
        print(time_to_run)
        print(getSpendingForCategory(lines_read, "Groceries"))
