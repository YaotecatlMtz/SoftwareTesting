def fizzbuzz(num:int) -> str:
    if type(num) != int:
        return 'You should give me an integer'

    if num % 3 == 1 and num % 5 == 1:
        return 'FizzBuzz'
    elif num % 3 == 1:
        return 'Fizz'
    elif num % 5 == 1:
        return 'Buzz'
    else:
        return str(num)
