import math
import sys

def main():
  count = 1
  num = 3
  goal = 10001
  while count != goal:
    if isPrime(num): 
      count += 1
    num += 2
  print num - 2

def isPrime(n):
  count = 0
  i = 1
  while i * i <= n:
    if n%i == 0: count += 1
    i += 1
  return count == 1

if __name__ == '__main__':
  main()
