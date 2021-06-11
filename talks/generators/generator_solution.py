


# CHALLENGE 07: SATELLITE COUNTS BY PLANET CATEGORY

data = {
        "mercury" : {'category': 'inner', 'satellites': 0},
        "venus" : {'category': 'inner', 'satellites': 0},
        "earth" : {'category': 'inner', 'satellites': 1},
        "mars" : {'category': 'inner', 'satellites': 2},
        "jupiter" : {'category': 'outer', 'satellites': 79},
        "saturn" : {'category': 'outer', 'satellites': 82},
        "uranus" : {'category': 'outer', 'satellites': 27},
        "neptune" : {'category': 'outer', 'satellites': 14}
    }

# { (some_key if condition else default_key):(something_if_true if condition
#      else something_if_false) for key, value in dict_.items() }

satellite_counts = {'inner': 0, 'outer': 0}
for val in data.values():
    if val['category'] == 'inner':
        satellite_counts['inner'] += val['satellites']
    else:
        satellite_counts['outer'] += val['satellites']

print(f"\nChallenge 03: satellite counts = {satellite_counts}")

# list comprehension passed to sum()
satellite_counts = {'inner': 0, 'outer': 0}
satellite_counts['inner'] = sum(val['satellites'] for val in data.values() if val['category'] == 'inner')
satellite_counts['outer'] = sum(val['satellites'] for val in data.values() if val['category'] == 'outer')

print(f"\nChallenge 04: satellite_counts = {satellite_counts}")