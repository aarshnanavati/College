class Point:
   def __init__( self, x, y):
      self.x = x
      self.y = y
      print(x)
      print(y)
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point(5,6)

del pt1
