def less_than_ten(list_):
    n_list = []
    for i in list_:
        if i < 10:
            n_list.append(i)

    return n_list


def less_than_x(list_, x):
    n_list = []
    for i in list_:
        if i < x:
            n_list.append(i)

    return n_list


if __name__ == '__main__':
    list_ = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    less = int(input("Enter number: "))
    list_ = less_than_x(list_, less)

    print(list_)
