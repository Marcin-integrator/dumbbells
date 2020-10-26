def weights_order(discs, amt):
    discs.sort()
    for d in range(amt - 1):
        xy = discs[d] + discs[d + 1]
        discs.append(f"{discs[d + 1]} + {discs[d]} = {xy}")

    list_str = '\n'.join([str(elem) for elem in discs])

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
