def less_than_ten(list_):
    n_list = []
    for i in list_:
        if i < 10:
            n_list.append(i)

    return n_list



if __name__ == '__main__':
    list_ = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_ = less_than_ten(list_)

    print(list_)
