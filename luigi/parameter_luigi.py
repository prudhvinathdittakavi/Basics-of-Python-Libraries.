

import luigi
import sys

# to create a file one_fifty.txt with 1 to 50 numbers 
class numbers(luigi.Task):
	# parameter for how many numbers to print
	n = luigi.IntParameter()

	# if it is the first task just pass a empty list.
	def requires(self):
		return []

	# output of this task "one_fifty.txt"
	def output(self):
		return luigi.LocalTarget("one_n.txt")

	# opening the output file and doing necessary tasks.
	def run(self):
		with self.output().open('w') as i:
			for j in range(1, self.n + 1):
				i.write("{}\n".format(j))
			


# second task is to get the output of the first task and 
# pth power of all the values
class power(luigi.Task):
	# what power of the numbers to return
	n = luigi.IntParameter(sys.argv[0])
	pw = luigi.IntParameter(sys.argv[1])

	# pass the first class as this class requires the output of the first class.
	def requires(self):
		return [numbers(n = self.n)]

	def output(self):
		return luigi.LocalTarget("power.txt")

	def run(self):
		with self.input()[0].open() as input_file, self.output().open('w') as output_file:
			for num in input_file:
				num_power = int(num)**self.pw
				output_file.write("{},{}\n".format(num, num_power))
			


if __name__ == '__main__':
	luigi.run()
