import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd1 = random.randint(0, last)
  rnd2 = (rnd1 + random.randint(1, last)) % len(quotes)
  

  print(quotes[rnd1].replace('\n',''))
  print(quotes[rnd2].replace('\n',''))

if __name__== "__main__":
  primary()
