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
        print(getSpendingForCategory(file.read().splitlines(), "Groceries"))
