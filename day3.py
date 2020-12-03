def partOne():
    with open("input.txt") as input_file:
        input_list = input_file.read().splitlines()

    idx = 0
    nb_trees = 0
    for iline, line in enumerate(input_list):
        input_list[iline] = [char for char in line]
        if input_list[iline][idx]  == "#":
            print(idx)
            nb_trees += 1
        idx += 3
        if idx > len(input_list[iline]) - 1:
            idx = idx - len(input_list[iline])

    return nb_trees

def get_nb_trees(horiz_slope, vert_slope):
    with open("input.txt") as input_file:
        input_list = input_file.read().splitlines()

    horiz_idx = 0
    nb_trees = 0
    vert_idx = 0
    while vert_idx < len(input_list) - 1:
        input_list[vert_idx] = [char for char in input_list[vert_idx]]
        if input_list[vert_idx][horiz_idx] == "#":
            nb_trees += 1
        horiz_idx += horiz_slope
        if horiz_idx > len(input_list[vert_idx]) - 1:
            horiz_idx = horiz_idx - len(input_list[vert_idx])
        
        vert_idx += vert_slope

    return nb_trees


def partTwo():

    res_1 = get_nb_trees(1, 1)
    res_2 = get_nb_trees(3, 1)
    res_3 = get_nb_trees(5, 1)
    res_4 = get_nb_trees(7, 1)
    res_5 = get_nb_trees(1, 2)


    return res_1*res_2*res_3*res_4*res_5



print("Part one : ", partOne())
print("Part two : ", partTwo())