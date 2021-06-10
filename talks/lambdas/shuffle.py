# import arwutils.utils as utils
import umpy_utils as umpy
import random


def main():
    """Entry point to program."""

# Read
input_path = './input/happiness-2019.csv'
data = umpy.read_csv(input_path)

input_path = './input/m49.csv'
codes = umpy.read_csv(input_path)

# Extract headers
data_headers = data[0]

code_headers = codes[0]

# Warn: Kosovo (Southern Europe), Hong Kong (Eastern Asia), Taiwan (Eastern Asia), and Northern Cyprus (Western Asia)
# must be matched manually
for country in data:
    for code in codes:
        if country[data_headers.index('Country')].lower() == code[code_headers.index('Country or Area')].lower():
            country.insert(2, code[code_headers.index('Sub-region Name')])

data_headers.insert(2, 'Region')

# Shuffle (countries only)
countries = data[1:]
random.shuffle(countries) # shuffle order

print(countries[0])

# Write
output_path = './output/happiness-shuffled-2019.csv'
umpy.write_csv(output_path, countries, data_headers)

# Remove "Overall Rank" column
unranked_countries = [country[1:] for country in countries]

output_path = './output/happiness-shuffled-unranked-2019.csv'
umpy.write_csv(output_path, unranked_countries, data_headers[1:])


if __name__ == "__main__":
    main()
