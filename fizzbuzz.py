def fizzbuzz_convert(number):
    pass
    if number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return 'Buzz'


assert fizzbuzz_convert(3) == 'Fizz'
