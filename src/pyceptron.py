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






class Pyceptron:


	def __init__(self, dimension=2):
		self._dimension = dimension
		self._points = None
		self._weights = [0] * (dimension) + [1]


	def populate(self, points):
		self._points = points


	def weights(self, weights=None):
		if weights != None:
			self._weights = weights
		return self._weights


	def train(self, pick=None):

		count = 0
		while True:


			target = None

			# if pick == None:
			for point in self._points:
				if sign(point[1]) != sign(dot(self._weights, [1] + list(point[0]))):
					target = point
					break
			# else:
				# point = pick(points)

			print(self._weights)
			global ideal
			# render(self._points, self._weights, ideal)

			if target == None:
				print('FOUND A SOLUTION after %d steps' % (count))
				return True

			# print('=================')
			# print(target)

			# self._weights[0] += 1 * target[1]
			# for dim in range(1, self._dimension + 1):
				# self._weights[dim] += target[1] * target[0][dim - 1]

			self._weights[0] += target[1] * 1
			self._weights[1] += target[1] * target[0][0]
			self._weights[2] += target[1] * target[0][1]
			count += 1











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
