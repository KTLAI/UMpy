import string
import umpy_utils as utl

from stop_words import stop_words


# CHALLENGE 01: NUMBERS

filepath = './input/south_africa-life_expectancy-1960_2019.csv'
data = utl.read_csv(filepath)

headers = data[0]
female_life_exp = data[1][4:]
male_life_exp = data[2][4:]

print(female_life_exp)

# map(): convert to float (working with a list)
female_life_exp_flt = list(map(float, female_life_exp))

print(f"\nChallenge 01: female life expectancy (float) = {female_life_exp_flt}")

# map(): convert to dict using dict()/zip(); convert values to float using map()
headers_years = headers[4:]
male_life_exp_flt = dict(zip(headers_years, map(float, male_life_exp)))

print(f"\nChallenge 01: dict()/zip()/map() male life expectancy = {male_life_exp_flt}")

# dictionary comprehension
male_life_exp_flt = {headers_years[i]: float(male_life_exp[i]) for i in range(len(headers_years))}

print(f"\nChallenge 01: dict comp: male life expectancy (float) = {male_life_exp_flt}")





# CHALLENGE 02: GET SPEECH
# WARN: 1/2 lines in file are blank
filepath = './input/mandela-prepared_speech.txt'

# loop
with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
    data_loop = []
    for line in file_obj:
        if line.strip(): # truth value (not None)
            data_loop.append(line)

print(f"\nChallenge 02: loop: data length = {len(data_loop)}")
print(f"\nChallenge 02: loop: last line = {data_loop[-1]}")

# map()
with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
    # This does not work; lambda needs an else:
    # data_map = list(map(lambda x: x.strip() if (x.strip()), file_obj.readlines()))

    # map() and filter()
    # data_map = list(map(lambda x: x.strip(), filter(lambda x: x.strip() != '', file_obj.readlines())))
    data_map = list(map(lambda x: x.strip(), filter(lambda x: x.strip(), file_obj.readlines())))

print(f"\nChallenge 02: map()/filter(): data length = {len(data_map)}")
print(f"\nChallenge 02: map()/filter(): last line = {data_map[-1]}")

# list comprehension
with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
    data_comp = [line.strip() for line in file_obj.readlines() if line.strip()]

print(f"\nChallenge 02: comp: data length = {len(data_comp)}")
print(f"\nChallenge 02: comp: last line = {data_comp[-1]}")


# CHALLENGE 03: CLEAN DATA

# 3-argument version of str.maketrans
# arguments (x, y, z) where 'x' and 'y' must be equal-length strings
# characters in 'x' are replaced by characters in 'y'
# 'z' is string.punctuation where each character in the string is mapped to None

translator = str.maketrans('', '', string.punctuation)

# loop
data_cleaned_loop = []
for line in data_loop:
    data_cleaned_loop.append(line.translate(translator).lower())

print(f"\nChallenge 03: loop: last line = {data_cleaned_loop[-1]}")

# map()
data_cleaned_map = list(map(lambda x: x.translate(translator).lower(), data_map))

print(f"\nChallenge 03: map(): last line = {data_cleaned_map[-1]}")

# list comprehension
data_cleaned_comp = [line.translate(translator).lower() for line in data_comp]

print(f"\nChallenge 03: comp: last line = {data_cleaned_comp[-1]}")


# CHALLENGE 04: STATS

para_lengths = list(map(len, data_cleaned_map))

print(f"\nChallenge 04: paragraph lengths = {para_lengths}")

# CHALLENGE 04: SEARCH (FILTER())

search_term = 'apartheid'
# search_term = 'white supremacy'
# search_term = 'communist'
# search_term = 'freedom charter'

# filter()
lines = list(filter(lambda x: search_term in x, data_cleaned_map))

print(f"\nChallenge 04: filter: search len = {len(lines)}")
print(f"\nChallenge 04: filter: search")
for line in lines:
    print(f"\n{line}")

# list comprehension
lines = [line for line in data_cleaned_comp if search_term in line]

print(f"\nChallenge 04: comp: search len = {len(lines)}")
print(f"\nChallenge 04: comp: search")
for line in lines:
    print(f"\n{line}")






