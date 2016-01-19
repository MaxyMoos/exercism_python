def transform(old):
	new = {}
	for key in old.keys():
		values = old[key]
		for singleValue in values:
			new[singleValue.lower()] = key
	return new