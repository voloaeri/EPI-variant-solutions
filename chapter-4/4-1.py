# Following three must complete in O(1) time

# Right propagate the rightmost set bit in x (01010000 -> 01011111)
def right_propagate(x):
    return x-1 | x

# Compute x mod a power of two  (17 mod 8 = 1)
# Cannot be tested: INFINITE number of bits are used for Python negative numbers.
# -5 is treated by bitwise operators as if it were written "...1111111111111111111011".
def mod_power_2(x,a):
     a = a << 1
     return x ^ -a

# Return true if x is a power of 2
def is_power_of_2(x):
    return (x ^ right_propagate(x)) == (x - 1)


#test cases

print("Right progpagation of {} is {}".format(bin(64), bin(right_propagate(64))))
print("Right progpagation of {} is {}".format(bin(200), bin(right_propagate(200))))
# print("26 mod 4 is {}".format(mod_power_2(26,4)))
# print("21 mod 8 is {}".format(mod_power_2(21,8)))
print("Is 16 a power of 2: {}".format(is_power_of_2(16)))
print("Is 30 a power of 2: {}".format(is_power_of_2(30)))
