from django.shortcuts import render
from django.http import HttpResponse
import json
import time
from myapp.models import Fibonacci

def index(request):
    return HttpResponse('<head><title>Nth Fibonacci Number</title></head><center><h1>Enter the Postion:</h1><form name="val" action="/fibo/" method="get"><input type="text" name="val"><input type="submit" value="Submit"></form>')

def nth_fib(n):
	if not isinstance(n, int) or n < 0 or isinstance(n, bool):
		return "Incorrect Input"
	return _fib(n)[0]

def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

def get_num(request):
    if request.method == 'GET':
        num=request.GET.get('val')
        try:
            n=int(num)
            start = time.time()
            fibo_num = nth_fib(n)
            if fibo_num=="Incorrect Input":
                i=1/0
            end = time.time() - start
            fib = Fibonacci(n, fibo_num, end)
            response = '<center><h1>Fibonacci Number at {} position:</h1>{}<h1>Time Taken:</h1>{}'.format(n, fib.nth_num, fib.time)
            return HttpResponse(response)
        except:
            response = '<center><h1>Enter a valid number</h1>'
            return HttpResponse(response)

