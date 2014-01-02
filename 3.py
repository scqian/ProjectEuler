import sys
import math

def main():
  toFactor = 600851475143
  limit = math.trunc(math.sqrt(toFactor))
  factors = []
  primeFactors = []
  for i in range(1, limit):
    if toFactor % i == 0:
	  factors.append(i)
	  factors.append(toFactor/i)
  for factor in factors:
    if isPrime(factor):
      primeFactors.append(factor)
  print factors;

def isPrime(n):
  count = 0
  limit = math.trunc(math.sqrt(n))
  for i in range(1,limit + 1):
    if n % i == 0:
	  count += 1
  return count == 2

if __name__ == '__main__':
  main()