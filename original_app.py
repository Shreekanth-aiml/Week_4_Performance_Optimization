def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])

    return duplicates


numbers = list(range(1000)) * 2

duplicates = find_duplicates(numbers)

print("Number of duplicates:", len(duplicates))