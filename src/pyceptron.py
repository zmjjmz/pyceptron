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
		return self._weights


	def _update(self, point, direction):
		point = [1] + list(point)
		for dim in range(self._dimension):
			self._weights[dim] += point[dim] * direction


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
				if sign(point[1]) != self._classify(point[0]):
					self._update(point[0], point[1])
					break
			else:
				return True




from matplotlib import pyplot as plt
from random import randint, uniform


def dot(v1, v2):
	result = 0.0
	for index in range(len(v1)):
		result += v1[index] * v2[index]
	# print(v1, 'dot', v2, '=', result)
	return result

def sign(value):
	return -1 if value < 0 else 1


def line(w, x):
	w2=w[2]
	if w2 == 0:
		w2 = .000001
	return (w[1] * x + w[0]) / float(-1 * w2)


def render(points, weights, ideal):
	plt.axis([-10, 10, -10, 10])

	for point in points:
		if point[1] < 0:
			plt.plot(point[0][0], point[0][1], 'rv')
		else:
			plt.plot(point[0][0], point[0][1], 'g^')


	plt.plot([-10, 10], [line(ideal, -10), line(ideal, 10)], 'k-')
	plt.plot([-10, 10], [line(weights, -10), line(weights, 10)], 'b-')
	# print([0, 5], [line(weights, 0), line(weights, 5)])

	plt.show()





ideal = [34,77,81]

points = []
for _ in range(500):
	x = uniform(-10, 10)
	y = uniform(-10, 10)
	h = sign(dot(ideal,[1,x,y]))
	points.append(((x, y), h))




pt = Pyceptron(2)
pt.populate(points)
pt.weights([randint(1,100), randint(1,100), randint(1,100)])
if pt.train():
	print(pt.weights())
	render(points, pt.weights(), ideal)
