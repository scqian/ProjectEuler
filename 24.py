import math
import sys
import itertools

def main():
    perms = [''.join(p) for p in itertools.permutations('0123456789')]
    sPerms = sorted(perms)
    print sPerms[1000000 - 1]

'''def perm(elem):
    if len(elem) <=1:
        yield elements
    else:
        for perm in all_perms(elem[1:]):
            for i in range(len(elem)):
                yield perm[:i] + elem[0:1] + perm[i:]'''

    
if __name__ == '__main__':
    main()
