'''def fibbonacaci(n):
    if n in [1,2]:
        return 1

    seq = [1,1]
    x=0
    while len(seq) < n:
        seq.append(seq[x] + seq[x+1])
        print seq
        x=x+1
    return seq[len(seq)-1]


print fibbonacaci(1)
print fibbonacaci(2)
print fibbonacaci(10)
'''


def is_palindrome(word):
  first_half = None
  second_half = None
  #print word
  #word.replace(' ','')
  #print word
 
  if len(word) % 2 == 0:
    first_half = len(word) / 2
    second_half = len(word) / 2
  else:
    first_half = (len(word) / 2) +1
    second_half = (len(word) / 2)

  first_half = word[:first_half]
  second_half = word[second_half:]
  second_half = second_half[::-1]
 
  if first_half == second_half: 
    print word + ' is a palindrome!'
  else:
    print word + ' is not a palindrome...'
 
is_palindrome('kayak')
is_palindrome('race car')
is_palindrome('katniss everdeen')
