pyceptron
=========

An n-dimensional hyperplanar perceptron

Usage
-----

### Importing

```python
from pyceptron import Pyceptron
````

### Constructing

```python
# Constructor assumes 2 dimensions
tron = Pyceptron()

# Or, if you want a perceptron in some other dimension
tron = Pyceptron(4)
```

### Creating points

```python
# Each data point is a combination of an n-dimensional array, and a classification (-1 or 1)

# 2-dimensional data
points1d = [
	([0.25],  1),
	([0.50],  1),
	([1.00], -1),
	([1.25], -1)
]

# 2-dimensional data
points2d = [
	([0, 3],  1),
	([1, 2],  1),
	([2, 1], -1),
	([3, 0], -1)
]

# 3-dimensional data
points3d = [
	([1,  2,  3],  1),
	([2,  4,  6],  1),
	([4,  8, 12), -1),
	([8, 16, 24), -1)
]
```

### Populating

```python
tron.populate(points2d)
```

### Training

```python
# By default, the algorithm rill run until it finds a solution
tron.train()

# Or, you can give it a max number of steps
if tron.train(100) != True:
	print('No solution was found in 100 iterations...')
else:
	print('A solution was found!')

# You can even give it a max precision!
tron.SetErrorThreshold(0.05)
if tron.train(True) != True:
	print('No solution was found with an error below 5%')
else:
	print('A solution was found with an error below 5%')

# Of course, you can keep training without losing state
if tron.train(100) != True:
	print('No solution was found in 100 iterations...')
	if tron.train(50) != True:
		print('No solution was found in 150 iterations...')
	else:
		print('A solution was found within 150 iterations!')
else:
	print('A solution was found within 100 iterations!')
```

### Weights

``` python
	# Getting weights
	weights = tron.weights()

	# Setting weights
	# Note - For n-dimensional data points, you have n+1 weights
	tron.weights([12, 33, 56])
```
