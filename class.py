class PrintClass:
  def print_me(self):
    print(self.x, self.y)

pl = PrintClass()

pl.x = 10
pl.y = 100
pl.z = 1000

pl.print_me()

print(pl.z)
