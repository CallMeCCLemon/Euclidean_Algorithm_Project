

def main():
    # gcd()
    # phi_function()
    print "RSA Homework:"
    print "Problem 1:"
    print "***A) p=3, q=11, e=7, M=5***"
    rsa_encrypt(3*11, 7, 5)
    print "***B) p=5, q=11, e=3, M=9***"
    rsa_encrypt(5*11, 3, 9)
    print "***C) p=7, q=11, e=17, M=8***"
    rsa_encrypt(7*11, 17, 8)
    print "***D) p=11, q=13, e=11, M=7***"
    rsa_encrypt(11*13, 11, 7)

    print "Problem 2:"
    print "***n=35, e=5, encrypted_message = 10***"
    rsa_decrypt(35, 5, 10)


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


def rsa_encrypt(n, e, m):
    phi_n = calculate_phi(n)
    d = 0
    while (e * d) % phi_n != 1:
        d += 1
    print "Public Key (e, n): ({0}, {1})".format(e, n)
    print "Private Key: d = {0}".format(d)
    print "Encrypting Message = {0}.".format(m)
    encrypted_message = (m**e) % n
    print "Encrypted Message = {0}.\n".format(encrypted_message)
    rsa_decrypt(n, e, encrypted_message)


def rsa_decrypt(n, e, m):
    phi_n = calculate_phi(n)
    d = 0
    while (e * d) % phi_n != 1:
        d += 1
    print "Public Key (e, n): ({0}, {1})".format(e, n)
    print "Private Key: d = {0}".format(d)
    print "Decrypting Message = {0}.".format(m)
    decrypted_message = (m**d) % n
    print "Decrypted Message = {0}.\n".format(decrypted_message)

if __name__ == '__main__':
    main()
