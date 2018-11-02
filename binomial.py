#!/usr/bin/env python
"""This module retuns the binomial coefficient (n choose k) using
two functions. The first, logfactorial(), calculates log(n!/k!), and the
second function, choose(), calculates the binomial coefficient as either
an integer or its log."""

import argparse
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("-l", "--log", action="store_true", help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()
binom_coef = False if args.log else True

# test argument problems early:
if not args.test and __name__ == '__main__':
    if args.n<0:
        raise Exception("argument -n must be 0 or positive")
    # no error if file imported as module

import math

def logfactorial(n=args.n, k=args.k):
    """This function takes input values n and k, which must be 
    positive integers, and calculates log (n factorial / k factorial).
    k is 0 by default.
    Requires "math" to be imported beforehand.
    Examples:

    >>> logfactorial(5, 1)
    4.787491742782046
    >>> logfactorial(5, 3)
    2.995732273553991
    >>> logfactorial(5, 4)
    1.6094379124341003
    >>> logfactorial(5, 6)
    0.0
    >>> logfactorial(5, 5)
    0.0
    """
    assert type(n) == int, "n is not an integer"
    assert type(k) == int, "k is not an integer"
    assert n >= 0, "n must be non-negative"
    assert k >= 0, "k must be non-negative"
    log_nk = float()
    for index in range(k, n):
        log_nk += math.log(index + 1)
    return log_nk

def choose(n=args.n, k=args.k, binom_coef=binom_coef):
    """This function takes input values n, k, and binom_coef and 
    calculates n choose k (binomial coefficient). n and k must be 
    positive integers. binom_coef is true by default. If true, the
    function returns the integer value of the binomial coefficient; 
    if false, the function returns its log.
    Requires "math" to be imported beforehand and the logfactorial()
    equation to be defined.
    Examples:

    >>> choose(5, 1)
    5
    >>> choose(5, 1, True)
    5
    >>> choose(5, 1, False)
    1.60943791243
    >>> choose(5, 2)
    10
    >>> choose(5, 3)
    10
    >>> choose(5, 3, False)
    2.30258509299
    >>> choose(5, 4)
    5
    >>> choose(5, 5)
    1
    
    """
    assert type(n) == int, "n is not an integer"
    assert type(k) == int, "k is not an integer"
    assert n >= 0, "n must be non-negative"
    assert k >= 0, "k must be non-negative"
    assert n >= k, "n must be greater than or equal to k"
    log_nminusk = float()
    for index in range(k, n):
        log_nminusk += math.log(index + 1 - k)
    total = logfactorial(n, k) - log_nminusk
    result = int(round(math.exp(total))) if binom_coef else total
    print(result)

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")    

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        choose()
