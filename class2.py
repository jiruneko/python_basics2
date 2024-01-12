class MyCalcClass:

  def __init__(self, x ,y):
    self.x = x
    self.y = y

  def calc_add1(self, a, b):
    return a + b

  def calc_add2(self):
    return self.x + self.y

  def calc_multi(self, a, b):
    return a * b

  def calc_print(self, a):
    print('data:{0}:yの値{1}'.format(a, self.y))

instance_1 = MyCalcClass(1, 2)
instance_2 = MyCalcClass(5, 10)

print('2つの数の足し算(新たに数字を引数としてセット):', instance_1.calc_add1(5, 3))
print('2つの数の足し算(インスタンス化の時の値):', instance_1.calc_add2())
print('2つの数の掛け算:', instance_1.calc_multi(5, 3))
instance_1.calc_print(5)
