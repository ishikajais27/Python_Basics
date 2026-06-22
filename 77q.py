from timeit import timeit

print(timeit("1+1", number=100))

# "1+1" is the code to execute. number=100 means run it 100 times. timeit() returns the total execution time in seconds.
# timeit is a Python module used to measure how long a piece of code takes to execute.
# It returns a float representing the total execution time in seconds.