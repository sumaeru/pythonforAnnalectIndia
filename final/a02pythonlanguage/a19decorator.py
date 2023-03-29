# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)



def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}
def memoize_factorial(f):
	
	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			print('result saved in memory')
		else:
			print('returning result from saved memory')
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

print(facto(5))
print(facto(5)) # directly coming from saved memory


