from predicate import is_prime

# int is used to test code you write below; yields 1, 2, 3, 4, ...
def ints(maxi=None):
    i = 1
    while maxi == None or i <= maxi:
        yield i
        i += 1
         
# primes is used to test code you write below; yields 2, 3, 5, 7, 11, ...
def primes(maxi=None):
    p = 2
    while maxi == None or p <= maxi:
        if is_prime(p):
            yield p
        p += 1
         
# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# A function to return the nth yielded value in iterable (1st, 2nd, ..etc)
# returns None if the iterable doesn't have n values
# Interesting to use when iterable is infinite to select a value from it
def nth(iterable, n):
    for i,v in enumerate(iterable,1):
        if i == n:
            return v
    return None


# A function to return the nth through n+mth yielded value in iterable (1st, 2nd, ..etc)
# returns None if the iterable doesn't have n+m values
# Interesting to use when iterable is infinite to select a few values from it
def nth_for_m(iterable, n, m):
    n_for_m = []
    for i,v in enumerate(iterable,1):
        if i in range(n,n+m):
            n_for_m.append(v)
        if i == n+m:
            return n_for_m
    return None


# A function decorator to "speed-up" certain kinds of recursive functions
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
 
    def reset_cache(self):
        self.cache = {}
         
    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)
