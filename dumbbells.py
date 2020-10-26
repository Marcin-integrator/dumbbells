from itertools import combinations
from operator import itemgetter


def weights_order(discs, amt):
    discs.sort()
    combi = []
    discs_combi = [[xix] for xix in discs]
    for quantity in range(2, amt + 1):
        combi.append(list(combinations(discs, quantity)))

    for y in range(len(combi)):
        for z in combi[y]:
            z = list(z)
            total = sum(z)
            z.append(total)
            discs_combi.append(z)

    discs_sequence = sorted(discs_combi, key=itemgetter(-1))

    list_str = '\n'.join([str(elem) for elem in discs_sequence])

    summary = ("Combinations are:\n" + list_str)

    return summary


if __name__ == "__main__":
    amount = int(input('Please type the number of discs:'))
    weights_list = []
    for x in range(amount):
        kilos = float(input('Disc weight:'))
        weights_list.append(kilos)
    res = weights_order(weights_list, amount)
    print(res)
