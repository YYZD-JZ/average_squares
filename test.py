from squares import average_of_squares


def average_squares(list_of_numbers, list_of_weights=None):
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights need to be same length as the numbers"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * list_of_weights
    squares = [weight * number * numer
        for number, weight in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)/len(squares)

def convert_numbers(list_of_strings):
    all_numbers = []
    for s in list_of_strings:
        all_numbers.extend([token.split() for token in s.split])
    return [int(number_string) for number_string in all_numbers]

if __name__ == "__main__":
    num_strings =  ["1", "2", "4"]
    weight_strings = ["1", "1", "1"]
    numbers = convert_numbers(num_strings)
    weights = convert_numbers(weight_strings)

    result = average_of_squares(numbers, weights)
    print(result)