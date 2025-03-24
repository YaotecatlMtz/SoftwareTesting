import pytest
from src.tdd import *

def test_fizzbuzz():
    fizzbuzz(5) == 'Buzz'
    fizzbuzz(3) == 'Fizz'
    fizzbuzz(15) == 'FizzBuzz'
    fizzbuzz('lol') == 'You should give me an integer'
    fizzbuzz(7) == '7'
