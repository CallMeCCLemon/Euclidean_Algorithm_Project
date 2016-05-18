

def main():
    numbers = []
    numbers.append(int(raw_input('Input first integer: ')))
    numbers.append(int(raw_input('Input second integer: ')))
    while max(numbers) % min(numbers) != 0:
        print "{0} = q_1 * {1} + r_1".format(max(numbers), min(numbers))
        numbers[numbers.index(max(numbers))] = max(numbers) % min(numbers)

    print min(numbers)


if __name__ == '__main__':
    main()
