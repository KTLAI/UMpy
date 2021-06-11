import operator
import umpy_utils as umpy


def sort_region_by_score_desc(country):
    """Convert score to a negative value."""
    return (country[1], -float(country[2]), country[0])


def main():
    """Entry point to program."""

# Source
# https://www.kaggle.com/unsdsn/world-happiness?select=2019.csv

# Columns

# Country
# Rank
# GDP per capita
# Social support
# Healthy life expectancy
# Freedom to make life choices
# Generosity
# Perceptions of corruption

# Read
input_path = './input/happiness-shuffled-unranked-2019.csv'
data = umpy.read_csv(input_path)

# Extract headers and countries
headers = data[0]
print(f"\nHappiness headers = {headers}")

countries = data[1:]
print(f"\nCountries random (limit=10) = {countries[:10]}")

# LIST METHOD .sort()

# TODO FIX SORT BY SCORE

# Lexicographic sort
countries.sort() # in place operation, sorted lexicographically, returns None
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries default sort() asc = {printable}")

# Lexicographic sort
countries = data[1:] # reset
countries.sort(key=lambda x: x[2]) # sort on happiness score
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries by score asc = {printable}")

# Lexicographic sort
countries = data[1:] # reset
countries.sort(key=lambda x: x[2], reverse=True) # sort on second element, reverse order
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries score desc = {printable}")

# Numeric sort
countries = data[1:] # reset
countries.sort(key=lambda x: float(x[2]), reverse=True) # sort on second element, reverse order
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries score desc float = {printable}")

# Alternative (operator.itemgetter())
countries = data[1:] # reset
countries.sort(key=operator.itemgetter(2), reverse=True) # TypeError: sort() takes no positional arguments
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT() ITEMGETTER(): countries score desc = {printable}")


# RESET
countries = data[1:] # reset

# SORTED (NEW LIST) RANK DESC
countries = sorted(countries, key=lambda x: x[1], reverse=True)
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\nSORTED(): Countries rank desc = {printable}")

# Alternative
countries = sorted(countries, key=operator.itemgetter(1), reverse=True)
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\nSORTED() ITEMGETTER(): countries rank desc = {printable}")


# SORT MULTIPLE COLUMNS

# SORTED (NEW LIST) REGION, SCORE, COUNTRY ASCENDING ALL KEYS
countries = sorted(countries, key=lambda x: (x[1], float(x[2]), x[0])) # tuple of values
writable = [(country[1], country[0], country[2]) for country in countries if 'Europe' in country[1]]
output_path = './output/europe-happiness.csv'
umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))

# SORTED (NEW LIST) REGION, SCORE, COUNTRY MIXED ORDERING
countries = sorted(countries, key=lambda x: (x[1], -float(x[2]), x[0])) # negative value (sorting hack)
writable = [
    (country[1], country[0], country[2])
    for country in countries
    if country[1] == 'Sub-Saharan Africa'
    ]
output_path = './output/africa-happiness.csv'
umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))

# Alternative: local function
countries = sorted(countries, key=sort_region_by_score_desc) # reference function name
writable = [
    (country[1], country[0], country[2])
    for country in countries
    if country[1] == 'Eastern Asia'
    ]
output_path = './output/east_asia-happiness.csv'
umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))

# Add ranking write out all values
countries = sorted(countries, key=lambda x: float(x[2]), reverse=True) # negative value (sorting hack)

rankings = []
for i, country in enumerate(countries, 1):
    # country.insert(0, i)
    # rankings.append(country)

    # [i].extend(country)
    # rankings.append(i)

    rankings.append([i] + country) # expression returns a new list

# headers.insert(0, 'Rank') # Don't mutate headers
output_path = './output/world_rank-happiness-loop.csv'
umpy.write_csv(output_path, rankings, ['Rank'] + headers)

# Warn: country.insert(0, i) and [i].extend(country) not appropriate in a comprehension
# Both methods return None and trigger a runtime error when the list is passed to write_csv().
# _csv.Error: iterable expected, not NoneType

# writable = [country.insert(0, i) for i, country in enumerate(countries, 1)]
# writable = [[i].extend(country) for i, country in enumerate(countries, 1)]

writable = [[i] + country for i, country in enumerate(countries, 1)]
output_path = './output/world_rank-happiness.csv'
umpy.write_csv(output_path, writable, ['Rank'] + headers)


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






if __name__ == "__main__":
    main()



