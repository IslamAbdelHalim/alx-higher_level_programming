x = 'wwwoooorrrldd'

def my_function(x):
  if len(x) == 1:
    return x
  if x[0] == x[1]:
    return my_function(x[1:])
  else:
    return x[0] + my_function(x[1:])

word = my_function(x)
print(word)