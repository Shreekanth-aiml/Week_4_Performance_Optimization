def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


numbers = list(range(1000)) * 2

duplicates = find_duplicates(numbers)

print("Number of duplicates:", len(duplicates))