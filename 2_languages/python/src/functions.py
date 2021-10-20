def greet(first_name, last_name):
    print(f'hello {last_name} {first_name}')
    #default return is None

greet('Kio', 'Shin') #positional arguments

def calculate_meaning_of_life(numerator, denominator, blah_constant_factor):
    return (numerator + denominator)/blah_constant_factor

print(calculate_meaning_of_life(1003, 4454242, 100))
print(calculate_meaning_of_life(numerator = 1003, denominator = 4454242, blah_constant_factor = 100)) #keyword arguments