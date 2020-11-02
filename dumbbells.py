from itertools import combinations
from operator import itemgetter


def weights_order(discs, amt):
    discs.sort()
    combi = []
    discs_combi = [[xix] for xix in discs]
    for quantity in range(2, amt + 1):
        combi.append(list(combinations(discs, quantity)))

    for total_lenght in range(len(combi)):
        for spec_combi in combi[total_lenght]:
            spec_combi = list(spec_combi)
            total = sum(spec_combi)
            spec_combi.append(total)
            discs_combi.append(spec_combi)

    discs_sequence = sorted(discs_combi, key=itemgetter(-1))

    discs_string = []

    for weights in discs_sequence:
        curr_str = ''
        if len(weights) == 1:
            discs_string.append(f"{str(weights[0])}")
        else:
            for weight in weights[:-1]:
                curr_str = f" + {weight}" + curr_str
            curr_str = curr_str.lstrip('+ ')
            curr_str += f" = {weights[-1]}"
            discs_string.append(curr_str)

    list_str = '\n'.join([str(elem) for elem in discs_string])

    summary = ("Combinations are:\n" + list_str)

    return summary


if __name__ == "__main__":
    amount = int(input('Please type the number of discs:'))
    weights_list = []
    for x in range(amount):
        kilos = float(input('Disc weight (in kg):'))
        weights_list.append(kilos)
    RESULT = weights_order(weights_list, amount)
    print(RESULT)
