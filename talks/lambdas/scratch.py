# TODO arithmetic

['Rank'] + headers

# Using Lambda: Lambda definition does not include a “return” statement,
# it always contains an expression that is returned. We can also put a lambda definition anywhere
# a function is expected, and we don’t have to assign it to a variable at all. This is the
# simplicity of lambda functions.

# def multipler(multiplicand, multiplier):
#     try:
#         return float(multiplicand) * multiplier # expression assigned
#     except ValueError as err:
#         print(err.args)

# def multiplier(multiplier):
#     """Returns lambda expression."""
#     return lambda multiplicand: multiplicand * multiplier

multiplier = lambda multiplicand, multiplier: multiplicand * multiplier
# multiplier = lambda x: x * y

for country in countries:
    for i in range(2, len(country)):
        val = multiplier(float(country[i]), 100) # call lambda
        country[i] = round(val, 2)

print(f"\n Arithmetic = {countries[0]}")

# TODO ADD country[3:]

adder = lambda x: sum(x)
val = adder([1, 2, 3])
print(val)