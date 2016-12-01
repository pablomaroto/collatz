#########################
#   Pablo Maroto Lopez  #
#   Python 2.7.12       #
#########################

import sys

def collaz(num):
    if num != 1:
        if num %2 == 0:
            num=num/2
        else:
            num = num*3+1

        print num
        collaz(num)


def check(num):
    try:
        num=int(num)
    except ValueError:
        print "Error: numero invalido"
        sys.exit(0)

    if num < 1:
        print "Error: numero invalido"
        sys.exit(0)

    return num


if len(sys.argv) > 2:
    print "Error: 1 argumento max"
    sys.exit(0)

elif len(sys.argv) == 2:
    num=sys.argv[1]
    num=check(num)

else:
    num=raw_input("Introduce un numero natural positivo: ")
    num=check(num)

print num
collaz(num)
