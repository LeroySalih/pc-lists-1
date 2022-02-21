from difflib import Differ
from colorama import Fore, Style


def displayDif(expected, actual):
  
  expected = expected.decode("UTF-8")
  actual = actual.decode("UTF-8")

  delta = Differ().compare(expected, actual)


  for dif in delta:
    if(dif[0] == "+"):
      print(Fore.GREEN + dif[2], end="")
    elif(dif[0] == "-"):
      print(Fore.RED + dif[2], end="")
    else:
      print(Fore.WHITE + dif[2], end="")

if __name__ == "__main__":
  exp = b"abcd."
  act = b"abcd"

  displayDif(exp, act)