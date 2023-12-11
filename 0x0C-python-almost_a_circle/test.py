class Base:
  num_base = 0
  def __init__(self, id=None):
    if id is not None:
      self.id = id
    else:
      Base.num_base += 1
      self.id = Base.num_base

class Rectangle(Base):
  def __init__(self, width, height, x=0, y=0, id=None):
    self.__width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

  @property
  def width(self):
    return self.__width
  
  @width.setter
  def width(self, value):
    self.__width = value

class Square(Rectangle):
  def __init__(self, size, x=0, y=0, id=None):
    self.size = size
    super().__init__(self.size, self.size, x, y, id)


s1 = Square(5)

print(s1.size)
print(s1.width)
print(s1.height)



print(s1.__class__.__name__)