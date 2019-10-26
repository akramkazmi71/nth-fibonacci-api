from django.test import TestCase
from myapp.views import nth_fib

# Create your tests here.
class FibonacciTestCase(TestCase):
    def test_fibo(self):
        self.assertEqual(nth_fib(1), 1)
        self.assertEqual(nth_fib(-1), 'Incorrect Input')
        self.assertEqual(nth_fib('a'), 'Incorrect Input')
        self.assertEqual(nth_fib(6), 8)
        self.assertEqual(nth_fib(True), 'Incorrect Input')
        self.assertEqual(nth_fib(6.1), 'Incorrect Input')
        self.assertEqual(nth_fib(False), 'Incorrect Input')
        self.assertEqual(nth_fib(-5.6), 'Incorrect Input')
        self.assertEqual(nth_fib(999), 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626)
        self.assertEqual(nth_fib('fibonacci'), 'Incorrect Input')
        self.assertEqual(nth_fib('%12#'), 'Incorrect Input')
        self.assertEqual(nth_fib(None), 'Incorrect Input')
