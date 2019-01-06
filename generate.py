import sys


def main(start, end):
    assert start % 10 == 0
    assert end % 10 == 9
    with open('jogos_{}-{}.txt'.format(start, end), 'w') as f:
        f.write('\n'.join(['jogos:{}-{}'.format(a, a+9)
                           for a in range(start, end, 10)]))
        f.write('\n')

if __name__ == '__main__':
    main(*[int(i) for i in sys.argv[1:]])

