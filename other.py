def calc_multi(a, b):
  return a + b

print(calc_multi(5, 7))

print((lambda a, b: a * b)(3, 10))

def calc_double(x):
  return x * 2

print(calc_double(5))

for num in [1, 2, 3, 4]:
  print(calc_double(num))
