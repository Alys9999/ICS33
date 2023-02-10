# A decorater for speeding up recursive functions
# We will discuss memoize in a later lecture. Don't worry about its meaning/implementation
class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}

    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer

# Computes minimum distance between two words recursively
# Use memoization for dynamic programming speedup (explained later in the quarter)
@Memoize
def min_dist(a : str, b : str) -> int:
    # Levenshtein distance:: 1 for every addition, deletion, substitution
    if a == '':
        return len(b)
    elif b == '':
        return len(a)
    elif a[0] == b[0]:
        return min_dist(a[1:],b[1:])
    else:
        return 1 + min(
            min_dist(a[1:],b),
            min_dist(a,b[1:]),
            min_dist(a[1:],b[1:])
            )

    # Same basic result, but allows flip letters to count as 1: so min_dist('abc','bac') == 1 not 2
#     if a == '' or b == '':
#         return len(a)+len(b)
#     else:
#         return min(1+min_dist(a,b[1:]),                                 # drop 1st char in b
#                    1+min_dist(a[1:],b),                                 # drop 1st char in a
#                    (0 if a[0]==b[0] else 1)+ min_dist(a[1:],b[1:]),     # same or subst
#                    (1 if a[0:2] == b[1::-1] else 2) + min_dist(a[2:],b[2:]) # flip
#                    )

if __name__ == '__main__':
    print(min_dist('abc','bac'))