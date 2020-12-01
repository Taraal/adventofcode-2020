TARGET = 2020
TEST_TWO_RESULT = 514579
TEST_THREE_RESULT = 241861950

test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

with open("input.txt") as input_file:
    input_list = [int(i) for i in input_file]

def two_sum(input):
    input_set = set(input)
    for num in input_set:
        if TARGET - num in input_set:
            return (TARGET - num) * num

def three_sum(input):
    input_set = set(input)
    for i in input_set:
        for j in input_set:
            if (TARGET - i - j) in input_set:
                return (TARGET - i - j) * i * j

assert two_sum(test_input) == TEST_TWO_RESULT
assert three_sum(test_input) == TEST_THREE_RESULT
print(two_sum(input_list))
print(three_sum(input_list))