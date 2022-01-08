def create_3x3(tab, x, y):
    tab1 = []
    cx = 0
    cy = 0

    if x <= 2 and y <= 2:  # sektor 1
        cx = cy = 0
        x = y = 2
    elif 3 <= x <= 5 and y <= 2:  # sektor 2
        cx = 3
        cy = 0
        x = 5
        y = 2
    elif 6 <= x <= 8 and y <= 2:  # sektor 3
        cx = 6
        cy = 0
        x = 8
        y = 2

    elif x <= 2 and 3 <= y <= 5:  # sektor 4
        cx = 0
        cy = 3
        x = 2
        y = 5
    elif 3 <= x <= 5 and 3 <= y <= 5:  # sektor 5
        cx = 3
        cy = 3
        x = 5
        y = 5
    elif 6 <= x <= 8 and 3 <= y <= 5:  # sektor 6
        cx = 6
        cy = 3
        x = 8
        y = 5

    elif x <= 2 and 6 <= y <= 8:  # sektor 7
        cx = 0
        cy = 6
        x = 2
        y = 8
    elif 3 <= x <= 5 and 6 <= y <= 8:  # sektor 8
        cx = 3
        cy = 6
        x = 5
        y = 8
    elif 6 <= x <= 8 and 6 <= y <= 8:  # sektor 9
        cx = 6
        cy = 6
        x = 8
        y = 8

    while cx <= x and cy <= y:
        tab1.append(tab[cy][cx])

        if cx == x and cy < y:
            cy += 1
            cx -= 3

        cx += 1

    return tab1


def check_point(tab, x, y, value):
    i = 0

    tab1 = create_3x3(tab, x, y)

    if value in tab1:
        return False

    while i <= 8:
        if tab[y][i] == value:
            return False
        if tab[i][x] == value:
            return False
        i += 1

    return True


def matching_numbers(value, tab, cx, cy):
    while value <= 9:
        if check_point(tab, cx, cy, value):
            tab[cy][cx] = value
            break

        value += 1

    if tab[cy][cx] == 0:
        return True

    return False


<<<<<<< HEAD
def typing(tab):
=======
def write_list(tab):
>>>>>>> 77ded23d6545a5cb5d6852daddab02c0e543274b
    tabw = []
    cx = 0
    cy = 0
    j = 0
    while cx <= 8 and cy <= 8:
        if tab[cy][cx] == 0:
            tabw.append([cx, cy])

        if cx == 8 and cy < 8:
            cy += 1
            cx = -1

        cx += 1

    while j < len(tabw):
        c = tabw[j]
        cx = c[0]
        cy = c[1]
        value = tab[cy][cx] + 1
        if tab[cy][cx] >= 1:
            tab[cy][cx] = 0
        if matching_numbers(value, tab, cx, cy):
            j -= 2
        j += 1


if __name__ == "__main__":
    #         0  1  2     3  4  5      6  7  8
    # tab = [[0, 0, 0,    0, 0, 0,     0, 0, 0],     # 0
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 1
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 2
    #
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 3
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 4
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 5
    #
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 6
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0],     # 7
    #        [0, 0, 0,    0, 0, 0,     0, 0, 0], ]   # 8

    # tab = [[3, 0, 0, 1, 0, 0, 0, 0, 7],  # 0
    #        [8, 4, 0, 5, 9, 0, 0, 6, 1],  # 1
    #        [0, 5, 1, 0, 0, 0, 9, 3, 0],  # 2
    #
    #        [0, 0, 0, 4, 0, 8, 0, 5, 9],  # 3
    #        [0, 1, 0, 0, 0, 0, 0, 7, 0],  # 4
    #        [5, 2, 0, 7, 0, 6, 0, 0, 0],  # 5
    #
    #        [0, 8, 5, 0, 0, 0, 3, 1, 0],  # 6
    #        [1, 7, 0, 0, 3, 5, 0, 2, 6],  # 7
    #        [6, 0, 0, 0, 0, 1, 0, 0, 5], ]  # 8

<<<<<<< HEAD
    # writing to the blackboard
=======
    # write_list do tablicy
>>>>>>> 77ded23d6545a5cb5d6852daddab02c0e543274b
    tab = []
    quantity = 0
    while quantity < 9:
        print(quantity)
        liczba_str = input(">> ")
        if liczba_str != '':
            for j in liczba_str.split(" "):
                tab.append(int(j))
            quantity += 1


    tab = [[tab[i * 9 + j] for j in range(9)] for i in range(9)]

    for i in tab:
        print(i)

<<<<<<< HEAD
    typing(tab)
=======
    write_list(tab)

>>>>>>> 77ded23d6545a5cb5d6852daddab02c0e543274b

    # displaying the results
    print("\n\n\n")
    space = 1
    tabulator = 1
    for i in tab:
        for j in i:
            print(j, end="  ")
            if tabulator % 3 == 0:
                print("\t", end="")
            tabulator += 1
        print("")
        if space % 3 == 0:
            print("")
        space += 1
