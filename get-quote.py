def primary():
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13],quotes[14])

if __name__== "__main__":
  primary()