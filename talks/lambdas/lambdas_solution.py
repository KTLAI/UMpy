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

countries.sort() # in place operation, sorted lexicographically, returns None
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries default sort() asc = {printable}")

countries = data[1:] # reset
countries.sort(key=lambda x: x[2]) # sort on happiness score
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries by score asc = {printable}")

countries = data[1:] # reset
countries.sort(key=lambda x: x[2], reverse=True) # sort on second element, reverse order
printable = [(country[0], country[2]) for country in countries[:10]]
print(f"\n.SORT(): countries score desc = {printable}")

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

# SORTED (NEW LIST) REGION, SCORE, COUNTRY ASCENDING ALL KEYS
countries = sorted(countries, key=lambda x: (x[1], x[2], x[0]))
printable = [(country[1], country[2], country[0]) for country in countries[:10]]
print(f"\nSORTED(): region, score, country  = {printable}")

# SORTED (NEW LIST) REGION, SCORE, COUNTRY MIXED ORDERING
countries = sorted(countries, key=lambda x: (x[1], -float(x[2]), x[0]))
printable = [(country[1], country[2], country[0]) for country in countries[:10]]
print(f"\nSORTED(): region, score, country  = {printable}")

# Alternative: custom function
countries = sorted(countries, key=sort_region_by_score_desc) # reference function name
printable = [(country[1], country[2], country[0]) for country in countries[:10]]
print(f"\nSORTED(): region, score, country  = {printable}")










if __name__ == "__main__":
    main()



