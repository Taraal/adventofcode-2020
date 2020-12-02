def partOne():
    with open("input.txt") as input_file:
        input_list = input_file.read().splitlines()


    correct_passwords = 0
    for line in input_list:

        # Can't get uglier 

        data = line.split(":")
        password = data[1]
        limit = data[0]
        letter = limit[-1]
        limit = limit[:-1]

        limit_list = limit.split("-")
        lower_bound = limit_list[0]
        upper_bound = limit_list[1]

        occurences = password.count(letter)
        if occurences >= int(lower_bound) and occurences <= int(upper_bound):
            correct_passwords += 1
        
    return correct_passwords

def partTwo():
    with open("input.txt") as input_file:
        input_list = input_file.read().splitlines()


    correct_passwords = 0
    for line in input_list:

        # If it ain't broken, don't fix it 
        data = line.split(":")
        password = data[1].replace(" ", "")
        limit = data[0]
        letter = limit[-1]
        limit = limit[:-1]

        index_list = limit.split("-")
        first_index = int(index_list[0]) - 1
        last_index = int(index_list[1]) - 1

        logic_gate = False
        if password[first_index] == letter: 
            logic_gate = not logic_gate
        if password[last_index] == letter:
            logic_gate = not logic_gate
        if logic_gate:
            correct_passwords = correct_passwords + 1

    return correct_passwords

print("Part one : ", partOne())
print("Part two : ", partTwo())