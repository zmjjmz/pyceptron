class Pyceptron:


	def __init__(self, dimension=2):
		self._dimension = dimension
		self._points = []
		self._weights = [0] * (dimension) + [1]


	def populate(self, points=None):
		if points != None:
			self._points += points
		return self._points



	def weights(self, weights=None):
		if weights != None:
			self._weights = weights

		def normalize(v):
			from math import sqrt
			sum = 0.0
			for dim in v:
				sum += dim * dim
			length = sqrt(sum)
			return [dim/length for dim in v]

		return normalize(self._weights)


	def _update(self, point, direction):
		point = [1] + list(point)
		for dim in range(self._dimension):
			self._weights[dim] += point[dim] * direction
		# print(self.weights())


	def _classify(self, point):
		point = [1] + list(point)

		def dot(u, v):
			result = 0.0
			for index in range(len(u)):
				result += u[index] * v[index]
			return result

		def sign(value):
			return -1 if value < 0 else 1

		return sign(dot(self._weights, point))


	def train(self, steps=None):

		while True:

			if steps != None:
				if steps == 0:
					return False
				steps -= 1

			target = None

			for point in self._points:
				if point[1] != self._classify(point[0]):
					self._update(point[0], point[1])
					break
			else:
				return True
