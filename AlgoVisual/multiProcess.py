import multiprocessing as mp
import time
import random
import csv
from AlgoVisual import sort_algo as sort

# comparing multiple sorting algo
# Define time analysis functions

def bubble_time_analysis(queue, arr, sequence):
	start_time = time.time()
	sort.bubble_sort(arr)
	end_time = round(time.time() - start_time, 5)
	queue.put((end_time, sequence))

def selection_time_analysis(queue, arr, sequence):
	start_time = time.time()
	sort.selection_sort(arr)
	end_time = round(time.time() - start_time, 5)
	queue.put((end_time, sequence))

def insertion_time_analysis(queue, arr, sequence):
	start_time = time.time()
	sort.insertion_sort(arr)
	end_time = round(time.time() - start_time, 5)
	queue.put((end_time, sequence))

def merge_time_analysis(queue, arr, sequence):
	start_time = time.time()
	sort.merge_sort(arr)
	end_time = round(time.time() - start_time, 5)
	queue.put((end_time, sequence))

def quick_time_analysis(queue, arr, sequence):
	start_time = time.time()
	sort.quick_sort(arr)
	end_time = round(time.time() - start_time, 5)
	queue.put((end_time, sequence))

# Main performance analysis function

def sorting_performance_analysis(arr):
	queue = mp.Queue()

	# Define processes for each sorting function
	sorting_processes = [
		mp.Process(target=bubble_time_analysis, args=(queue, arr, 0)),
		mp.Process(target=selection_time_analysis, args=(queue, arr, 1)),
		mp.Process(target=insertion_time_analysis, args=(queue, arr, 2)),
		mp.Process(target=merge_time_analysis, args=(queue, arr, 3)),
		mp.Process(target=quick_time_analysis, args=(queue, arr, 4))
	]

	# Start all processes
	for process in sorting_processes:
		process.start()

	# Collect results in the correct order
	results = [queue.get() for _ in sorting_processes]
	time_lst = [0]*len(results)
	for time, i in results:
		time_lst[i] = time

	# Join all processes
	for process in sorting_processes:
		process.join()

	return time_lst


# Global variables
case_mapping = {0: 'Best_case', 1: 'Average_case', 2: 'Worst_case'}

# Function for array creation
def array(size):
	lst_asc = list(range(size))         # for best case
	lst_random = lst_asc.copy()         # for average case
	random.shuffle(lst_random)
	lst_des = lst_asc[::-1]             # for worst case
	return [lst_asc, lst_random, lst_des]

# Function for process execution
def process(lst, case_index, result_queue, sort_name):
	start_time = time.time()

	if sort_name == 'bubble':
		sort.bubble_sort(lst)
	elif sort_name == 'selection':
		sort.selection_sort(lst)
	elif sort_name == 'insertion':
		sort.insertion_sort(lst)
	elif sort_name == 'merge':
		sort.merge_sort(lst)
	elif sort_name == 'quick':
		sort.quick_sort(lst)

	end_time = round(time.time() - start_time, 5)
	result_queue.put((case_index, end_time))

# Function to measure time for different cases
def time_measure(size, result_queue, sort_name):
	all_cases = array(size)
	if sort_name == 'quick':
		all_cases[1], all_cases[0] = all_cases[0], all_cases[1]

	for case_index, lst in enumerate(all_cases):
		p = mp.Process(target=process, args=(lst, case_index, result_queue, sort_name))
		p.start()

# Main function to measure time complexity for different sizes
def main(sort_name):
	result_queue = mp.Queue()
	processes = []

	# Start processes for each size
	for i in range(1, 51):
		p = mp.Process(target=time_measure, args=(i, result_queue, sort_name))
		p.start()
		processes.append(p)

	# Wait for all processes to finish
	for p in processes:
		p.join()

	# Initialize dictionaries for best, average, and worst cases
	best_case = {}
	average_case = {}
	worst_case = {}

	# Process results
	while not result_queue.empty():
		case_index, time_elapsed = result_queue.get()
		case = case_mapping[case_index]
		if case == 'Best_case':
			best_case[len(best_case) + 1] = time_elapsed
		elif case == 'Average_case':
			average_case[len(average_case) + 1] = time_elapsed
		elif case == 'Worst_case':
			worst_case[len(worst_case) + 1] = time_elapsed

	# Write data to CSV file
	if sort_name == 'bubble':
		csv_file = "static/bubblesort_time_complexity.csv"
	elif sort_name == 'selection':
		csv_file = "static/selectionsort_time_complexity.csv"
	elif sort_name == 'insertion':
		csv_file = "static/insertionsort_time_complexity.csv"
	elif sort_name == 'merge':
		csv_file = "static/mergesort_time_complexity.csv"
	elif sort_name == 'quick':
		csv_file = "static/quicksort_time_complexity.csv"
	
	with open(csv_file, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Size', 'Best_case', 'Average_case', 'Worst_case'])
		for size in range(1, 51):
			writer.writerow([size, best_case.get(size, ""), average_case.get(size, ""), worst_case.get(size, "")])
	print("Data has been written to", csv_file)
