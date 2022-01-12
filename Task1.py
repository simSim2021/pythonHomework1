# Задание 1.4. по номеру месяца напечатать пору года
def season(m):
    if m == 12 or m == 1 or m == 2:
        return "It is Winter"

    elif m == 3 or m == 4 or m == 5:
        return "It is Spring"

    elif m == 6 or m == 7 or m == 8:
        return "It is Summer"

    elif m == 9 or m == 10 or m == 11:
        return "It is Autumn"

    elif m == 0 or m > 12:
        return "There is no such month"


result = season(int(input("Enter month's number: ")))

print(result)
