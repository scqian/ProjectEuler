def main():
  sum = 0
  previous = 0
  current = 1
  temp = previous
  while current < 4e6:
    if current % 2 == 0: sum += current
    temp = previous
    previous = current
    current += temp
  print sum
  
if __name__ == '__main__':
  main()
    