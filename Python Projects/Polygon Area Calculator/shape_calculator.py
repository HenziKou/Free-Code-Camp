import math


class Rectangle:

	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height

	def __str__(self) -> str:
		return f"Rectangle(width={self.width}, height={self.height})"

	def setWidth(self, new_width: int) -> None:
		self.width = new_width

	def setHeight(self, new_height: int) -> None:
		self.height = new_height

	def getArea(self) -> int:
		""" Returns area (width * height) """
		return (self.width * self.height)

	def getPerimeter(self) -> int:
		""" Returns perimeter (2 * width + 2 * height) """
		return (2 * self.width + 2 * self.height)

	def getDiagonal(self) -> float:
		""" Returns diagonal ( (width ** 2 + height ** 2) ** 0.5 ) """
		return ( (self.width ** 2 + self.height ** 2) ** 0.5 )

	def getPicture(self) -> str:
		"""
		Returns a string that represents the shape using lines of "*". The number of lines
		should be equal to the height and the number of "*" in each line should be equal to
		the width. There should be a new line (\n) at the end of each line. If the width or
		height is larger than 50, this should return the string: "Too big for picture.".
		"""
		shape = ""

		if (self.width > 50 or self.height > 50):
			return "Too big for picture."
		else:
			row = "*" * self.width
			for i in range(self.height):
				shape += row + '\n'
			return shape

	def getAmountInside(self, shape) -> int:
		"""
		Takes another shape (square or rectangle) as an argument. Returns the number of
		times the passed in shape could fit inside the shape (with no rotations).
		For instance, a rectangle with a width of 4 and a height of 8 could fit in two
		squares with sides of 4.
		"""
		return math.floor( self.getArea() / shape.getArea() )



class Square:

	def __init__(self, shape: int):
		super().__init__(shape, shape)
		self.shape = shape

	def __str__(self) -> str:
		return f"Square(side={self.side})"

	def setSide(self, new_side: int) -> None:
		super().__init__(new_side, new_side)
		self.side = new_side

	def setWidth(self, new_width: int) -> None:
		super().__init__(new_width, new_width)
		self.side = new_width

	def setHeight(self, new_height: int) -> None:
		super().__init__(new_height, new_height)
		self.side = new_height

