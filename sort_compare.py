## IS211 Assignment 4 - sort_compare.py
import time
import random 
def main():
	def insertion_sort(a_list):
		time_start = time.time()
		for index in range(1, len(a_list)):
			current_value = a_list[index]
			position = index
			
			while position > 0 and a_list[position - 1] > current_value:
				a_list[position] = a_list[position - 1]
				position = position - 1
			
			a_list[position] = current_value
		time_end = time.time()
		return time_end - time_start

		
	def shell_sort(a_list):
		time_start = time.time()
		sublist_count = len(a_list) // 2
		while sublist_count > 0:
			for start_position in range(sublist_count):
				gap_insertion_sort(a_list, start_position, sublist_count)
			#print("After increments of size", sublist_count, "The list is", a_list)
			sublist_count = sublist_count // 2
		time_end = time.time()
		return time_end - time_start
			

	def gap_insertion_sort(a_list, start, gap):
		for i in range(start + gap, len(a_list), gap):
			current_value = a_list[i]
			position = i
			while position >= gap and a_list[position - gap] > current_value:
				a_list[position] = a_list[position - gap]
				position = position - gap
			a_list[position] = current_value
		

	def python_sort(a_list):
		time_start = time.time()
		a_list.sort()
		time_end = time.time()
		return time_end - time_start
		
		
	input_list_500 = []
	input_list_1k = []
	input_list_10k = []

	is_outputs_500 = []
	is_outputs_1k = []
	is_outputs_10k = []

	shell_outputs_500 = []
	shell_outputs_1k = []
	shell_outputs_10k = []

	py_outputs_500 = []
	py_outputs_1k = []
	py_outputs_10k = []
	# NOTE: Per the assignment, list_count is set to 100.  However I have been experiencing extremely slow code, so changing this to a lower number is helpful.
	list_count = 100
	for i in xrange(list_count):
		# Using random samples, since previous method was leading to extreme slowdown
		input_list_500 = random.sample(xrange(500),500)
		input_list_1k = random.sample(xrange(1000),1000)
		input_list_10k = random.sample(xrange(10000),10000)
		
		# for y in xrange(500):
			# input_list_500.append(random.random() * 1000)
		# for q in xrange(1000):
			# input_list_1k.append(random.random() * 5000)
		# for p in xrange (10000):
			# input_list_10k.append(random.random() * 100000)
		# Insertion Sort Outputs
		is_outputs_500.append(insertion_sort(input_list_500))
		is_outputs_1k.append(insertion_sort(input_list_1k))
		is_outputs_10k.append(insertion_sort(input_list_10k))
		print("Insertion Sort: ",i) # Progress Report
		# Shell Sort Outputs
		shell_outputs_500.append(shell_sort(input_list_500))
		shell_outputs_1k.append(shell_sort(input_list_1k))
		shell_outputs_10k.append(shell_sort(input_list_10k))
		print("Shell Sort: ",i) # Progress Report
		# Python Sort Outputs
		py_outputs_500.append(python_sort(input_list_500))
		py_outputs_1k.append(python_sort(input_list_1k))
		py_outputs_10k.append(python_sort(input_list_10k))
		print("Python Sort: ",i) # Progress Report
	# Computing Averages for Outputs
	is_average_500 = sum(is_outputs_500) / float(len(is_outputs_500))
	is_average_1k = sum(is_outputs_1k) / float(len(is_outputs_1k))
	is_average_10k = sum(is_outputs_10k) / float(len(is_outputs_10k))

	shell_average_500 = sum(shell_outputs_500) / float(len(shell_outputs_500))
	shell_average_1k = sum(shell_outputs_1k) / float(len(shell_outputs_1k))
	shell_average_10k = sum(shell_outputs_10k) / float(len(shell_outputs_10k))

	py_average_500 = sum(py_outputs_500) / float(len(py_outputs_500))
	py_average_1k = sum(py_outputs_1k) / float(len(py_outputs_1k))
	py_average_10k = sum(py_outputs_500) / float(len(py_outputs_10k))


	# Printing Outputs

	print "Insertion Sort took %10.7f seconds, on average, to run over a list of length 500" % is_average_500
	print "Insertion Sort took %10.7f seconds, on average, to run over a list of length 1000" % is_average_1k
	print "Insertion Sort took %10.7f seconds, on average, to run over a list of length 10000" % is_average_10k
	print "\n"
	print "Shell Sort took %10.7f seconds, on average, to run over a list of length 500" % shell_average_500
	print "Shell Sort took %10.7f seconds, on average, to run over a list of length 1000" % shell_average_1k
	print "Shell Sort took %10.7f seconds, on average, to run over a list of length 10000" % shell_average_10k
	print "\n"
	print "Python Sort took %10.7f seconds, on average, to run over a list of length 500" % py_average_500
	print "Python Sort took %10.7f seconds, on average, to run over a list of length 1000" % py_average_1k
	print "Python Sort took %10.7f seconds, on average, to run over a list of length 10000" % py_average_10k

main()



