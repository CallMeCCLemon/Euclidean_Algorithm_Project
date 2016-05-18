

def main():
    # gcd()
    phi_function()


def gcd():
    number_1 = int(raw_input('Input first integer: '))
    number_2 = int(raw_input('Input second integer: '))
    gcd = calculate_gcd(number_1, number_2, True)
    print 'GCD for {0} and {1}: {2}'.format(number_1, number_2, gcd)


def calculate_gcd(number_1, number_2, show_work=False):
    numbers = [number_1, number_2]
    while max(numbers) % min(numbers) != 0:
        # This print statement shows work.
        if show_work:
            print "{0} = q_1 * {1} + r_1".format(max(numbers), min(numbers))
        numbers[numbers.index(max(numbers))] = max(numbers) % min(numbers)
    return min(numbers)


def phi_function():
    number = int(raw_input('Input integer for phi function: '))
    phi = calculate_phi(number)
    print 'Phi({0}) = {1}'.format(number, phi)


def calculate_phi(number):
    return_value = 0
    temp = []
    for count in range(1, number):
        temp.append(number)
    results = map(calculate_gcd, range(1, number), temp)
    for value in results:
        if value == 1:
            return_value += 1
    return return_value


if __name__ == '__main__':
    main()
