import random

def primary():
  quote = raw_input('Write your quote : ')

  f = open("quotes.txt", "a+")
  f.write(quote+"\n")
  f.close()

if __name__== "__main__":
  primary()
