class Vector2D:
  x = 0.0
  y = 0.0
  #define
  def Set(self, x, y):
    self.x = x
    self.y = y

def Main():
  v = Vector2D()
  v.Set(5,6)
  print("X: " + str(v.x) + ", Y: " + str(v.y))

if __name__ == "__main__":
    Main()