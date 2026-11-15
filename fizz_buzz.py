#print numbers 0-100
for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:   #divisible 3 and 5
        print("FizzBuzz")
    elif numbers % 3 == 0:                      #numbers divisible by 3
        print("fizz")
    elif numbers % 5 == 0:                      #number divisible by 5
        print("buzz")
    else:
        print(numbers)