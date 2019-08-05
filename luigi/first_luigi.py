import luigi

# to create a file one_fifty.txt with 1 to 50 numbers 
class numbers(luigi.Task):

	# if it is the first task just pass a empty list.
	def requires(self):
		return []

	# output of this task "one_fifty.txt"
	def output(self):
		return luigi.LocalTarget("one_fifty.txt")

	# opening the output file and doing necessary tasks.
	def run(self):
		with self.output().open('w') as i:
			for j in range(1, 50):
				i.write("{}\n".format(j))
			


# second task is to get the output of the first task and 
# cube all the values
class cube(luigi.Task):

	# pass the first class as this class requires the output of the first class.
	def requires(self):
		return [numbers()]

	def output(self):
		return luigi.LocalTarget("cube.txt")

	def run(self):
		with self.input()[0].open() as input_file, self.output().open('w') as output_file:
			for num in input_file:
				num_cube = int(num)**3
				output_file.write("{},{}\n".format(num, num_cube))
			


if __name__ == '__main__':
	luigi.run()
