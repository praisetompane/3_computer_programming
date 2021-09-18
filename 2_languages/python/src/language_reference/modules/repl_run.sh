python3

#import version 1
import number_funcs
number_funcs.adder(1,3)
number_funcs.generalised_adder(1,2)

#import version 2
from number_funcs import adder, generalised_adder
adder(1,4)
generalised_adder(3,4)