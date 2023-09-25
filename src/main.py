def main():
    
    # Page 212
    # Q7.
    ArrayTwoD = [
        [3, 6, 7],
        [4, 8, 1],
        [9, 3, 8],
    ]

    total = 0
    for i in range(len(ArrayTwoD)):
        for j in range(len(ArrayTwoD[i])):
            total += ArrayTwoD[i][j]
    print(total)

    # Page 213
    # Q8
    for i in range(len(ArrayTwoD)):
        for j in range(len(ArrayTwoD[i])):
            ArrayTwoD[i][j] *= 5
    print(ArrayTwoD)

    # Page 213
    # Q9
    picture = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(len(picture)):
        for j in range(len(picture[i])):
            el = picture[i][j]
            print(el if el != 0 else " ", end="")
        print()

    # Page 213
    # Q10
    for i in range(len(picture)):
        for j in range(len(picture[i])):

            if picture[i][j] == 0:
                print(" ", end="")
                continue

            adjacent = False

            if i > 0:
                adjacent = picture[i-1][j] == 0
            if i < len(picture) - 1 and not adjacent:
                adjacent = picture[i+1][j] == 0
            if j > 0 and not adjacent and not adjacent:
                adjacent = picture[i][j-1] == 0
            if j < len(picture[i]) - 1 and not adjacent:
                adjacent = picture[i][j+1] == 0

            print("1" if adjacent else " ", end="")
            
        print()

    # Page 213
    # Q11
    dark = 0
    perimetre = 0

    for i in range(len(picture)):
        for j in range(len(picture[i])):

            if picture[i][j] == 0:
                continue

            dark += 1

            adjacent = False

            if i > 0:
                adjacent = picture[i-1][j] == 0
            if i < len(picture) - 1 and not adjacent:
                adjacent = picture[i+1][j] == 0
            if j > 0 and not adjacent and not adjacent:
                adjacent = picture[i][j-1] == 0
            if j < len(picture[i]) - 1 and not adjacent:
                adjacent = picture[i][j+1] == 0

            if adjacent:
                perimetre += 1
            
    print(dark / perimetre)


if __name__ == "__main__":
    main()