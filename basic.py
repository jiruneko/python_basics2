import math
print((5 ** (0.5) + 1) / 2)

print(9 ** (0.5))

def felt_air_temperature(temperature, humidity):
  return temperature -1 / 2.3 * (temperature - 10) * (0.8 - humidity / 100)

print(felt_air_temperature(28, 50))
