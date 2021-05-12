import copy
import random
from typing import List
# Consider using the modules imported above.


class Hat:

	def __init__(self, **kwargs):
		self.contents = list()

		# Utilizing 'keyword arguments' that stores arguments in a dictionary
		for key, value in kwargs.items():
			for i in range(value):
				self.contents.append(key)

	def draw(self, n: int) -> List[str]:
		"""
		This method that accepts an argument indicating the number of balls to draw from the
		hat. This method should remove balls at random from contents and return those balls
		as a list of strings. The balls should not go back into the hat during the draw,
		similar to an urn experiment without replacement. If the number of balls to draw
		exceeds the available quantity, return all the balls.
		"""
		removed = []

		if (n > len(self.contents)):
			removed = self.contents
			self.contents = []
		else:
			for i in range(n):
				pick = random.choice(self.contents)
				removed.append(pick)
				self.contents.remove(pick)

		return removed



def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
	"""
	hat: A hat object containing balls that should be copied inside the function.

	expected_balls: An object indicating the exact group of balls to attempt to draw from the
	hat for the experiment. For example, to determine the probability of drawing 2 blue balls
	and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.

	num_balls_drawn: The number of balls to draw out of the hat in each experiment.

	num_experiments: The number of experiments to perform. (The more experiments performed,
	the more accurate the approximate probability will be.)

	Returns a probability.
	"""
	m = 0
	expected = expectedList(expected_balls)

	for i in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		expected_copy = copy.deepcopy(expected_balls)
		drawn = hat_copy.draw(num_balls_drawn)

		for item in drawn:
			if (item in expected_copy):
				expected_copy[item] -= 1

		if ( all( value <= 0 for value in expected_copy.values() ) ):
			m += 1

	return m / num_experiments

