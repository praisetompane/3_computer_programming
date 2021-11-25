try:
    age  = int(input('please enter age: '))
    risk = 100/age
    print('you are {age} years old na dhave a risk profile of {risk}')
except ValueError:
    print('age cannot be non numerical')
except ZeroDivisionError:
    print('division by zero is invalid')