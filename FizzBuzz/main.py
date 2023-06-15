n = int(input())
message = n
if n % 3 == 0 and n % 5 == 0:
    message = "FizzBuzz"
elif n % 3 == 0:
    message = "Fizz"
elif n % 5 == 0:
    message = "Buzz"
print(message)
