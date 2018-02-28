import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build a diamond')
    parser.add_argument('integer', metavar='N', type=int,
                    help='an integer for the accumulator')
    args = parser.parse_args()
    n = args.integer
    print("running diamond program with integer {}".format(n))
    
    for row in list(range(n)):
        if row == 0:
            print("*" * (n-1) + str(n) + "*" * (n-1))
        else:
            num_out=(n-1-row)
            num_in=((2 * row) - 1)
            print("*" * num_out + str(n) + '*' * num_in + str(n) + '*' * num_out)

        