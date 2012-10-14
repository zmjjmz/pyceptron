class Pyceptron:


	def __init__(self, dimension=2):
		self._dimension = dimension
		self._points = []
		self._weights = [0] * (dimension + 1)
		self._steps = 0
		self._Ein = []
		self._errlimit = 0


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
			if length == 0:
				return [0.0] * len(v)
			return [dim/length for dim in v]

		return normalize(self._weights)


	def steps(self, steps=None):
		if steps != None:
			self._steps = steps
		return self._steps


	def _update(self, point, direction):
		point = [1.0] + list(point)
		for i in range(len(point)):
			self._weights[i] += direction * point[i]


	def _classify(self, point):
		point = [1] + list(point)

		def dot(u, v):
			result = 0.0
			for index in range(len(u)):
				result += u[index] * v[index]
			return result

		def sign(value):
			if value > 0:
				return 1
			if value < 0:
				return -1
			return 0

		return sign(dot(self._weights, point))

	def _ein(self):
		Ein = 0
		for i in self._points:
			if i[1] != self._classify(i[0]):
				Ein += 1
		Ein /= len(self._points)
		return Ein

	def Error(self):
		return self._Ein

	def SetErrorThreshold(self, threshold):
		self._errlimit = threshold



	def train(self, steps=None, pocket=False):

		Ein = 1

		while True:

			if steps != None:
				if steps == 0:
					return False
				steps -= 1
			self._steps += 1

			target = None

			if pocket:
				new_Ein = _ein()
				if new_Ein < Ein:
					Ein = new_Ein
				if new_Ein < self._errlimit:
					return True
				self._Ein.append(new_Ein)
				

			for point in self._points:
				if point[1] != self._classify(point[0]):
					self._update(point[0], point[1])
					break
			else:
				return True
