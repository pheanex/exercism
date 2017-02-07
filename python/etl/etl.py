def transform(score_map):
    new_map = dict()
    for key, values in score_map.items():
        for value in values:
            new_map[value.lower()] = key
    return new_map
