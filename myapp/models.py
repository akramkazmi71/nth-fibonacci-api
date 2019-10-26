from django.db import models

# Create your models here.
class Fibonacci():
    def __init__(self, n, fibo_num, end):
        self.number = n
        self.nth_num = fibo_num
        self.time = end
