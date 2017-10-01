class Rectangle(object):
    def __init__(self, w, h):
        self._width = w
        self._height = h

    def getArea(self):
        return self._width * self._height

    @property
    def width(self) :
        return self._width

    @width.setter
    def width(self, w):
        self._width = max(10, min(100, self._width))

    @property
    def height(self):
        self._width = max(10, min(100, self._width))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = max(10, min(100, self._width))
    
r1 = Rectangle(10, 10)
r1.width = 100

print("rectangle({}. {})".format(r1._width, r1._height))
print("Area : {}".format(r1.getArea()))
