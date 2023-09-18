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
            print()


if __name__ == "__main__":
    main()